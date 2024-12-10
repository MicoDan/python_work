from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import ContactDetails, Register, PersonalInfo, CardioData, Metric
from datetime import datetime, timedelta
from django.urls import reverse
from django.http import JsonResponse

# Home page view
def home(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getemail = request.POST.get('email')
        getmessage = request.POST.get('message')

        user = ContactDetails(name=getname, email=getemail, message=getmessage)
        user.save()

    return render(request, 'html/home.html')

# User registration view
def registerpage(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getemail = request.POST.get('email')
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        getconfirm_password = request.POST.get('confirm_password')
        users = Register(name=getname, email=getemail, username=getusername, password=getpassword, confirm_password=getconfirm_password)
        users.save()
    return render(request, 'html/registerpage.html')

# User login view
def loginpage(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        try:
            Register.objects.get(username=getusername, password=getpassword)
            return redirect('home_page')
        except:
            return HttpResponse('Invalid user')
    return render(request, 'html/loginpage.html')

# Admin login view
def adminlogin(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        if getusername == 'admin' and getpassword == 'admin':
            return redirect(reverse('admin_dashboard'))  # Redirect to admin dashboard
        else:
            return HttpResponse('Invalid Credentials')
    return render(request, 'html/admin_login.html')

# Admin dashboard view
def admin_dashboard(request):
    # Fetch counts for approved and pending athletes
    approved_count = Register.objects.filter(Status=True).count()
    pending_count = Register.objects.filter(Status=False).count()

    # Example: Fetch historical data for the last 7 days
    today = datetime.now()
    dates = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
    approved_counts = []
    pending_counts = []

    for date in dates:
        approved_counts.append(Register.objects.filter(Status=True, created_at__date=date).count())
        pending_counts.append(Register.objects.filter(Status=False, created_at__date=date).count())

    context = {
        'approved_count': approved_count,
        'pending_count': pending_count,
        'dates': dates,
        'approved_counts': approved_counts,
        'pending_counts': pending_counts,
    }

    return render(request, 'html/admin_dashboard.html', context)

# View for pending user registrations
def pending(request):
    details = Register.objects.filter(Status=False)
    return render(request, 'html/pending.html', {'value': details})

def approve(request, id):
    data = get_object_or_404(Register, id=id)
    data.Status = True
    data.save()
    return redirect('pending_list')

def delete(request, id):
    data = get_object_or_404(Register, id=id)
    data.delete()
    return redirect('pending_list')

# View for approved users
def approved(request):
    approved_users = Register.objects.filter(Status=True)
    return render(request, 'html/approve.html', {'approved_users': approved_users})

def approved_api(request):
    approved_users = Register.objects.filter(Status=True)
    users_list = list(approved_users.values()) 
    return JsonResponse(users_list, safe=False)

def delete_approved_user(request, id):
    data = get_object_or_404(Register, id=id)
    data.delete()
    return redirect('approve_list')

# Health information form submission
def health(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getheight = request.POST.get('height')
        getweight = request.POST.get('weight')
        getnationality = request.POST.get('nationality')
        getlevel = request.POST.get('competition_level')
        gettraining = request.POST.get('training_frequency')
        savedata = PersonalInfo(name=getname, height=getheight, weight=getweight,
                                 nationality=getnationality, competition_level=getlevel, training_frequency=gettraining)
        savedata.save()
    return render(request, 'html/health_data.html')



# Cardio data form submission

# Cardio data form submission
def cardio(request):
    context = {}  # Initialize the context to avoid issues

    if request.method == 'POST':
        # Retrieve POST data with validation
        getresting = request.POST.get('resting_heart_rate')
        getage = request.POST.get('age')
        getgender = request.POST.get('gender')
        getmax = request.POST.get('max_heart_rate')
        getsystolic = request.POST.get('systolic')
        getdiastolic = request.POST.get('diastolic')
        getvo2 = request.POST.get('vo2_max')
        gethrv = request.POST.get('hrv')
        getrecovery = request.POST.get('recovery_time')
        getcardiac = request.POST.get('cardiacOutput')
        getldl = request.POST.get('ldlCholesterol')
        gethdl = request.POST.get('hdlCholesterol')
        gettri = request.POST.get('triglycerides')
        getfBloodSugar = request.POST.get('fastingBloodSugar')
        getpBloodSugar = request.POST.get('postprandialBloodSugar')
        getblood_sugar_condition = request.POST.get('bloodSugarIssues')
        getfamilyHistory = request.POST.get('familyHistory')
        cardiac_events = request.POST.get('cardiac_events', 'No Events')

        # Validate numerical data before saving
        try:
            resting_heart_rate = int(getresting)
            age = int(getage)
            max_heart_rate = int(getmax)
            systolic = int(getsystolic)
            diastolic = int(getdiastolic)
            vo2_max = float(getvo2)
            hrv = int(gethrv)
            cardiacOutput = float(getcardiac)
            ldlCholesterol = int(getldl)
            hdlCholesterol = int(gethdl)
            triglycerides = int(gettri)
            fastingBloodSugar = int(getfBloodSugar)
            postprandialBloodSugar = int(getpBloodSugar)
        except ValueError as e:
            # Handle invalid input (non-integer or non-float)
            context['error'] = f"Invalid input: {str(e)}"
            return render(request, 'html/cardio.html', context)

        # Save the CardioData object
        save_data = CardioData(
            resting_heart_rate=resting_heart_rate, age=age, gender=getgender, max_heart_rate=max_heart_rate,
            systolic=systolic, diastolic=diastolic, vo2_max=vo2_max, hrv=hrv, recovery_time=getrecovery,
            cardiacOutput=cardiacOutput, ldlCholesterol=ldlCholesterol, hdlCholesterol=hdlCholesterol,
            triglycerides=triglycerides, fastingBloodSugar=fastingBloodSugar, postprandialBloodSugar=postprandialBloodSugar,
            bloodSugarIssues=getblood_sugar_condition, familyHistory=getfamilyHistory, cardiacEvents=cardiac_events
        )
        save_data.save()
        context['success'] = "Cardio data saved successfully!"

    # If cardio data is needed for some further logic or report generation, fetch it safely
    cardio_data = CardioData.objects.last()  # Example of fetching last saved cardio data (adjust if necessary)
    
    if cardio_data is None:
        context['error'] = "No cardio data found."
    else:
        # Use cardio_data safely here
        try:
            rhr_category = rhr(cardio_data.resting_heart_rate)  # Assuming 'rhr' is a function that categorizes resting heart rate
            context['rhr_category'] = rhr_category
        except AttributeError:
            context['error'] = "Error processing cardio data."

    return render(request, 'html/cardio.html', context)




# calculating the values
def rhr(resting_heart_rate):
    try:
        rhr_value = int(resting_heart_rate)
    except ValueError:
        return {"category": "Invalid", "review": "Invalid RHR value"}

    if 40 <= rhr_value <= 60:
        return {"category": "Athlete Level", "review": "Low (Optimal for athletes)"}
    elif 60 < rhr_value <= 100:
        return {"category": "Normal", "review": "Normal"}
    elif rhr_value > 100:
        return {"category": "Elevated", "review": "High (Requires attention)"}
    return {"category": "Unknown", "review": "Out of range"}

def hrv(hrv):
    try:
        hrv_value = int(hrv)
    except ValueError:
        return "Invalid HRV value"

    if hrv_value > 80:
        return "High (Excellent Recovery)"
    elif 60 <= hrv_value <= 80:
        return "Normal (Good Recovery)"
    elif 40 <= hrv_value <= 59:
        return "Low (Moderate Stress/Recovery)"
    elif hrv_value < 40:
        return "Low (Poor Recovery)"
    return "Out of range"

def cardiac_output(cardiac_output):
    try:
        co_value = float(cardiac_output)
    except ValueError:
        return "Invalid Cardiac Output value"

    if co_value > 7.0:
        return "High (Excellent)"
    elif 4.0 <= co_value <= 6.9:
        return "Normal"
    else:
        return "Low (Requires attention)"

def blood_sugar(fasting_blood_sugar):
    try:
        sugar_value = int(fasting_blood_sugar)
    except ValueError:
        return "Invalid Blood Sugar value"

    if 70 <= sugar_value <= 99:
        return "Normal"
    elif 100 <= sugar_value <= 125:
        return "Prediabetes (High)"
    elif sugar_value >= 126:
        return "Diabetes (High)"
    return "Out of range"

def family_history(family_history):
    if family_history == 'No Known Family History':
        return "No Significant Risk"
    elif family_history == 'Single Case in Family':
        return "Slightly Increased Risk"
    elif family_history == 'Multiple Cases in Family':
        return "Increased Risk"
    return "Out of range"

def mhr(age, max_heart_rate):
    try:
        mhr_value = int(max_heart_rate)
    except ValueError:
        return "Invalid MHR value"

    if 20 <= age <= 29:
        if 191 <= mhr_value <= 200:
            return "Normal"
        elif mhr_value < 191:
            return "Low (Below Expected)"
        else:
            return "High"
    elif 30 <= age <= 39:
        if 181 <= mhr_value <= 190:
            return "Normal"
        elif mhr_value < 181:
            return "Low (Below Expected)"
        else:
            return "High"
    elif 40 <= age <= 49:
        if 171 <= mhr_value <= 180:
            return "Normal"
        elif mhr_value < 171:
            return "Low (Below Expected)"
        else:
            return "High"
    return "Age out of range for MHR"



def blood_pressure(systolic, diastolic):
    try:
        sys = int(systolic)
        dia = int(diastolic)
    except ValueError:
        return "Invalid Blood Pressure values"

    if sys < 120 and dia < 80:
        return "Normal"
    elif 120 <= sys <= 129 and dia < 80:
        return "Elevated (Requires attention)"
    elif 130 <= sys <= 139 or 80 <= dia <= 89:
        return "High (Hypertension Stage 1)"
    elif sys >= 140 or dia >= 90:
        return "High (Hypertension Stage 2)"
    return "Out of range"



def vo2_max(vo2_max, gender):
    try:
        vo2_value = float(vo2_max)
    except ValueError:
        return "Invalid VO2 Max value"

    if gender == 'male':
        if vo2_value >= 60:
            return "High (Elite Athlete)"
        elif 50 <= vo2_value < 60:
            return "Very Good"
        elif 40 <= vo2_value < 50:
            return "Good"
        elif 30 <= vo2_value < 40:
            return "Average"
        else:
            return "Low (Poor)"
    elif gender == 'female':
        if vo2_value >= 55:
            return "High (Elite Athlete)"
        elif 45 <= vo2_value < 55:
            return "Very Good"
        elif 35 <= vo2_value < 45:
            return "Good"
        elif 25 <= vo2_value < 35:
            return "Average"
        else:
            return "Low (Poor)"
    return "Invalid gender"


def cholesterol(ldl, hdl, triglycerides):
    try:
        ldl_value = int(ldl)
        hdl_value = int(hdl)
        triglycerides_value = int(triglycerides)
    except ValueError:
        return "Invalid Cholesterol values"

    if ldl_value < 100 and hdl_value >= 60 and triglycerides_value < 150:
        return "Normal"
    elif 100 <= ldl_value <= 129 and 40 <= hdl_value < 60 and 150 <= triglycerides_value < 199:
        return "Slightly Elevated"
    elif 130 <= ldl_value <= 159 or 200 <= triglycerides_value < 499:
        return "High (Requires attention)"
    elif ldl_value >= 160 or triglycerides_value >= 500:
        return "Critical (Requires immediate attention)"
    return "Out of range"

def heart_health_score(resting_heart_rate, systolic, diastolic, ldl, hdl):
    try:
        # Convert inputs to integers
        rhr = int(resting_heart_rate)
        systolic_bp = int(systolic)
        diastolic_bp = int(diastolic)
        hdl_cholesterol = int(hdl)
        ldl_cholesterol = int(ldl)
    except ValueError:
        return "Invalid input values"

    # Validate ranges for heart health parameters
    if not (0 <= rhr <= 200):
        return "Resting heart rate out of range", None
    if not (50 <= systolic_bp <= 200) or not (30 <= diastolic_bp <= 120):
        return "Blood pressure values out of range", None
    if not (0 <= hdl_cholesterol <= 100) or not (0 <= ldl_cholesterol <= 300):
        return "Cholesterol values out of range", None

    # Calculate heart health score
    heart_health_score = (100 - rhr) + (120 / systolic_bp + 80 / diastolic_bp) * 10 + (hdl_cholesterol / ldl_cholesterol) * 10
    heart_health_score = min(max(heart_health_score, 0), 100)  # Cap between 0 and 100

    # Determine heart health level based on the score
    if heart_health_score >= 90:
        level = "Excellent Heart Health"
    elif 70 <= heart_health_score < 90:
        level = "Good Heart Health"
    elif 50 <= heart_health_score < 70:
        level = "Fair Heart Health"
    elif 30 <= heart_health_score < 50:
        level = "Poor Heart Health"
    else:
        level = "Very Poor Heart Health"

    # Return formatted string with both score and health level
    return f"Your Heart Health Score: {heart_health_score} | review: {level}"


def fitness_score(vo2_max, recovery_time, hrv):
    try:
        # Convert inputs to float
        vo2 = float(vo2_max)
        recovery = float(recovery_time)
        heart_rate_variability = float(hrv)
    except ValueError:
        return "Invalid input values"

    # Validate ranges for fitness parameters
    if vo2 <= 0:
        return "VO2 Max must be greater than zero"
    if recovery <= 0:
        return "Recovery time must be greater than zero"
    if heart_rate_variability < 0:
        return "HRV cannot be negative"

    # Calculate fitness score
    fitness_score = (vo2 / 50) * 50 + (100 / recovery) * 30 + (heart_rate_variability / 50) * 20
    fitness_score = min(max(fitness_score, 0), 100)  # Cap between 0 and 100

    # Determine fitness level based on the score
    if fitness_score >= 90:
        level = "Excellent Fitness Level"
    elif 70 <= fitness_score < 90:
        level = "Good Fitness Level"
    elif 50 <= fitness_score < 70:
        level = "Average Fitness Level"
    elif 30 <= fitness_score < 50:
        level = "Below Average Fitness Level"
    else:
        level = "Poor Fitness Level"

    # Return formatted string with both score and fitness level
    return f"Your Fitness Score: {fitness_score} | review: {level}"



def cardiovascular_risk_score(ldl_cholesterol, hdl_cholesterol, fasting_blood_sugar):
    try:
        ldl = float(ldl_cholesterol)
        hdl = float(hdl_cholesterol)
        fasting_sugar = float(fasting_blood_sugar)

        # Validate input values
        if ldl <= 0 or hdl <= 0:
            return "Cholesterol values must be greater than zero", None
        if fasting_sugar < 0:
            return "Fasting blood sugar cannot be negative", None


        # Calculate risk factors
        cholesterol_ratio = ldl / hdl if hdl != 0 else 0
        risk_factors = cholesterol_ratio + (fasting_sugar / 100)
        cardiovascular_risk_score = 100 - risk_factors * 10
        cardiovascular_risk_score = max(min(cardiovascular_risk_score, 100), 0)  # Cap between 0 and 100

        # Determine risk level based on the score
        if cardiovascular_risk_score >= 90:
            risk_level = "Low Risk"
        elif 70 <= cardiovascular_risk_score < 90:
            risk_level = "Moderate Risk"
        elif 50 <= cardiovascular_risk_score < 70:
            risk_level = "High Risk"
        else:
            risk_level = "Very High Risk"

        # Return formatted string with both score and risk level
        return f"Your Score: {cardiovascular_risk_score} | review: {risk_level}"

    except ValueError:
        return "Invalid input values, unable to calculate score"





def metrics(request):
    if request.method == 'POST':
        existing_medical_conditions = request.POST.get('existing_medical_conditions', '')
        medical_conditions = request.POST.get('medical_conditions', '')
        gettraining_intensity = request.POST.get('training_intensity', '')
        getendurance_results = request.POST.get('endurance_results', '')
        getsleep_patterns = request.POST.get('sleep_patterns', '')
        gettraining_regimen = request.POST.get('training_regimen', '')
        getinjury_during_training = request.POST.get('injury_during_training', '')
        getinjury_description = request.POST.get('injury_description', '')
        saves_data = Metric(existing_medical_conditions=existing_medical_conditions, medical_conditions=medical_conditions,
                            training_intensity=gettraining_intensity, endurance_results=getendurance_results,
                            sleep_patterns=getsleep_patterns, training_regimen=gettraining_regimen,
                            injury_during_training=getinjury_during_training, injury_description=getinjury_description)
        saves_data.save()
    return render(request, 'html/performance_metrics.html')





def report(request, username=None):
    if username:
        # Fetch data for a specific user by username
        registered_user = get_object_or_404(Register, username=username)
        personal_info = get_object_or_404(PersonalInfo, name=registered_user.name)
        
        # Check if the user has cardio data
        try:
            cardio_data = CardioData.objects.get(id=registered_user.id)
        except CardioData.DoesNotExist:
            cardio_data = None  # If no cardio data exists, set it to None

        metrics_data = get_object_or_404(Metric, id=registered_user.id)
    else:
        # Fetch the most recent data as a fallback
        registered_user = Register.objects.last()
        personal_info = PersonalInfo.objects.last()
        
        try:
            cardio_data = CardioData.objects.last()
        except CardioData.DoesNotExist:
            cardio_data = None  # If no cardio data exists, set it to None

        metrics_data = Metric.objects.last()
        
        current_datetime = datetime.now()
        date_only = current_datetime.strftime("%d-%m-%Y")

        if cardio_data:
            rhr_category = rhr(cardio_data.resting_heart_rate)
            mhr_category = mhr(int(cardio_data.age), int(cardio_data.max_heart_rate))
            blood_category = blood_pressure(int(cardio_data.systolic), int(cardio_data.diastolic))
            vo2_max_category = vo2_max(int(cardio_data.vo2_max), str(cardio_data.gender))
            hrv_category = hrv(cardio_data.hrv)
            cardiac_output_category = cardiac_output(cardio_data.cardiacOutput)
            cholesterol_category = cholesterol(int(cardio_data.ldlCholesterol), int(cardio_data.hdlCholesterol),
                                               int(cardio_data.triglycerides))
            blood_sugar_category = blood_sugar(cardio_data.fastingBloodSugar)
            family_history_category = family_history(cardio_data.familyHistory)
            health_score = heart_health_score(cardio_data.resting_heart_rate, cardio_data.systolic,
                                              cardio_data.diastolic, cardio_data.ldlCholesterol, cardio_data.hdlCholesterol)

            fitness = fitness_score(int(cardio_data.vo2_max), int(cardio_data.recovery_time), int(cardio_data.hrv))
            cardisovascular_risk = cardiovascular_risk_score(cardio_data.ldlCholesterol,
                                                            cardio_data.hdlCholesterol, cardio_data.fastingBloodSugar)
        else:
            # If no cardio data, set default or handle appropriately
            rhr_category = mhr_category = blood_category = vo2_max_category = hrv_category = None
            cardiac_output_category = cholesterol_category = blood_sugar_category = family_history_category = None
            health_score = fitness = cardiovascular_risk = None

        date = date_only

    context = {
        'registered_user': registered_user,
        'personal_info': personal_info,
        'cardio_data': cardio_data,
        'metrics_data': metrics_data,
        'rhr_category': rhr_category,
        'hrv_category': hrv_category,
        'cardiac_output_category': cardiac_output_category,
        'blood_sugar_category': blood_sugar_category,
        'family_history_category': family_history_category,
        'mhr_category': mhr_category,
        'blood_category': blood_category,
        'vo2_max_category': vo2_max_category,
        'cholesterol_category': cholesterol_category,
        'health_score': health_score,
        'fitness': fitness,
        'cardiovascular_risk': cardiovascular_risk,
        'date': date,
    }

    return render(request, 'html/report.html', context)

def training_plan(request):
    return render(request,'html/training_plans.html')

def tips(request):
    return render(request,'html/Tips_resources.html')


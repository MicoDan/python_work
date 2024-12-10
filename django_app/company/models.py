from django.db import models

class ContactDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    Status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class PersonalInfo(models.Model):
    name = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    level_choices = [
        ('recreational', 'Recreational'),
        ('amateur', 'Amateur'),
        ('semi-professional', 'Semi-Professional'),
        ('professional', 'Professional'),
        ('elite-international', 'Elite/International')
    ]
    competition_level = models.CharField(
        max_length=50,
        choices=level_choices,
        default='amateur'
    )
    training_choices = [
        ('low', 'Low: 1-3 hours per week'),
        ('moderate', 'Moderate: 4-7 hours per week'),
        ('high', 'High: 8-12 hours per week'),
        ('very-high', 'Very High: 13-20 hours per week'),
        ('elite', 'Elite: 21+ hours per week')
    ]
    training_frequency = models.CharField(
        max_length=50,
        choices=training_choices,
        default='moderate'
    )

class CardioData(models.Model):
    age = models.CharField(max_length=30,null=True)
    resting_heart_rate = models.CharField(max_length=30)
    max_heart_rate = models.CharField(max_length=30)
    diastolic = models.CharField(max_length=30)
    systolic = models.CharField(max_length=30,default=0)
    vo2_max = models.CharField(max_length=30)
    hrv = models.CharField(max_length=30)
    recovery_time = models.CharField(max_length=30)
    cardiacOutput = models.CharField(max_length=30)
    ldlCholesterol = models.CharField(max_length=30)
    hdlCholesterol = models.CharField(max_length=30)
    triglycerides = models.CharField(max_length=30)
    fastingBloodSugar = models.CharField(max_length=30)
    postprandialBloodSugar = models.CharField(max_length=30)
    familyHistory = models.CharField(max_length=30)
    cardiacEvents = models.CharField(max_length=30)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='other',
    )
    BLOOD_SUGAR_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    bloodSugarIssues = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=BLOOD_SUGAR_CHOICES,
        default='no',
    )
    blood_sugar_condition = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Specify the condition if blood sugar issues are present."
    )
    FAMILY_HISTORY_CHOICES = [
        ('No Known Family History', 'No Known Family History'),
        ('Single Case in Family', 'Single Case in Family'),
        ('Multiple Cases in Family', 'Multiple Cases in Family'),
        ('Early Onset Cardiovascular Disease', 'Early Onset Cardiovascular Disease'),
        ('Genetic Cardiovascular Disorders', 'Genetic Cardiovascular Disorders'),
    ]
    family_history = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=FAMILY_HISTORY_CHOICES,
        default='No Known Family History',
    )
    CARDIAC_EVENT_CHOICES = [
        ('Arrhythmias', 'Arrhythmias'),
        ('Myocardial Infarction (Heart Attack)', 'Myocardial Infarction (Heart Attack)'),
        ('Angina Pectoris', 'Angina Pectoris'),
        ('No Events', 'No Events'),
        ('Congestive Heart Failure (CHF)', 'Congestive Heart Failure (CHF)'),
        ('Stroke', 'Stroke'),
        ('Coronary Artery Disease (CAD)', 'Coronary Artery Disease (CAD)'),
        ('Cardiomyopathy', 'Cardiomyopathy'),
    ]
    cardiac_events = models.CharField(
        max_length=255,
        choices=CARDIAC_EVENT_CHOICES,
        blank=True,
        null=True,
        default='No Events',
        help_text="Select any previous cardiac events you have experienced."
    )

class Metric(models.Model):
    EXISTING_MEDICAL_CONDITION_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    existing_medical_conditions = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=EXISTING_MEDICAL_CONDITION_CHOICES,
        default='No',
        help_text="Do you have any existing medical conditions?"
    )
    medical_conditions = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    TRAINING_INTENSITY_CHOICES = [
        ('High', 'High'),
        ('Moderate', 'Moderate'),
        ('Low', 'Low'),
    ]
    training_intensity = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=TRAINING_INTENSITY_CHOICES,
        default='Moderate',
        help_text="How would you describe your training intensity levels?"
    )
    endurance_results = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    SLEEP_PATTERNS_CHOICES = [
        ('Less than 4 hours', 'Less than 4 hours'),
        ('4-6 hours', '4-6 hours'),
        ('6-8 hours', '6-8 hours'),
        ('More than 8 hours', 'More than 8 hours'),
    ]
    sleep_patterns = models.CharField(
        max_length=20,
        choices=SLEEP_PATTERNS_CHOICES,
        blank=True,
        null=True,
        default='6-8 hours',
        help_text="How many hours do you sleep on average per night?"
    )
    training_regimen = models.CharField(
        max_length=400,
        blank=True,
        null=True,
    )
    injury_during_training = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        default='No',
        help_text="Have you experienced any injuries during competition or training?"
    )
    injury_description = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Please describe the type, severity, and treatment of your injury."
    )



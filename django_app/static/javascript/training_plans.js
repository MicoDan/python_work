function showTraining() {
            const category = document.getElementById('sport-category').value;
            const output = document.getElementById('training-output');

            let training = '';

            switch(category) {
                case 'sprints':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week focusing on sprint drills and lower-body strength training. Alternate between 60m and 100m sprints, working on acceleration and maintaining top speed. Strength training includes squats, lunges, and deadlifts. Include 15-20 minutes of mobility work post-sprints to prevent injury. Rest days will be for recovery or light jogging.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4 days a week incorporating sprint intervals, strength training, and flexibility work. Alternate between high-intensity intervals and technical drills focusing on sprint mechanics. Include exercises for speed, power, and flexibility.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with high-intensity sprints, plyometrics, strength work, and technical sprint mechanics. Emphasize explosive power, speed endurance, and proper sprinting form. Include recovery strategies to manage fatigue.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week with short-distance sprints (20m-40m) combined with light weight training. Focus on developing proper sprinting technique and foundational strength. Gradually increase distance and intensity as proficiency improves.`;
                    break;
                case 'long-jump':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week focusing on jumping technique, plyometric drills, and lower-body strength work. Perform technique drills, plyometric exercises, and strength training for legs.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4-5 days a week with a focus on jump mechanics, sprint speed, and flexibility. Incorporate advanced jump drills and strength training to improve jump distance and technique.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with advanced plyometric, sprint, and jump drills. Emphasize technique refinement and explosive power development. Include flexibility and recovery work to support high-intensity training.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week with run-ups and basic jumps to develop proper technique and timing. Focus on learning the fundamentals of jumping and gradually increase intensity.`;
                    break;
                case 'relay-races':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week with baton-passing drills and sprint intervals. Focus on improving baton exchanges and sprint endurance through drills and practice.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4 days a week focusing on teamwork, passing skills, and sprint endurance. Emphasize smooth baton transitions, team coordination, and endurance workouts.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with teamwork drills, speed work, and technical baton exchanges. Incorporate high-intensity intervals, teamwork exercises, and recovery strategies.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week with team drills and short sprint intervals (50m-100m). Focus on basic baton passing and running technique.`;
                    break;
                case 'javelin':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week focusing on arm strength, throwing technique, and flexibility. Include drills for improving throwing form and exercises for upper-body strength.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4-5 days a week emphasizing shoulder mobility, power, and run-up speed. Incorporate advanced throwing drills, strength training, and flexibility exercises.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week focusing on technique, explosive strength training, and recovery work. Include high-intensity throwing sessions and detailed technique refinement.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week focusing on basic throws and light weight training. Develop foundational throwing skills and strength through basic drills and exercises.`;
                    break;
                case 'hammer-throw':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week with basic throws and strength training. Focus on form and strength exercises for the core and upper body.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4-5 days a week with increased focus on spinning techniques and power development. Incorporate rotational drills, strength training, and flexibility work.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with technical drills, core strength, and flexibility training. Emphasize advanced spinning techniques, explosive power, and recovery strategies.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week with footwork drills and light throws. Focus on learning basic mechanics and building initial strength.`;
                    break;
                case 'discus':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week working on form and basic strength training. Focus on discus technique, strength exercises, and flexibility.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4 days a week focusing on spin technique and upper-body conditioning. Emphasize technique drills, strength training, and flexibility.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with advanced discus drills, strength, and power exercises. Include high-intensity technique work and recovery strategies.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week focusing on grip and stance with light throws. Develop fundamental discus skills and basic strength.`;
                    break;
                case 'marathon':
                    training = `<span class="average-heading">Average Plan</span> Train 4 days a week of long-distance runs, alternating between slow and moderate pace. Focus on gradually increasing distance and maintaining steady pace.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 5 days a week with endurance, tempo, and long-run training. Include varied pace workouts and longer distances to build stamina.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week including interval, speed, long-run, and recovery training. Focus on comprehensive marathon preparation with a mix of high-intensity and endurance workouts.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 3 days a week with steady-state runs building up distance gradually (5-10km). Focus on developing endurance and gradually increasing run distances.`;
                    break;
                case 'shot-put':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week of throwing and strength work. Focus on shot-put technique and strength exercises for the upper body.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4 days a week focusing on technique and arm power. Include advanced strength training and shot-put drills.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with weight training, plyometrics, and advanced throws. Emphasize power development and technical refinement.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week with light weight practice and arm/shoulder strength. Develop basic shot-put skills and strength.`;
                    break;
                case 'high-jump':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week focusing on technique, jumping drills, and plyometrics. Incorporate vertical jump exercises and technique drills.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4-5 days a week working on jump height, approach speed, and flexibility. Include advanced jumping drills, speed work, and flexibility exercises.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with advanced jump drills, speed, and strength training. Focus on technique refinement, explosive power, and recovery.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week with basic jumps and flexibility drills. Focus on learning proper jumping technique and increasing flexibility.`;
                    break;
                case 'swimming':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week of endurance swimming and technique refinement. Focus on maintaining a steady pace and improving swimming form.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4-5 days a week focusing on stroke efficiency, speed, and endurance. Incorporate interval training and technique drills to enhance performance.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week with swim drills, speed intervals, and strength work. Emphasize technique refinement, endurance, and high-intensity workouts.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week of basic stroke work and breathing techniques. Focus on developing foundational swimming skills and breathing patterns.`;
                    break;
                case 'archery':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week with target practice and strength training. Focus on improving shooting accuracy and developing strength.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4-5 days a week focusing on precision, posture, and mental focus. Include advanced shooting drills and mental training techniques.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week of shooting practice, strength, and stability training. Emphasize technique refinement, physical conditioning, and mental preparation.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week of basic bow handling and shooting form. Develop fundamental archery skills and proper technique.`;
                    break;
                case 'cycling':
                    training = `<span class="average-heading">Average Plan</span> Train 3 days a week of endurance and moderate-speed rides. Focus on building stamina and maintaining a steady pace.\n\n` +
                               `<span class="normal-heading">Normal Plan</span> Train 4-5 days a week alternating between long rides, speed, and strength. Incorporate interval training and varied distance rides.\n\n` +
                               `<span class="fulltime-heading">Full-Time Plan</span> Train 6 days a week including interval training, endurance, and sprints. Focus on comprehensive cycling conditioning and high-intensity workouts.\n\n` +
                               `<span class="beginner-heading">Beginner Plan</span> Train 2 days a week of steady, short rides building up to higher distances. Focus on developing basic cycling endurance and technique.`;
                    break;
                default:
                    training = 'Please select a sport to see the training plan.';
            }

            output.innerHTML = training;
            output.style.display = 'block';
        }


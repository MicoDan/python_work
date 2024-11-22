# Generated by Django 4.2.15 on 2024-09-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0005_personal_info_alter_register_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="personal_info",
            name="competition_level",
            field=models.CharField(
                choices=[
                    (
                        "recreational",
                        "Recreational (Casual, non-competitive participation)",
                    ),
                    (
                        "amateur",
                        "Amateur (Local clubs, school teams, regional leagues)",
                    ),
                    (
                        "semi-professional",
                        "Semi-Professional (High-level amateur competition, minor leagues)",
                    ),
                    (
                        "professional",
                        "Professional (National and international competitions, professional leagues)",
                    ),
                    (
                        "elite-international",
                        "Elite/International (Olympic level, World Championships)",
                    ),
                ],
                default="amateur",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="personal_info",
            name="training_frequency",
            field=models.CharField(
                choices=[
                    ("low", "Low: 1-3 hours per week (Light training)"),
                    ("moderate", "Moderate: 4-7 hours per week (Regular training)"),
                    ("high", "High: 8-12 hours per week (Intensive training)"),
                    (
                        "very-high",
                        "Very High: 13-20 hours per week (Advanced training)",
                    ),
                    (
                        "elite",
                        "Elite: 21+ hours per week (Professional/elite training)",
                    ),
                ],
                default="moderate",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="personal_info",
            name="sports",
            field=models.CharField(
                choices=[
                    ("Sprints", "Long jump"),
                    ("javelin", "Discus"),
                    ("Swimming", "Shot Put"),
                    ("Cycling", "High jump"),
                    ("Mixed Martial Arts", "Archery"),
                ],
                default="Sprints",
                max_length=200,
            ),
        ),
    ]
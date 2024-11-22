# Generated by Django 4.2.15 on 2024-09-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0016_rename_age_personalinfo_dob"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cardiodata", old_name="blood_pressure", new_name="diastolic",
        ),
        migrations.AddField(
            model_name="cardiodata",
            name="systolic",
            field=models.CharField(default=0, max_length=30),
        ),
    ]
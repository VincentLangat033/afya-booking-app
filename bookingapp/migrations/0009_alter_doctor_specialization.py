# Generated by Django 4.1.3 on 2022-11-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0008_doctor_county_doctor_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Emergency Specialist', 'Emergency Specialist'), ('Allergy Specialist', 'Allergy Specialist'), ('Anesthesiologist', 'Anesthesiologist'), ('COlon and Rectal Surgeon', 'COlon and Rectal Surgeon'), ('Consultant', 'Consultant')], max_length=50, null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baby_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('clinical_staff', models.CharField(choices=[('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Dietitian', 'Dietitian'), ('Pharmacist', 'Pharmacist'), ('Healthcare Assistant', 'Healthcare Assistant')], default='Doctor', max_length=50)),
                ('guardian_name', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
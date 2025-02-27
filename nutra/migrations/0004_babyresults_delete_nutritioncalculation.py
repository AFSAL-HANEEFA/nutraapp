# Generated by Django 5.1.3 on 2024-12-03 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutra', '0003_nutritioncalculation_delete_admission'),
    ]

    operations = [
        migrations.CreateModel(
            name='BabyResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('age_in_days', models.IntegerField()),
                ('age_in_weeks', models.IntegerField()),
                ('age_in_months', models.IntegerField()),
                ('corrected_gestational_age', models.DecimalField(decimal_places=1, max_digits=5)),
                ('tpn_total_volume_ml', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tpn_calories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lipids_grams', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lipids_calories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maintenance_fluid_type', models.CharField(max_length=50)),
                ('maintenance_total_volume_ml', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maintenance_calories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('enteral_feed_type', models.CharField(blank=True, max_length=50, null=True)),
                ('feed_amount_ml', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('feed_calories', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_fluid_intake_ml', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_calorie_intake', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='nutra.baby_admission')),
            ],
        ),
        migrations.DeleteModel(
            name='NutritionCalculation',
        ),
    ]

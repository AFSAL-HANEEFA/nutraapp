from django.contrib import admin


from .models import baby_Admission,BabyResults





@admin.register(baby_Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('serial_no', 'first_name', 'surname', 'hosp_number', 'dob', 'gestational_age', 'birth_weight')
    search_fields = ('first_name', 'surname', 'hosp_number')




@admin.register(BabyResults)
class BabyResultsAdmin(admin.ModelAdmin):
    list_display = ('baby', 'date', 'total_fluid_intake_ml', 'total_calorie_intake', 'created_at')


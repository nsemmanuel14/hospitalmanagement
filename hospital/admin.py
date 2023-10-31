from django.contrib import admin
from .models import *
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)


class ConsultationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consultation, ConsultationAdmin)

class ExamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Exam, ExamAdmin)

class ExamTestOrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExamTestOrder, ExamTestOrderAdmin)

class MedicationCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(MedicationCategory, MedicationCategoryAdmin)

class MedicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Medication, MedicationAdmin)

class PrescriptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Prescription, PrescriptionAdmin)

class InsuranceCompanyAdmin(admin.ModelAdmin):
    pass
admin.site.register(InsuranceCompany, InsuranceCompanyAdmin)

class PatientsInsuranceAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientsInsurance, PatientsInsuranceAdmin)



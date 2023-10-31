from django.db import models
from django.contrib.auth.models import User


departments=[
('Cardiology','Cardiology'),
('Dermatology','Dermatology'),
('Oncology','Oncology'),
('Neurology','Neurology'),
('Orthopedics','Orthopedics'),
('Dermatology','Dermatology'),
('Pediatrics','Pediatrics'),
('Gynecology','Gynecology'), 
('Urology','Urology'),
('Ophthalmology','Ophthalmology'),
('Internal Medicine','Internal Medicine'),
('Radiology','Radiology'),
('Anesthesiology','Anesthesiology'),
('Emergency Medicine','Emergency Medicine'),
('General Surgery','General Surgery')

]


specialties=[
('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Oncologist','Oncologist'),
('Neurologist','Neurologist'),
('Orthopedicsist','Orthopedicsist'),
('Dermatologist','Dermatologist'),
('Pediatrist','Pediatrist'),
('Gynecologist','Gynecologist'), 
('Urologist','Urologist'),
('Ophthalmologist','Ophthalmologist'),
('Internist','Internist'),
('Radiologist','Radiologist'),
('Anesthesiologist','Anesthesiologist'),
('General Surgery','General Surgery')

]

gender_choices = [
    ("Male", "Male"),
    ("Female", "Female"),
    ]

marital_statuses = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced')
    ]
work_statuses = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,null=False,default='Cardiology')
    specialty= models.CharField(max_length=50,choices=specialties,null=False,default='Cardiologist')
    gender = models.CharField(max_length=6, choices=gender_choices, null=False, blank=False,default='Male')
    marital_status = models.CharField(max_length=10, choices=marital_statuses, null=False, blank=False,default='Single')
    email = models.EmailField(unique=True,null=True, blank=True,)
    date_registered = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    work_status = models.CharField(max_length=10, choices=work_statuses, null=False, blank=False,default='Active')
    nid_number = models.CharField(max_length=16,unique=True, null=False, blank=False)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=13,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    nid_number = models.CharField(max_length=16,unique=True, null=False, blank=False)
    date_of_birth=models.DateField(auto_now=False)
    gender = models.CharField(max_length=6, choices=gender_choices, null=False, blank=False,default='Male')
    marital_status = models.CharField(max_length=10, choices=marital_statuses, null=False, blank=False,default='Single')
    email = models.EmailField(unique=True,null=True, blank=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=False)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    
class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)
    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)
    
    
class Consultation(models.Model):
    consultation_id = models.AutoField(primary_key=True)  # AutoField is used for serial
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    consultation_date = models.DateField(auto_now=True)
    complain = models.TextField(null=False, blank=False)
    diagnosis_note = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return f"Consultation {self.consultation_id} - Patient: {self.patient}, Doctor: {self.doctor}, Date: {self.consultation_date}"

class Exam(models.Model):
    exam_id = models.CharField(max_length=5, primary_key=True)
    exam_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"Exam {self.exam_id} - Name: {self.exam_name}"
    
class ExamTestOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)
    exams_result = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Exam Test Order {self.order_id} - Exam: {self.exam.exam_name}, Consultation: {self.consultation}"


class MedicationCategory(models.Model):
    category_id = models.CharField(primary_key=True, max_length=5)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.medication_name

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    prescription_note = models.TextField()
    prescription_date = models.DateField(auto_now=True)
    consomation_condition = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prescription {self.prescription_id}"



class InsuranceCompany(models.Model):
    insurance_id = models.CharField(primary_key=True, max_length=10)
    insurance_name = models.CharField(max_length=255)

    def __str__(self):
        return self.insurance_name


class PatientsInsurance(models.Model):
    patient_insurance_id = models.CharField(primary_key=True, max_length=10)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    insurance = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    patient_percentage = models.IntegerField()
    insurance_percentage = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Insurance for {self.patient} - {self.insurance}"






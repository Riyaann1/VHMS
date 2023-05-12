from django.contrib import admin
from .models import AnimalOwner,Animal,HospitalStaff,Doctors,Medicines,AnimalTreatment,MedicinePurchase,Bills,Admission

# Register your models here.
admin.site.register(AnimalOwner)
admin.site.register(Animal)
admin.site.register(HospitalStaff)
admin.site.register(Doctors)
admin.site.register(Medicines)
admin.site.register(AnimalTreatment)
admin.site.register(MedicinePurchase)
admin.site.register(Admission)
admin.site.register(Bills)
from django.db import models

# Create your models here.
# AnimalOwner(id, name, house, street, locality, city, pin, phone, email, )
# Animal(id, animal,insurence_id, specie, family,ownerid, colour, name_if_any, age, gender, note )
# HospitalStaff(id, name, designation, house, street, locality, city, pin, phone, email  )
# Doctors(id, name, designation, house, street, locality, city, pin, phone, email)
# Medicines(id, medicine, cost_price, sale_price, quantity_in_stock, make,  )
# AnimalTreatment(adm_id, doctorid,medicineid, dosage, date, note, billamount )
# MedicinePurchase(tid, medicineid, supplier, date, quantity, )
# Admission(adm_id,animal_id,date,discharge_date,)

class AnimalOwner(models.Model):
	fname=models.CharField(max_length=50)
	pssd=models.CharField(max_length=8)
	lname=models.CharField(max_length=50)
	house=models.CharField(max_length=30)
	street=models.CharField(max_length=30)
	locality=models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	pin=models.IntegerField(max_length=3)
	phone=models.CharField(max_length=40)
	email=models.EmailField(max_length=100)
	age=models.IntegerField(max_length=2)
	def __str__(self):
		return self.fname + ' '+ self.lname

#FileField

class Animal(models.Model):
	animal=models.CharField(max_length=100)
	insurence_id=models.CharField(max_length=30)
	species=models.CharField(max_length=30)
	family=models.CharField(max_length=30)
	owner_id = models.ForeignKey(AnimalOwner,verbose_name='Owner_ID', on_delete=models.CASCADE)      
	colour=models.CharField(max_length=30)
	name_if_any=models.CharField(max_length=30)
	age=models.IntegerField()
	gender=(('M','Male'),('F','Female'))
	note=models.CharField(max_length=100)
	def __str__(self):
		st = "%-30s %-5d %-3s %s %d %s %s %s %s %s "%(self.animal, self.insurence_id,
                                               self.species, self.family, self.owner_id,self.colour,self.name_if_any,self.age,self.gender,self.note)
		return st
	class Meta:
		verbose_name_plural="Animals"



class HospitalStaff(models.Model):
	name=models.CharField(max_length=30)
	designation=models.CharField(max_length=30)
	house=models.CharField(max_length=30)
	street=models.CharField(max_length=30)
	locality=models.CharField(max_length=30)
	pin=models.IntegerField()
	phone=models.CharField(max_length=40)
	email=models.CharField(max_length=100)
	def __str__(self):
		st = "%-30s %-5s %-3s %s %s "%(self.name, self.designation,
                                               self.house, self.street, self.locality,self.pin,self.phone,self.email)
		return st
	class Meta:
		verbose_name_plural="Hospital Staff"



class Doctors(models.Model):
	name=models.CharField(max_length=30)
	designation=models.CharField(max_length=30)
	house=models.CharField(max_length=30)
	street=models.CharField(max_length=30)
	locality=models.CharField(max_length=30)
	pin=models.IntegerField()
	phone=models.CharField(max_length=40)
	email=models.CharField(max_length=100)
	def __str__(self):
		st = "%-30s %-5s %-3s %s %s %s %d %s "%(self.name, self.designation,
                                               self.house, self.street, self.locality,self.pin,self.phone,self.email)
		return st
	class Meta:
		verbose_name_plural="Doctors"



class Medicines(models.Model):
	Medicine=models.CharField(max_length=40)
	cost_price=models.IntegerField(default=0)
	sale_price=models.IntegerField()
	quantity_in_stock=models.IntegerField()
	maker=models.CharField(max_length=30)
	def __str__(self):
		st = "%-30s %-5d %d %d %s "%(self.Medicine ,self.cost_price,
                                               self.sale_price, self.quantity_in_stock, self.maker,)
		return st
	class Meta:
		verbose_name_plural="Medicines"


class AnimalTreatment(models.Model):
	doctorid=models.ForeignKey(Doctors,verbose_name='Doctor_ID', on_delete=models.CASCADE)
	Medicineid=models.ForeignKey(Medicines,verbose_name='Medicine_ID', on_delete=models.CASCADE)
	dosage=models.IntegerField()	
	date=models.IntegerField()	
	note=models.CharField(max_length=10)	
	billamount=models.IntegerField()	
	def __str__(self):
		st = "%-30d %-5d %-3d %d %s %s "%(self.doctorid, self.Medicineid,
                                               self.dosage, self.date, self.note,self.billamount)
		return st
	class Meta:
		verbose_name_plural="Animal Treatment"

class MedicinePurchase(models.Model):
	medicineid=models.ForeignKey(Medicines,verbose_name='Medicine_ID', on_delete=models.CASCADE)      
	supplier=models.CharField(max_length=100)
	date=models.IntegerField()
	quantity=models.IntegerField()
	def __str__(self):
		st = "%-30s %-5s %-3s %s %s "%(self.medicineid, self.designation,
                                               self.house, self.street, self.locality,self.pin,self.phone,self.email)
		return st
	class Meta:
		verbose_name_plural="Hospital Staff"


class Admission(models.Model):
	date=models.IntegerField(default=0)
	discharge_date=models.IntegerField()
	animal_id = models.ForeignKey(Animal,verbose_name='Animal_ID', on_delete=models.CASCADE)
	def __str__(self):
		st = "%-30d %-5d %-3d "%(self.date, self.discharge_date,self.animal_id)
		return st
	class Meta:
		verbose_name_plural="Admission"
 



#bill(tid,amount,billdate)

class Bills(models.Model):
	billdate=models.IntegerField(default=0)
	tid= models.ForeignKey(AnimalTreatment,verbose_name='Treatment_ID', on_delete=models.CASCADE)
	def __str__(self):
		st = "%-30s %-5s  "%(self.billdate, self.tid)
		return st
	class Meta:
		verbose_name_plural="Bills"
  















#  item = models.ForeignKey(KalotsavItems, 
#         	verbose_name='ParticipatingItem', on_delete=models.CASCADE)
#         participant=models.ForeignKey(Participants, on_delete=models.CASCADE, 
# 	verbose_name='Participant')

# class Animal(models.Model):
# 	admno = models.IntegerField(default=0)
# 	owner_name = models.CharField(max_length=30,default='None')
# 	def __str__(self):
# 		st = " %s %s "%(self.admno, self.owner_name)
# 		return st

# class Doctor(models.Model):
# 	name = models.CharField(max_length=40, default='Item')
# 	Dept = models.CharField(max_length=40, default='Item')
# 	GEN=(('B','Boys'), ('G','Girls'), ('C', 'Common'))
# 	CAT=((x,x) for x in(1,2,3,4))
# 	igender = models.CharField(choices=GEN, default='C', max_length=1)
# 	category=models.IntegerField( choices=CAT, default=4)
# 	teamsize=models.IntegerField( default=1),
	
# 	def __str__(self):
# 		st = "{No:%d Item:%-40s Gender:%-3s Cat:%-3d Teamsize:%d}"%( self.itemno, self.item, self.igender, self.category, self.teamsize)
# 		return st




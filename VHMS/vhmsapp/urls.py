
from django.urls import path
from . import views
#from django.conf.urls import  url

urlpatterns = [
   
    path("home.html", views.home),
    path('Appoint.html',views.Appoint,name='AnimalOwner'),
    path('DoctorP.html',views.DoctorP),
    path('UserP.html',views.UserP),
    path('Contact.html',views.Contact),
    path('MedInfo.html',views.MedInfo),
    path('FindDoc.html',views.FindDoc),
    path('signin_form.html',views.signin_form),
    path('A.html',views.A),
    path('B.html',views.B),
    path('C.html',views.C),
    path('AnimalOwner_DB',views.AnimalOwner_DB),
]


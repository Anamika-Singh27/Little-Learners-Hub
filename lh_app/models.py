from django.db import models

# Create your models here.
##feedback model
from django.utils import timezone
class FeedBack(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50)
    remarks = models.TextField(null=True)
    ratings = models.CharField(max_length=2)
    date = models.DateField(default=timezone.now)
    def __str__(self):# to the represent object in the form of string
        return self.name

###contact Mobel
class Contact(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    question=models.TextField()
    date = models.DateField(default=timezone.now)
    def __str__(self):# to the represent object in the form of string
        return self.name

class Event(models.Model):
    event_name=models.CharField(max_length=55,primary_key=True)
    event_venue=models.CharField(max_length=55,default="Auditorium") 
    event_date=models.DateField(default=timezone.now)
    event_description=models.TextField()
    event_pic=models.FileField(max_length=100,upload_to="lh_app/event_images" ,default="")
    def __str__(self):# to the represent object in the form of string
        return self.event_name

class Organization(models.Model):
    org_id=models.CharField(max_length=55,primary_key=True)
    password=models.CharField(max_length=55)
    org_name=models.CharField(max_length=55)
    email=models.EmailField(max_length=55)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=55)
    address=models.CharField(max_length=55)
    owner_name=models.CharField(max_length=55)
    about_org=models.TextField(max_length=55)
    date = models.DateField(default=timezone.now)
    def __str__(self):# to the represent object in the form of string
        return self.org_id

class Parent(models.Model):
    user_id=models.CharField(max_length=55,primary_key=True)
    password=models.CharField(max_length=55)
    org_name=models.CharField(max_length=55)
    email=models.EmailField(max_length=55)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=55)
    address=models.CharField(max_length=55)
    owner_name=models.CharField(max_length=55)
    about_org=models.TextField(max_length=55)
    date = models.DateField(default=timezone.now)
    def __str__(self):# to the represent object in the form of string
        return self.user_id

class Activity(models.Model):
    org_id=models.CharField(max_length=55)
    activity_name=models.CharField(max_length=55)
    charge=models.CharField(max_length=55)
    duration=models.CharField(max_length=55)
    contact=models.CharField(max_length=10)
    date = models.DateField(default=timezone.now)
    def __str__(self):# to the represent object in the form of string
        return self.org_id

class Message(models.Model):
    sender_id=models.CharField(max_length=55)
    receiver_id=models.CharField(max_length=55)
    subject=models.CharField(max_length=55)
    message=models.TextField(max_length=55)
    def __str__(self):# to the represent object in the form of string
        return self.sender_id

class Admission(models.Model):
      activity=models.ForeignKey(Activity,on_delete=models.DO_NOTHING)
      org=models.ForeignKey(Organization,on_delete=models.DO_NOTHING)
      student_name=models.CharField(max_length=55)
      mother_name=models.CharField(max_length=55)
      father_name=models.CharField(max_length=55)
      phone=models.IntegerField(max_length=10)
      alternative_phone=models.IntegerField(max_length=10)
      email=models.EmailField(max_length=55)
      dob=models.CharField(max_length=10)
      age=models.CharField(max_length=3)
      gender=models.CharField(max_length=10)
      school_name=models.CharField(max_length=55)
      admission_mode=models.CharField(max_length=50, blank=True)
      fees=models.CharField(max_length=10)
      payment_screenshot=models.FileField(max_length=100,upload_to="lh_app/payment_images",default="")
      photo=models.FileField(max_length=100,upload_to="lh_app/student_images",default="")
      def __str__(self):# to the represent object in the form of string
        return self.student_name

class OrgQr(models.Model):
      org=models.ForeignKey(Organization,on_delete=models.DO_NOTHING)
      qr_pic=models.FileField(max_length=100,upload_to="lh_app/qr_images" ,default="")
      def __str__(self):# to the represent object in the form of string
        return self.org.org_name

      
      







    



    
    

    





    


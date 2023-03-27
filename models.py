from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class client(User):
    uid = models.AutoField(primary_key=True)
    # firstname = models.CharField(max_length=20,null=False,blank=False)
    # lastname = models.CharField(max_length=20,null=False,blank=False)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    email_id = models.EmailField(null=False,blank=False)

class adventure(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    adv_name = models.CharField(null=False,blank=False,max_length=20)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # capacity = models.IntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()

    def __str__(self):
        return self.adv_name

class schedule(models.Model):
    adv_id = models.ForeignKey(adventure,on_delete=models.CASCADE)
    adv_name = models.CharField(max_length=100,null=False,blank=False)
    sid = models.AutoField(primary_key=True)
    start_hours = models.TimeField(null=False,blank=False)
    end_hours = models.TimeField(null=False,blank=False)
    duration = models.IntegerField(blank=False,null=False)
    capacity = models.IntegerField(blank=False,null=False,default=10)
    schedule_date = models.DateField(default=datetime.now, blank=True)
    #end_date = models.DateTimeField(default=datetime.now, blank=True)

# SERVICE_CHOICES = (
#     ("Skydiving", "SKY"),
#     ("Nursing care", "Nursing care"),
#     ("Medical social services", "Medical social services"),
#     ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
#     )
TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("13 PM", "13 PM"),
    ("14 PM", "14 PM"),
    ("15 PM", "15 AM"),
    ("16 PM", "16 PM"),
    ("17 PM", "17 PM"),
    ("18 PM", "18 PM"),
    ("19 PM", "19 PM"),
    ("20 PM", "20 PM"),
    ("21 PM", "21 PM"),

)

class bookingData(models.Model):
    booking_Id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(client, on_delete=models.CASCADE, null=False, blank=False)
    aid = models.ForeignKey(adventure,on_delete=models.CASCADE,null=False,blank=False)
    People = models.IntegerField(null=False,blank=False);
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="9 AM")
    Comments = models.CharField(max_length=100);
    TotalPrice = models.CharField(max_length=100,default=0);

# class packages(models.Model):
#     id = models.AutoField(primary_key=True, auto_created=True)
#     package_name = models.CharField(null=False, blank=False, max_length=20)
#     package_activities = models.ManyToManyField(adventure,blank=True, related_name='activities')
#     description = models.TextField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     # capacity = models.IntegerField()
#     # min_age = models.IntegerField()
#     # max_age = models.IntegerField()
#
#     # def __str__(self):
#     #     return self.package_activities

class Profile (models. Model):
    user = models. OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def str (self):
        return self.user. username

class packages(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    package_name = models.CharField(null=False, blank=False, max_length=20)
    package_activities = models.ManyToManyField(adventure,blank=True, related_name='activities')
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField(blank=False,null=False,default=0)
    day = models.DateField(default=datetime.now)

    def __str__(self):
        return self.package_name

class packagebookingData(models.Model):
    package_Id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(client, on_delete=models.CASCADE, null=False, blank=False)
    pid = models.ForeignKey(packages, on_delete=models.CASCADE, null=False, blank=False)
    People = models.IntegerField(null=False, blank=False);
    day = models.DateField(default=datetime.now)
    Comments = models.CharField(max_length=100);
    TotalPrice = models.CharField(max_length=100, default=0);


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)  # Unique company ID
    company_name = models.CharField(max_length=191)
    def __str__(self):
        return str(self.company_id)  # Returns company_id
    
class Alumni(models.Model):
    alumni_id = models.CharField(max_length=16, primary_key=True)  # Unique Alumni ID
    password = models.CharField(max_length=191)  
    name = models.CharField(max_length=191)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=191)
    previous_status = models.CharField(max_length=191, blank=True, null=True)
    contact = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=191,unique=True)
    linkedin = models.URLField()
    branch = models.CharField(max_length=100)
    passout_year = models.CharField(max_length=4)
    profile_picture = models.ImageField(upload_to='Docs/', blank=True, null=True)


    def __str__(self):
        return self.alumni_id  # Returns Alumni ID
    
class Student(models.Model):
    student_id = models.CharField(max_length=16, primary_key=True)  # Unique Alumni ID
    password = models.CharField(max_length=191)  
    name = models.CharField(max_length=191, null=True)
    Gender = models.CharField(max_length=100, null=True)
    Birth_date = models.DateField( null=True)
    contact = models.CharField(max_length=10, unique=True, null=True)
    email = models.EmailField(max_length=191,unique=True, null=True)
    branch = models.CharField(max_length=100, null=True)
    sslc_per = models.CharField(max_length=100, null=True)
    passout_year_sslc = models.CharField(max_length=4, null=True)
    hsc_per = models.CharField(max_length=100, null=True)
    passout_year_hsc = models.CharField(max_length=4, null=True)
    skill = models.CharField(max_length=100, null=True)
    profile_picture = models.ImageField(upload_to='Docs/', blank=True, null=True)
    resume = models.FileField(upload_to='Docs/', blank=True, null=True)


    def __str__(self):
        return self.student_id  # Returns Alumni ID


class Placement(models.Model):
    placement_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE, null=True)  # Foreign key to Company
    email = models.EmailField(max_length=191,unique=True)
    contact_number = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=191)
    skill = models.CharField(max_length=191)
    date_of_drive = models.DateField()
    backlogs = models.IntegerField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.placement_id)

class Application(models.Model):
    application_id = models.AutoField(primary_key=True) 
    placement_id = models.ForeignKey(Placement,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE) 
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    passout_year = models.CharField(max_length=4, null=True)
    backlogs = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.application_id)
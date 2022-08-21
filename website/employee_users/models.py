from django.db import models
from sqlalchemy import false, true

# Create your models here.
class Admin_details(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Employee_details(models.Model):
    email = models.EmailField(blank = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    role = models.CharField(max_length=100,blank=True,null=True)
    
class Employee_project(models.Model):

    employee_id = models.ForeignKey(Employee_details,related_name='employee_id',on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    project_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    deadline_date = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=200)



class Role_master(models.Model):
    role_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200,blank=True,null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=200,blank=True,null=True)


class Role_mapping(models.Model):
    role_id = models.CharField(max_length=100,blank=True,null=True)
    user_id = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200,blank=True,null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=200,blank=True,null=True)
    # class Meta:
    #     db_table = 'employee_project'
    #     ordering = ('-created_at',)
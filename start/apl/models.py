from django.db import models
import datetime
# Create your models here.
class login(models.Model):
    EmpName=models.CharField(max_length=100,unique=True)
    Password=models.CharField(max_length=50)
    Role=models.CharField(max_length=20)
    def __str__(self):
        return self.EmpName



item=(
    ('Food','Food'),
    ('Travelling','Travelling'),
    ('Medical','Medical'),
    ('Internet','Internet'),
    ('Other','Other'),
)
class Employee(models.Model):
    Employee_Name=models.CharField(max_length=80)
    Employee_Id=models.CharField(max_length=80)
    Employee_Designation=models.CharField(max_length=80)
    Date=models.DateField(null=True, blank=True)
    Type_of_Reimbursement=models.CharField(max_length=70,default='New Type_of_Reimbursement=models',choices=item)
    Description=models.TextField(max_length=400)
    Upload_Bill=models.ImageField(upload_to='pics',blank="True",null="True")
    Expense_Ammount_In_Rs=models.IntegerField()
    Status=models.CharField(default="Pending",max_length=20)
    
    def __str__(self):
        return self.Employee_Name
    
  

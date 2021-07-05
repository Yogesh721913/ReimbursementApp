from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . form import Emplogin
from .models import login
from .models import Employee
from django.contrib import messages
#from django.contrib.auth import authenticate    


# Create your views here.

def boot(request):
    return render(request,'boot.html')
def home(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #role=request.POST['role']
        
        check=login.objects.filter(EmpName=username,Password=password).exists()  #if we write .exists()after filter then it returns true or false if not write then returns value  
        if check:
          value=login.objects.filter(EmpName=username).first() #if more than one employee have same Empname in table then .first()return record of first employee
          if value.Role=='Emp':
           name1=value.EmpName
           print(id)
           return redirect('/empredirect/'+ name1)
          else:
              if  value.Role=='Admin':
                  
               return redirect('/Show')


        else:
            messages.success(request,"Invalid Credential")  
            return render(request,'login.html')

    else:
     return render(request,'login.html')





def employee(request):
    if request.method=='POST':
     emp=Employee()
     Name=request.POST['Name']
     Email=request.POST['email']
     desig=request.POST['deg']
     dd=request.POST['drop']
     desc=request.POST['des']
     date=request.POST['date']
     file=request.FILES['file']
     exp=request.POST['exp']
     emp.Employee_Name=Name
     emp.Employee_Id=Email
     emp.Employee_Designation=desig
     emp.Date=date
     emp.Type_of_Reimbursement=dd
     emp. Description=desc
     emp.Expense_Ammount_In_Rs=exp
     emp.Upload_Bill=file
     emp.save()
     messages.success(request,'Request has been submitted ')
     return redirect('/Requestform')
     #return HttpResponse("Request has been submitted")
    return render(request,"Requestform.html")
    
def show(request):
    sho=Employee.objects.all()
    
    return  render(request,'show.html',{'show':sho})


def Delete(request,id):
    eid=Employee.objects.get(id=id)  
    eid.delete()
    return redirect('/Show')


def adminrequest(request):
    if request.method=='POST':
     emp=Employee()
     Name=request.POST['Name']
     Email=request.POST['email']
     desig=request.POST['deg']
     dd=request.POST['drop']
     desc=request.POST['des']
     date=request.POST['date']
     file=request.FILES['file']
     exp=request.POST['exp']
     emp.Employee_Name=Name
     emp.Employee_Id=Email
     emp.Employee_Designation=desig
     emp.Date=date
     emp.Type_of_Reimbursement=dd
     emp. Description=desc
     emp.Expense_Ammount_In_Rs=exp
     emp.Upload_Bill=file
     emp.save()
     #messages.success(request,'Request has been submitted ')
     return redirect('/Show')
     #return HttpResponse("Request has been submitted")
    return render(request,"Requestform.html")

def empredirect(request,name1):

    return render(request ,'empredirect.html',{'nam':name1})


def statusupdateapprove(request,id):
    upd=Employee.objects.filter(id=id).first()
    upd.Status="Approved"
    upd.save()
    return redirect('/Show')

def statusupdatedisapprove(request,id):
    upd=Employee.objects.filter(id=id).first()
    upd.Status="Rejected"
    upd.save()
    return redirect('/Show')    


def showpastreq(request,take):
  data=Employee.objects.filter(Employee_Name=take).exists()  
  if data:
      record=Employee.objects.filter(Employee_Name=take)
      return render(request,'showpast.html',{'show':record})
  else:
      return HttpResponse("Request Not found")    
  
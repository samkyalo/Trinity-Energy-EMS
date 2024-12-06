from django.db.models.fields import return_None
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from .models import Employee,Myusers
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import EmployeeForm
from django.contrib import auth,messages

# Create your views here.
def index(request):
    return render(request,'employees/index.html',
    {
        'employees':Employee.objects.all()
    })

# kuonyeshana employees
def view_employee(request,id):
    employee=Employee.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

#kuadd 
def add(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            new_employee_number=form.cleaned_data['employee_number']
            new_first_name=form.cleaned_data['first_name']
            new_last_name=form.cleaned_data['last_name']
            new_email=form.cleaned_data['email']
            new_department=form.cleaned_data['department']
            new_salary=form.cleaned_data['salary']


            new_employee=Employee(
                employee_number= new_employee_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                department=new_department,
                salary=new_salary,

            )
            new_employee.save()
            return render(request,'employees/add.html',{
                'form':EmployeeForm(),
                'success':True
            })
        else:
            form=EmployeeForm()
    return render(request,'employees/add.html',{
            'form':EmployeeForm()
        })
def edit(request,id):
    employee=Employee.objects.get(pk=id)
    if request.method =='POST':
        
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return render(request,'employees/edit.html',
            {

                'form':form,
                'success':True
            })
    else:
        
        form=EmployeeForm(instance=employee)
    return render(request,'employees/edit.html',{
            'form':form,
            'employee':employee
    })
    
def delete(request,id):
    if request.method=='POST':
        employee=Employee.objects.get(pk=id)
        employee.delete()
    return HttpResponseRedirect(reverse('index'))

def home(request):
    return render(request,'employees/home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
    return render(request,'employees/login.html')
def logout(request):
    auth.logout(request),
    messages.info(request,'You have been logged out'),
    return redirect('/')
def adduser(request):
    return render(request,'employees/users.html')


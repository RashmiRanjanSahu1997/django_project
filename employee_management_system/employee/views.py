from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps':emps}    
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        print(request.POST['first_name'],'=ffffffffffffffffffffffffff')
        first_name = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        # hiredate = request.POST('hire_date')
        new_emp = Employee(first_name=first_name,lastname=lastname,email=email,phone=phone,salary=salary,bonus=bonus,dept_id = dept,role_id = role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return render(request,'add_emp.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse('Record Deleted Successfully')
        except:
            return HttpResponse('Please Enter A valid Emp id')
    emps = Employee.objects.all()
    context = {'emps':emps} 
    return render(request,'remove_emp.html',context)


def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        dept = request.POST['dept']
        emp = Employee.objects.all()
        if name:
            emps = emp.filter(Q(first_name__icontains = name) | Q(lastname__icontains=name))
        if dept:
            emps = emp.filter(dept__name = dept)
        if email:
            emps = emp.filter(email__icontains=email)
        context = {emps:emps}
        print(context,'ffffffffffffffffffffffffff')
        return render(request,'all_emp.html',context)
    elif request.method == "GET":
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('Envalid input')

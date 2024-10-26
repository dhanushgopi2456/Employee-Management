from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.db.models import *
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')
def view_all_emp(request):
    template=loader.get_template('view_all_emp.html')
    mylist=Employee.objects.all()
    context={
        'mylist':mylist,
    }
    return HttpResponse(template.render(context,request))

def add_emp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phonenum = request.POST['phonenum']
        dept_id = request.POST['department'] 
        role_id = request.POST['role']  

        dept = Department.objects.get(id=dept_id) 
        role = Role.objects.get(id=role_id) 
        new_emp = Employee(
            firstname=firstname,
            lastname=lastname,
            salary=salary,
            bonus=bonus,
            phonenum=phonenum,
            dept=dept,
            role=role
        )
        new_emp.save()
        return redirect('view_all_emp')  
    else:
        departments = Department.objects.all()  
        roles = Role.objects.all()  
        return render(request, 'add_emp.html', {'departments': departments, 'roles': roles})

def remove_emp(request):
    if request.method == 'POST':
        emp_id = request.POST['employee']
        emp = Employee.objects.get(id=emp_id) 
        emp.delete()
        return redirect('view_all_emp')
    else:
        employees = Employee.objects.all()
        return render(request, 'remove_emp.html', {'employees': employees})
    

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        mylist = Employee.objects.all()
        if name:
            mylist = mylist.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name))
        if dept:
            mylist = mylist.filter(dept__name__icontains = dept)
        if role:
            mylist = mylist.filter(role__name__icontains = role)

        context = {
            'mylist': mylist
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
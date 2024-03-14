from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request): #read
 context = {'employee_list':Employee.objects.all() }
 return render(request, "emp_reg/employee_list.html",context)


def employee_form(request, id=0): #get and post request for insert and updfate operations
 if request.method =='GET':
  if id==0: #if it is insert operation 
   form= EmployeeForm()
  else: #if it is update operation
   employee= Employee.objects.get(pk=id)
   form=EmployeeForm (instance=employee)
  return render(request, "emp_reg/employee_form.html",{'form': form})
 else:
  if id==0:
   form= EmployeeForm(request.POST)
  else:
   employee= Employee.objects.get(pk=id)
   form= EmployeeForm(request.POST,instance=employee)
  if form.is_valid():
    form.save()
  return redirect("/employee/list")


def employee_delete(request,id): #to delete employee
 employee= Employee.objects.get(pk=id)#retieve the data from given id
 employee.delete()
 return redirect("/employee/list")
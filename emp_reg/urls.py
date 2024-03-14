
from django.urls import path,include
from . import views

urlpatterns = [
 path('',views.employee_form, name='employee_insert'), #get and post request for insert

 path('<int:id>/',views.employee_form, name='employee_update'), #get and post request for update operation
 path('list/',views.employee_list, name='employee_list'), #get request to retrive and display all records 
 path('delete/<int:id>/',views.employee_delete,name='employee_delete')#post request to delete the data

]

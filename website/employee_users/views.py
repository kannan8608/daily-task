
from django.shortcuts import redirect, render
from .models import Admin_details,Employee_details,Employee_project,Role_master,Role_mapping
import psycopg2
import psycopg2.extras



def login(request):
    return render(request,'login.html')

# def home(request):
#     return render(request,'home.html')

def home(request):
    return render(request,'home.html')

# def Error(request):
#     return render(request,'Error.html')
# def view(request):
#     return render(request,'view.html')   
        

def profile(request):
    # if request.method=='POST':
    #     uname1=request.POST.get('uname')
    #     password1=request.POST.get('password')
    #     details=Employee_details.objects.get(email=uname1,password=password1)
    #     if details.email==uname1 and details.password==password1:
    #         return render(request,'profile.html')
    if request.method=='POST':
        uname1=request.POST.get('uname')
        password1=request.POST.get('password')
        details=Employee_details.objects.get(email=uname1,password=password1)
        if details.email==uname1 and details.password==password1:
            if details.role=='Admin':
                mydata = Employee_project.objects.all()
            
                context = {'mymembers': mydata,}
            
                return render(request,'view.html',context)
            else:
                mydata = Employee_project.objects.filter(employee_id_id=details)
            
                context = {'mymembers': mydata,}
            
            return render(request,'view.html',context)
        else:
            return render(request,'Error.html')
    # else:
    #         return render(request,'profile.html')


def Admin_details(request):
    if request.method=='POST':
        uname=request.method.get('uname')
        password=request.method.get('password')
        admin_details=Admin_details(uname=uname,password=password)
        admin_details.save()
    return render(request,'register.html')

def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        mobile_number=request.POST.get('mobile_number')
        city=request.POST.get('city')
        password=request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        role=('consumer')
        employee_details=Employee_details(email=email,password=password,repeat_password=repeat_password,first_name=first_name,last_name=last_name,mobile_number=mobile_number,city=city,role=role)
        employee_details.save()



    return render(request,'register.html')


def submit(request):
    if request.method=='POST':
        project_title=request.POST.get('project_title')

        employee_name =request.POST.get('employee_name')

        project_number =request.POST.get('project_number')

        description =request.POST.get('description')

        deadline_date =request.POST.get('deadline_date')

        details=Employee_details.objects.get(first_name=employee_name)
        employee_project=Employee_project(project_title=project_title,employee_name=employee_name,project_number=project_number,description=description,deadline_date=deadline_date,created_by=details,employee_id=details)
        employee_project.save()
        role_master=Role_master.objects.get(role_name='consumer').id
  
        userid = employee_project.id
 
        rolemappingobj = Role_mapping(role_id = role_master,user_id=userid )
        rolemappingobj.save()
        
    return render(request,'profile.html')



# def view(request):
#     # if request.method=='POST':
#     mydata = Employee_project.objects.all()
#     context = {
#     'mymembers': mydata,
# }
#     return render(request,'view.html',context)

# def consumer(request):
#     if request.method=='POST':
#         uname1=request.POST.get('uname')
#         password1=request.POST.get('password')
#         details=Employee_details.objects.get(email=uname1,password=password1)
#         if details.email==uname1 and details.password==password1:
#             mydata = Employee_project.objects.filter(employee_id_id=details.email.id)
#             print('mydata=',mydata)
#             context = {'mymembers': mydata,}
#             print('context=',context)
#             return render(request,'consumer_view.html',context)
#     else:
#         return render(request,'profile.html')

from django.urls import path
from django.contrib import admin
from . import views

app_name = "employee_users"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('home/profile/',views.profile, name='profile'),
    path('home/Error/',views.Error, name='Error'),
    # path('home/profile/view/',views.view, name='view'),
    # path('home/profile/consumer/',views.consumer, name='consumer'),
    path('home/register/',views.register, name='register'),
    path('Admin_details/',views.Admin_details, name='Admin_details'),
    path('home/profile/submit/',views.submit, name='submit'),
]
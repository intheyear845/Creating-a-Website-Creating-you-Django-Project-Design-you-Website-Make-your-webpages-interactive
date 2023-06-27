from django.urls import path
from . import views
app_name='cust'

urlpatterns=[
    path('customers_home/', views.getcustomershome,name="Customers"),
    path('abcd_home/', views.getabcdhome,name="ABCD"),
    path('master_home/', views.getmasterhome,name="Master"),
    path('change_password/', views.getchangepassword,name="ChangePassword"),
    path('my_profile/', views.getmyprofile,name="MyProfile"),
    path('settings_home/', views.getmysettingshome,name="Settings"),
    path('xyz_home/', views.getxyzhome,name="XYZ"),
]
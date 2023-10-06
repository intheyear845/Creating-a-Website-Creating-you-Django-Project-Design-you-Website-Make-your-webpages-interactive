from django.urls import path
from . import views
app_name='css_asg'

urlpatterns=[
    path('master_home/', views.getmasterhome,name="Master"),
    path('home_home/', views.gethomehome,name="Home"),
    path('courses_home/', views.getcourseshome,name="Courses"),
    path('contact_home/', views.getcontacthome,name="Contact"),
]
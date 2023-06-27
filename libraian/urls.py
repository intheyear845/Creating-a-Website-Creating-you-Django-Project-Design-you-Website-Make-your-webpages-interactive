from django.urls import path
from . import views 
app_name='lib'

urlpatterns=[
    path('libraians_home/', views.getlibrarianshome,name="Library"),
    path('book_collection/', views.getbooks,name="Books")
]
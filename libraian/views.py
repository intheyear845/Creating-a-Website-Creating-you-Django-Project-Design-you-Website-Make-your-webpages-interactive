from django.shortcuts import render

# Create your views here.

def getlibrarianshome(request):
    return render(request,'librarians.html')

def getbooks(request):
    return render(request,'books.html')
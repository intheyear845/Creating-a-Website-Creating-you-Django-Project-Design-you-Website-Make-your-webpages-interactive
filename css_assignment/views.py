from django.shortcuts import render

# Create your views here.
def getmasterhome(request):
    return render(request,'master.html')

def gethomehome(request):
    return render(request,'home.html')

def getcourseshome(request):
    return render(request,'courses.html')

def getcontacthome(request):
    return render(request,'contact.html')


from django.shortcuts import render

# Create your views here.
def getcustomershome(request):
    return render(request,'customers.html')

def getabcdhome(request):
    return render(request,'abcd.html')

def getmasterhome(request):
    return render(request, 'master.html')

def getchangepassword(request):
    return render(request, 'changepassword.html')

def getmyprofile(request):
    return render(request, 'myprofile.html')

def getmysettingshome(request):
    return render(request, 'settings.html')

def getxyzhome(request):
    return render(request, 'xyz.html')
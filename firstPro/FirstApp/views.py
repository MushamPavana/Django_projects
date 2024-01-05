from django.shortcuts import render,redirect
from FirstApp.models import employee

def HomePage(request):
    return render(request, 'HomePage.html')

def signupPage(request):
    if request.method == 'POST':
        ausername=request.POST['uname']
        aEmail=request.POST['Email']
        apassword=request.POST['password']
        apassword1=request.POST['password1']
        print(ausername,apassword,aEmail,apassword1)
        details=employee(username=ausername,Email=aEmail,password=apassword,password1=apassword1)
        details.save()
        return redirect('login')
    return render(request, 'signup.html')

def loginPage(request):
    return render(request, 'login.html')

def logoutPage(request):
   return render(request, 'logout.html')

 
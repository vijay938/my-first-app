from django.shortcuts import render,HttpResponse
from app.models import Contact

# Create your views here.
def about(request):
    return render(request,'about.html')
def Home(request):
    return render(request,'Home.html')
def Services(request):
    return render(request,'Services.html')
def Contacts(request):
    if request.method == "POST":
      name=request.POST.get('name')
      address=request.POST.get('address')
      Contacts=Contact(name=name,address=address)
      Contacts.save()
      
    return render(request,'Contacts.html')
def Hello(request):
      return HttpResponse('This is Hello page')
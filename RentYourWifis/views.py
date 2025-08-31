from ast import Pass
import re
from urllib import request
from django.forms import EmailField
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from collectdata.models import collectFormData
from  ourServiceDetail.models import  ourService
from rechargePlans.models import rechargePlans  

def home(request):

 rechargePlanPrice = rechargePlans.objects.all().order_by('planPrice')
 data = {
    'rechargePlanPrice1': rechargePlanPrice
          } 
 return render(request,'index.html',data)

def contact(request):
#    return render(request,'Contact.html')
    if request.method=='post':
        data ={}
    try :  
        FIRSTNAME = request.POST.get('name')
        EmailField = request.POST.get('email')
        Usermessage = request.POST.get('msgContent')
        data =  {
                'usesName' : FIRSTNAME,
                'userEmail' : EmailField , 
                'userMess' : Usermessage
                }
        return render(request, 'contact.html',data)
    except :
          
          return render(request,'contact.html',data)

def header(request):
    return render(request,'header.html')
def footer(request):
    return render(request,'footer.html')
def base(request):
    return render(request,'base.html')
def about(request):
    if request.method=='post':
        data ={}
    try :  
        FIRSTNAME = request.POST.get('name')
        EmailField = request.POST.get('email')
        Usermessage = request.POST.get('msgContent')
        
        data =  {
                'usesName' : FIRSTNAME,
                'userEmail' : EmailField , 
                'userMess' : Usermessage
                }
        return render(request, 'AboutUs.html',data)
    except :
          
          return render(request,'AboutUs.html',data)

    # return render(request,'AboutUs.html')
def ourservices(request):
   servicesNow = ourService.objects.all()
   data = {
    'serviceNow1': servicesNow
          }
   return render(request,'OurServices.html',data)
def term(request):
    return render(request,'Terms.html')

def contactData(request):
    return render(request,'Contact.html')

def saveEnquiry(request):
    if request.method=='post':
         data = {}
    try : 
         FIRSTNAME  =  request.POST.get('name')
         EmailField =  request.POST.get('email')
         Usermessage = request.POST.get('msgContent')
         en = collectFormData(userName=FIRSTNAME,userEmail=EmailField,userMess=Usermessage)
         en.save()
         return render(request, 'AboutUs.html')
    except :
        return render(request, 'AboutUs.html')

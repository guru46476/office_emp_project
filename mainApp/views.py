from django.http import HttpResponseRedirect
from django.shortcuts import render
from mainApp.models import Employee


def homePage(request):
    data = Employee.objects.all()
    return render(request,"index.html",{"Data":data})

def addRecord(request):
    if(request.method=='POST'):
        e = Employee()
        e.name = request.POST.get('name')
        e.role = request.POST.get('role')
        e.salary = request.POST.get('salary')
        e.email = request.POST.get('email')
        e.phone = request.POST.get('phone')
        e.hiredate = request.POST.get('hiredate')
        e.location = request.POST.get('location')
        e.save()
        return HttpResponseRedirect('/')
    return render(request,"add.html")

# YOU CAN USE ID NAME OR NUM OR ANYTHING TO GET ID(request,write which u want to get)
def updateRecord(request,ID):
    data = Employee.objects.get(id=ID)
    if (request.method=="POST"):
        data.name = request.POST.get('name')
        data.role = request.POST.get('role')
        data.salary = request.POST.get('salary')
        data.email = request.POST.get('email')
        data.phone = request.POST.get('phone')
        data.location = request.POST.get('location')
        data.save()
        return HttpResponseRedirect('/')
    return render(request,"update.html",{"Data":data})    

def deleteRecord(request,num):
    data = Employee.objects.get(id=num)
    data.delete()
    return HttpResponseRedirect("/")    

#  src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
#         integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"
from django.shortcuts import render,redirect
from .models import Studentdetails
from .models import Payment
from .models import Certificate
from .models import Exam

# Create your views here.


def index(request):
    return render(request,"index.html")

def profile(request):
    return render(request,"profile.html")

def course(request):
    return render(request,"course.html")

def login(request):
    return render(request,"login.html")

def forgot(request):
    return render(request,"forgot.html")

def reset(request):
    return render(request,"reset.html")

def register(request):
    return render(request,"register.html")

def studentdetails(request):
    if request.method == "POST":
        registerno = request.POST.get("registerno")
        name = request.POST.get("name")
        fathername = request.POST.get("fathername")
        dob = request.POST.get("dob")
        phonenumber = request.POST.get("phonenumber")
        mail = request.POST.get("mail")
        studentdetails = Studentdetails(registerno=registerno, name=name, fathername=fathername, dob=dob, phonenumber=phonenumber, mail=mail)
        studentdetails.save()
        return redirect("index")
    else:
        return render(request,"studentdetails.html")

def payment(request):
    if request.method =="POST":
        registerno = request.POST.get("registerno")
        name = request.POST.get("name")
        billdate = request.POST.get("billdate")
        reciptno = request.POST.get("reciptno")
        course = request.POST.get("course")
        feesamount = request.POST.get("feesamount")
        paytype = request.POST.get("paytype")
        status = request.POST.get("status")
        payment = Payment(registerno=registerno, name=name, billdate=billdate, reciptno=reciptno, course=course, feesamount=feesamount, paytype=paytype, status=status)
        payment.save()
        return redirect("index")
    else:
        return render(request,"payment.html")

def certificate(request):
    if request.method =="POST":
        registerno = request.POST.get("registerno")
        name = request.POST.get("name")
        course = request.POST.get("course")
        date = request.POST.get("date")
        feesamount = request.POST.get("feesamount")
        certificate = Certificate(registerno=registerno, name=name, course=course, date=date, feesamount=feesamount)
        certificate.save()
        return redirect("index")
    else:
        return render(request,"certificate.html")

def exam(request):
    if request.method =="POST":
        registerno = request.POST.get("registerno")
        name = request.POST.get("name")
        course = request.POST.get("course")
        feesamount = request.POST.get("feesamount")
        paytype = request.POST.get("paytype")
        exam = Exam(registerno=registerno, name=name, course=course, feesamount=feesamount, paytype=paytype)
        exam.save()
        return redirect("index")
    else:
        return render(request,"exam.html")

def display(request):
    tablea = Studentdetails.objects.all()
    return render(request,'studenttable.html',{'tablea':tablea})

def read(request):
    tableb = Payment.objects.all()
    return render(request,'paymenttable.html',{'tableb':tableb})

def display1(request):
    tablec = Certificate.objects.all()
    return render(request,'certificatetable.html',{'tablec':tablec})

def read1(request):
    tabled = Exam.objects.all()
    return render(request,'examtable.html',{'tabled':tabled})




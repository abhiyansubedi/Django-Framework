from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect

from service.models import Service
from .forms import usersForm

def HomePage(request):
    servicesData=Service.objects.all()
    # for a in servicesData:
    #     print(a.service_title)
    # print(services)
    data={
        'servicesData':servicesData
    }
    return render(request,"service.html",data)
    
   



def aboutUS(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"test.html",{'output':output})

def course(request):
    return HttpResponse("Faculties")

def userForm(request):
    ans=0
    fn=usersForm()

    data={'form':fn}
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            ans=n1+n2
            data={
                'form':fn,
                'output':ans
                 
            }
            url="about-us/?output={}".format(ans)
            return redirect(url)
    except:
        pass

    return render(request,"userform.html",data)


def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            op=request.POST.get('opr')

            if op=="+":
                c=n1+n2
            elif op=="-":
                c=n1-n2
            elif op=="*":
                c=n1*n2
            elif op=="/":
                c=n1/n2
    except:
        c="Invalid opr......"
    
    print(c)
    return render(request,"calculator.html",{'c':c})

def evenodd(request):
        c=''
        if request.method=="POST":
            if request.POST.get('num1')=="":
                return render(request,"Even_odd.html",{'error':True})

            n=int(request.POST.get("num1"))
            if n%2==0:
                c="EVEN NUMBER"
            else:
                c="ODD NUMBER"

        return render(request,"Even_odd.html",{'c':c})


def marksheet(request):
    t=''
    p=''
    d=''
    try:
        if request.method=="POST":
            s1=eval(request.POST.get("sub1"))
            s2=eval(request.POST.get("sub2"))
            s3=eval(request.POST.get("sub3"))
            s4=eval(request.POST.get("sub4"))
            s5=eval(request.POST.get("sub5"))
             
            t=s1+s2+s3+s4+s5
            p=t/5
            
            
            if p > 90:
                d="A"
            elif p<90 and p>80:
                d="B"
            elif p<80 and p>70:
                d="C"
            else:
                d="failed"
    except:
        print("Invalid")
    
    return render(request,"marksheet.html",{'t':t, 'p':p, 'd':d})


    





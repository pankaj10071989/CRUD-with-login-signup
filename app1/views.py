from django.contrib.auth.hashers import check_password
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import signup

def dashboard(request):
    return render(request,'dashboard.html')

def verify(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        try:
            st = signup.getdata_username(email)
        except signup.DoesNotExist:
            st=None
        con={
            'em': email
        }
        error_msg = None
        if st is not None:
            if (password==st.password and email==st.email):
                return render(request,'dashboard.html',con)
            else:
                error_msg = 'Invalid email/password !!'
        else:
            error_msg = 'Invalid email/password !!'
        return render(request, 'login.html', {'error': error_msg})


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')

def logout(request):
    return redirect('home')

def signup1(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        pic = request.POST['image']
        ins = signup(fname=fname, lname=lname, email=email, phone=phone, password=password,pic=pic)
        ins.save()
        return render(request, 'signup_success.html')

    return render(request, 'signup.html')

def getdata(request):
        obj = signup.objects.all()
        return render(request, 'display.html', {'stu': obj})

def getdatabyid(request):
    if request.method == 'POST':
        id = request.POST['id']
        try:
            s = signup.objects.get(id=id)
        except signup.DoesNotExist:
            s=None
        error_msg='Data not found'
        if s:
            con={
                'info':s
            }
            return render(request, 'displaybyid.html',con)
        else:
            con={
                'er':error_msg
            }
            return render(request, 'displaybyid.html',con )

    return render(request, 'displaybyid.html')

def deletedata(request,pk):
    if request.method == 'POST':
        s = signup.objects.get(id=pk)
        s.delete()
        return redirect('getdata')
    return render(request, 'display.html')

def editdata(request,pk):
    if request.method == 'GET':
        s = signup.objects.get(id=pk)
        return render(request,'update.html',{'info':s})
    return render(request, 'display.html')

def updatedata(request,pk):
    if request.method=='POST':
        s = signup.objects.get(id=pk)
        s.fname = request.POST['firstname']
        s.lname = request.POST['lastname']
        s.email = request.POST['email']
        s.phone = request.POST['phone']
        s.password = request.POST['password']
        s.save()
        return redirect('getdata')
    return render(request,'update.html')

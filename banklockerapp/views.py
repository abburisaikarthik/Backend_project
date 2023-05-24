from random import randint

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def index(request):
    data = About.objects.all()
    d = {'data': data}
    contact = Contact.objects.all()
    d = {'data': data}
    return render(request, "index_home.html", locals())

def dashboard(request):
    admin = Subbanker.objects.all()
    type = Lockertype.objects.all()
    assign = Assignlocker.objects.all()
    return render(request, "admin_dashboard.html", locals())

def authentication_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        try:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('dashboard')
            if user:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('dashboard')
            else:
                messages.success(request, "Invalid User")
                return redirect('authentication_login')
        except:
            messages.success(request, "Invalid User")
            return redirect('authentication_login')
    return render(request, "authentication-login.html")

@login_required(login_url='/authentication_login/')
def change_password(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(c)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('admin_change_password')

    return render(request, 'change_password.html')

@login_required(login_url='/authentication_login/')
def logout_user(request):
    logout(request)
    messages.success(request, "logout Successful")
    return redirect('authentication_login')

@login_required(login_url='/authentication_login/')
def add_subbanker(request, pid=None):
    user = None
    subbanker = None
    if pid:
        user = User.objects.get(id=pid)
        subbanker = Subbanker.objects.get(user=user)
    if request.method == "POST":
        form = SubbankerForm(request.POST, request.FILES, instance=subbanker)
        if form.is_valid():
            new_subbanker = form.save()
            if pid:
                new_user = User.objects.filter(id=pid).update(email=request.POST['email'], first_name=request.POST['firstname'])
                Subbanker.objects.filter(user=request.user).update(mobile=request.POST['mobile'])
            else:
                new_user = User.objects.create_user(username=request.POST['username'],
                                                    first_name=request.POST['firstname'], email=request.POST['email'],
                                                    password=request.POST['password'],)
                new_subbanker.user = new_user
                new_subbanker.save()
        messages.success(request, "Registration Successful")
        return redirect('view_subbanker')
    return render(request, 'add_subbanker.html', locals())

@login_required(login_url='/authentication_login/')
def view_subbanker(request):
    data = Subbanker.objects.all()
    d = {'data': data}
    return render(request, "view_subbanker.html", d)

@login_required(login_url='/authentication_login/')
def delete_subbanker(request, pid):
    data = Subbanker.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('view_subbanker')

@login_required(login_url='/authentication_login/')
def add_lockertype(request, pid=None):
    lockertype = None
    if pid:
        lockertype = Lockertype.objects.get(id=pid)
    if request.method == "POST":
        lockertype = LockertypeForm(request.POST, request.FILES, instance=lockertype)
        if lockertype.is_valid():
            new_lockertype = lockertype.save()
            new_lockertype.save()
        if pid:
            messages.success(request, "Update Locker Successful")
            return redirect('view_lockertype')
        else:
            messages.success(request, "Add Locker Successful")
            return redirect('view_lockertype')
    return render(request, 'add_lockertype.html', locals())

@login_required(login_url='/authentication_login/')
def view_lockertype(request):
    data = Lockertype.objects.all()
    d = {'data': data}
    return render(request, "view_lockertype.html", d)

@login_required(login_url='/authentication_login/')
def delete_lockertype(request, pid):
    data = Lockertype.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('view_lockertype')

@login_required(login_url='/authentication_login/')
def add_assign(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        occupation = request.POST['occupation']
        lockernumber = request.POST['lockernumber']
        keynumber = request.POST['keynumber']
        instruction = request.POST['instruction']
        nominee = request.POST['nominee']
        relnominee = request.POST['relnominee']
        valuable = request.POST['valuable']
        idproof = request.POST['idproof']
        type = request.POST['type']
        status = request.POST['status']
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        typeobj = Lockertype.objects.get(id=type)

        Assignlocker.objects.create(fullname=fullname, email=email, status=status, mobile=mobile, address=address,occupation=occupation, lockernumber=lockernumber, keynumber=keynumber, instruction=instruction, nominee=nominee, relnominee=relnominee, valuable=valuable, idproof=idproof, image=image, image2=image2,  type=typeobj)
        messages.success(request, "Add Successful")
        return redirect('view_assign')
    mylockertype = Lockertype.objects.all()
    return render(request, 'add_assign.html', locals())

def edit_assign(request, pid):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        occupation = request.POST['occupation']
        lockernumber = request.POST['lockernumber']
        keynumber = request.POST['keynumber']
        instruction = request.POST['instruction']
        nominee = request.POST['nominee']
        relnominee = request.POST['relnominee']
        valuable = request.POST['valuable']
        status = request.POST['status']
        idproof = request.POST['idproof']
        type = request.POST['type']
        try:
            image = request.FILES['image']
            data = Assignlocker.objects.get(id=pid)
            data.image = image
            data.save()
        except:
            pass

        try:
            image2 = request.FILES['image2']
            data = Assignlocker.objects.get(id=pid)
            data.image2 = image2
            data.save()
        except:
            pass
        Assignlocker.objects.filter(id=pid).update(fullname=fullname, email=email, status=status, mobile=mobile, address=address,
                                                   occupation=occupation, lockernumber=lockernumber,
                                                   keynumber=keynumber, instruction=instruction, nominee=nominee,
                                                   relnominee=relnominee, valuable=valuable, idproof=idproof, type=type)
        messages.success(request, "Update Successful")
        return redirect('view_assign')
    data = Assignlocker.objects.get(id=pid)
    mylockertype = Lockertype.objects.all()
    return render(request, "edit_assign.html", locals())

@login_required(login_url='/authentication_login/')
def view_assign(request):
    data = Assignlocker.objects.all()
    d = {'data': data}
    return render(request, "view_assign.html", d)

def detail(request,pid):
    data = Assignlocker.objects.get(id=pid)
    return render(request, "index_detail_view.html", locals())

@login_required(login_url='/authentication_login/')
def delete_assign(request, pid):
    data = Assignlocker.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('view_assign')

def index_search_locker(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        data2 = True
        data = Assignlocker.objects.filter(lockernumber__icontains=fromdate)
    return render(request, "index_search_locker.html", locals())

@login_required(login_url='/authentication_login/')
def report_date(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']

        data = Assignlocker.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate)
        data2 = True
    return render(request, "report_date.html", locals())

@login_required(login_url='/authentication_login/')
def search_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        data2 = True
        data = Assignlocker.objects.filter(Q(fullname__icontains=fromdate)|Q (lockernumber__icontains=fromdate)|Q(keynumber__icontains=fromdate))
    return render(request, "search_report.html", locals())

@login_required(login_url='/authentication_login/')
def about(request):
    if request.method == "POST":
        pagetitle = request.POST['pagetitle']
        description = request.POST['description']
        About.objects.filter(id=1).update(pagetitle=pagetitle, description=description)
        messages.success(request, "Update About Successful")
        return redirect('about')
    data = About.objects.get(id=1)
    return render(request, "about.html", locals())

@login_required(login_url='/admin_login/')
def contact(request):
    if request.method == "POST":
        pagetitle = request.POST['pagetitle']
        description = request.POST['description']
        email = request.POST['email']
        mobile = request.POST['mobile']

        Contact.objects.filter(id=1).update(pagetitle=pagetitle, description=description, email=email)
        messages.success(request, "Update Contact Successful")
        return redirect('contact')
    data = Contact.objects.get(id=1)
    return render(request, "contact.html", locals())

@login_required(login_url='/authentication_login/')
def profile(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        email = request.POST['email']
        uname = request.POST['username']
        mobile = request.POST['mobile']

        user = User.objects.filter(id=request.user.id).update(first_name=fname, email=email, username=uname)
        Subbanker.objects.filter(user=request.user).update(mobile=mobile)
        messages.success(request, "Updation Successful")
        return redirect('profile')
    data = Subbanker.objects.get(user=request.user)
    return render(request, "profile.html", locals())


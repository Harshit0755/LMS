import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from MyApp.forms import *
from MyApp.models import *
import requests



headers = { "X-Api-Key": "85fa69f496dec0b77cf2f538b3ef5f8e",
            "X-Auth-Token": "99cc1530aad3f42e6fcf244ee1c9d644"}

# Create your views here.
def Course_Home(request):

    courses = CourseDetails.objects.all()
    courses1 = CourseDetails.objects.order_by('-rating')
    d = {
        "courses": courses,"courses1": courses1
    }
    return render(request,"index.html",d)

def CourseList(request):
    courses=CourseDetails.objects.all()
    return render(request,"courses.html",{"courses":courses})




def Course_Details_Page(request, m_id):
    if not request.user.is_authenticated:
        return redirect("logout")

    error=True
    Usr=request.user

    a=1
    n_id=1
    course = CourseDetails.objects.filter(id = m_id).first()
    course1 = CourseDetails.objects.all()
    lec=LecturesModel.objects.filter(id=n_id)
    for i in lec:
        n_id=n_id+1
    print(n_id)

    St = Checkout.objects.filter(course_idd=m_id, usr=Usr).last()
    St5 = Checkout.objects.filter(course_idd=m_id, status="Booked")
    c=0
    for i in St5:
        c=c+1
   # St2 = Checkout.objects.filter(course_idd=m_id,).last()
    # sheets = Checkout.objects.filter(id=st_id)

    if (St.status=="Booked"):
        error = False

    if request.method == "POST":
        data = request.POST
        usr = request.user
        St1 = Checkout.objects.create(usr=usr, status="Pending", course_idd=m_id)
        error = True

        if (St.status=="Booked"):
            print(Usr)
            print("already enrolled")
            error=False
            #return redirect('gotocourse')

        else:
            error = False
            return redirect("payment")





    return render(request, "course-single.html", {"course":course,"id":m_id,"n_id":n_id,"a":a, "course1":course1, "lec":lec, "c":c, "error":error, "St":St, "St5":St5})


@login_required
def GoToCourse(request,m_id, n_id):
    Usr=request.user

    course = CourseDetails.objects.filter(id = m_id).first()
    #course1 = CourseDetails.objects.all()
    lec = LecturesModel.objects.filter(course_id=m_id)
    lec1 = LecturesModel.objects.filter(course_id=m_id, lect_number=n_id).first()
    n_id=int(lec1.lect_number)-1

    return render(request, "gotocourse.html", {"course": course, "m_id":m_id, "n_id":n_id, "lec1":lec1, "lec":lec})

def Login1(request):
    if request.user.is_authenticated:
        return redirect("course_home")

    error=False
    if request.method == "POST":
        un = request.POST["un"]
        ps = request.POST["ps"]
        usr = authenticate(username = un, password = ps)

        if usr:
            login(request, usr)
            return redirect("course_home")
        error=True
    return render(request, "login.html",{"error":error})


def Logout(request):
    logout(request)
    return redirect("login")

def Register(request):
    if request.user.is_authenticated:
        return redirect("courseList")

    error = False
    if request.method == "POST":
        d = request.POST
        name = d['name']
        un = d['un']
        ps = d['ps']
        email = d['email']
        number= d['number']
        usr = User.objects.filter(username = un)
        if not usr:
            usr = User.objects.create_user(un, email, ps)
            usr.first_name = name
            usr.save()
            Course_users.objects.create(usr=usr, name=name, number=number, email= email)
            course = CourseDetails.objects.all().count()
            for m_id in range (0,course+50):

                Checkout.objects.create(usr=usr, status="Default", course_idd=m_id)
            return redirect("login")
        error = True

    return render(request, "register.html", {"error":error})




def MakePayment(request):
    usr = request.user
    St = Checkout.objects.filter(usr=usr, status="Pending").last()
    p=St.course_idd
    print(p)
    St1 = CourseDetails.objects.filter(id=p).first()
    Rs = St1.price

    payload = {
        'purpose': 'Movie Booking',
        'amount': str(Rs),
        'buyer_name': request.user.username,
        'email': request.user.email,
        'phone': "7723818272",
        'redirect_url': 'http://127.0.0.1:8000/PayCheck/{}/'.format(request.user.username),
        'send_email': 'True',
        'send_sms': 'True',
        'allow_repeated_payments': 'False',
    }
    response = requests.post("https://www.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
    obj = json.loads(response.text)
    print(obj)
    Url= obj["payment_request"]["longurl"]
    Idd = obj["payment_request"]["id"]
    Di = Payment_Id.objects.filter(Usr = usr)
    Di.delete()
    Payment_Id.objects.create(Usr=usr, PayId=Idd)
    return redirect(Url)
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

from django.http import HttpResponse
def PayChack(request, Usr):
    Usr=request.user
    usr = User.objects.filter(username = Usr).first()
    pp=Checkout.objects.filter(usr=Usr, status="Pending").last()
    Di = Payment_Id.objects.filter(Usr=usr).first()
    response = requests.get("https://www.instamojo.com/api/1.1/payment-requests/{}/".format(Di.PayId),headers=headers)
    obj = json.loads(response.text)
    Status = obj["payment_request"]["payments"][0]["status"]
    if Status == "Failed":
        # get request
        pp.status="Booked"
        pp.save()

        # print response if you want
        print(response.text)
        return HttpResponse("<h1>Payment Failed</h1><br><a href='#' onclick='history.go(-3)'>Click Here to go back to course</a>")
    else:
        return HttpResponse("<h1>Payment Done... @@</h1><br><a href='#' onclick='history.go(-3)'>Click Here to go back to course</a>")
        print(response.text)

##################################     ADMIN   ##############################

def Admin_Add_Course(request):
    if request.user.is_superuser:
        form = Add_Course_form()
        ss=CourseDetails.objects.last()
        if request.method == "POST":
            form = Add_Course_form(request.POST ,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                usr = request.user
                course = CourseDetails.objects.all().count()
                for m in range(0, course+50):
                    Checkout.objects.create(usr=usr,course_idd=m, status="Default")
                return redirect("add_course")
    else:
        return HttpResponse("You are not an admin.")
    return render(request, "add_course.html", {"form":form})


def Admin_Add_Instructor(request):
    if request.user.is_superuser:
        form = Add_Instructor_form()
        if request.method == "POST":
            form = Add_Instructor_form(request.POST ,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect("add_course")
    else:
        return HttpResponse("You are not an admin")
    return render(request, "add_instructor.html", {"form":form})


def Admin_Add_Lectures(request):
    if request.user.is_superuser:
        form = Add_Lecture_form()
        if request.method == "POST":
            form = Add_Lecture_form(request.POST ,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                return redirect("add_lectures")
    else:
        return HttpResponse("You are not an admin")
    return render(request, "add_lectures.html", {"form":form})


def Contact(request):
    return render(request,"contact.html")

def About(request):
    data=Instructor.objects.all()
    return render(request,"about.html", {"data":data})

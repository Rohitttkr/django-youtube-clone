from distutils.command.build_scripts import first_line_re
from tabnanny import check
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from .forms import VideoFrom
from django.contrib.auth import authenticate, login
from .models import Otp, Profile, VideosUpload
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup(request):
    if request.method == 'POST':

        pass1 = request.POST.get("pass")
        cpass = request.POST.get("cpass")

        if pass1 == cpass:
            try:
                user = User.objects.get(username = request.POST.get('email'))
            
            except User.DoesNotExist:

                x = request.POST.get('name').split(" ")
                user_p = request.POST.get('email')
                has_pass = make_password(pass1)
                user = User.objects.create(first_name = x[0], last_name = x[1], is_active = False, username = request.POST['email'], email = request.POST['email'], password = has_pass)
                otp = random.randint(100000, 999999)

                usr = User.objects.get(username = user_p)
                otp_save = Otp.objects.create(user = usr, Otp = otp)

                send_mail(
                    "Verify Your Email - Rohit's Library",
                    f"Your OTP is - {otp}",
                    'usisrojit@gmail.com',
                    [user_p],
                    fail_silently=False,
                )

                return render(request, 'index.html', {"otp": True, "user" : request.POST.get('email')})
            else:
                return render(request, 'index.html')


    else:

        if request.method == 'GET':
            get_otp = request.GET.get('ottp')
            user_enter_otp = request.GET.get('user_enter_otp')
            
            if get_otp is not None:
              
                get_user = User.objects.get(username = user_enter_otp)
                check_otp =  Otp.objects.filter(user = get_user).last().Otp

                if int(get_otp) == int(check_otp):
                    get_user.is_active = True
                    get_user.save()
                    return render(request, 'login.html', {"msg" : "Your Email Has Verified Successfuly!"})

                else:
                    return render(request, 'index.html', {"otp": True, "user" : user_enter_otp})
        else:      
            return render(request, 'index.html', {"otp": True, "user" : user_enter_otp})

        return render(request, 'index.html')


def loginpage(request):
    if request.method == "POST":
        uname = request.POST['email']
        pass1 = request.POST['pass']


        usr = User.objects.get(username = uname)
        print(usr.first_name)

        otp =  Otp.objects.filter(user = usr).last().Otp
        print(otp)

        if usr.is_active is False:
            send_mail(
                "Verify Your Email - Rohit's Library",
                f"Your OTP is - {otp}",
                'usisrojit@gmail.com',
                [uname],
                fail_silently=False,
            )
            return render(request, 'index.html', {"otp": True, "user" : uname, "msg" : "You Have Not Verify Your Email. We Sent OTP To Your Registered Email."})

        else:            
            c_user = authenticate(request, username=uname, password=pass1)

            if c_user is not None:
                login(request, c_user)
                request.session['user'] = uname
                return redirect("home")

            else:
                return render(request, 'login.html', {"msg" : "Invalid Login Details!"})

    return render(request, 'login.html')

def home(request):
    user = request.session.get('user')
    usr = User.objects.get(username = user)
    pic = Profile.objects.get(pro_user = usr).pro_img
    print(pic)
    video = VideosUpload.objects.all()
    if request.method == 'POST':
        fname = request.POST.get("firstName")
        lname = request.POST.get("lastName")
        pro_pic = request.POST.get("pic")
        title = request.POST.get("title")
        tags = request.POST.get("tags")
        thumb = request.FILES['tumb']
        videoFile = request.FILES['video']

        Vsave = VideosUpload.objects.create(vid_user = usr, firstName=fname, lastname=lname, pic=pro_pic,
                video_title=title, video_tags=tags, video=videoFile, video_tumb=thumb)
        Vsave.save()



    return render(request, 'home.html', {'pic' : pic, 'user' : usr, 'video' : video})
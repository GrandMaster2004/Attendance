from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .form import StudentForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import subOtp
from django.contrib.auth import get_user_model
User = get_user_model()
import random
from django.urls import reverse
import smtplib
import time
from .models import subOtp,cseData,itData,eceData
import pandas as pd
from django.http import JsonResponse
from geopy.distance import geodesic
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# file_path = 'path/to/your/file.txt'


    

def send_email_with_attachment(receiver_email, subject, content, file_path):
  sender_email = "eurekadigital6@gmail.com"
  password = "yags nldl objv doyv"
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = receiver_email
  message["Subject"] = subject

  # Attach the text content
  message.attach(MIMEText(content, "plain"))

  # Attach the file
  with open(file_path, "rb") as file:
    message.attach(MIMEApplication(file.read(), Name=file_path))

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(sender_email, password)
  server.sendmail(sender_email, receiver_email, message.as_string())
  server.quit()
  os.remove(file_path) #jfdslfjk this file remove


def calculate_displacement(coord1, coord2):
    """ Calculate the displacement between two points given their latitude and longitude coordinates. Args:
    coord1: Tuple containing latitude and longitude of the first point (lat1, lon1). coord2: Tuple containing
    latitude and longitude of the second point (lat2, lon2). Returns: Displacement in kilometers. """ 
    return geodesic(coord1, coord2).meters



def send_otp(email,otp):
    receiver_email = email
    sender_email = "eurekadigital6@gmail.com"
    # print(receiver_email)
    password = "yags nldl objv doyv"
    subject = str(otp)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,subject)

def send_file(email, data):
    # print(data)
    receiver_email = email
    sender_email = "eurekadigital6@gmail.com"
    # print(receiver_email)
    password = "yags nldl objv doyv"
    subject = str(data)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,subject)

def signup_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        # new_otp = random.randint(1000,9999)
        # form.otp = new_otp
        # print("sfddd ")
        if form.is_valid():
            form.save()
            # print("Send opt successfully")
            # url = "/otp_verify/?output={}".format(receiver_email)
            return redirect('/login_view')
    else:
        form = StudentForm()
  
    return render(request, './AttendanceApp/home.html', {'form':form})

def profile_view(request):
    if request.user.is_authenticated:
        # if request.user.is_
        if request.user.is_staff==False:
            otp = random.randint(1000,9999)
            email = request.user.email
            if(request.POST.get('otp1')==None):
                send_otp(email, otp)
            elif request.method=='POST':
                otp1 = request.POST.get('otp1')
                otp2 = request.POST.get('otp2')
                print(f"{otp1} and {otp2}")
                if(otp1==otp2):
                    request.user.is_staff = True
                    request.user.save()
                else:
                    send_otp(email, otp)
            return render(request, './AttendanceApp/profile.html',{'otp2':otp})
    else:
        # print("some thing wrong")
        return redirect('/logout_view')
    return render(request, './AttendanceApp/profile.html')

def login_view(request):
    if request.method=='POST':
        roll_no = request.POST['roll_no']
        password = request.POST['password']
        # print(roll_no)
        # print(password)
        user = auth.authenticate(roll_no=roll_no, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/profile_view')
        else:
            messages.info(request, "Invalid username and password")
            # print('unsuccessful login')
            return redirect('/login_view')
    return render(request, './AttendanceApp/login_form.html')
 
def logout_view(request):
    auth.logout(request)
    return request('/')


def data_view(request):
    if request.method == "POST":
        roll_no = request.POST.get('roll_no')
        branch = request.POST.get('branch').upper()
        section = request.POST.get('sec').upper()
        name = request.POST.get('name').upper()
        year = request.POST.get('year')
        code = request.POST.get('subCode').upper()
        otp = request.POST.get('otp')
        latitude = request.GET.get('londitude')
        longitude = request.GET.get('langitude')
        
        # now we need to verify location and otp
        if(branch=="CSE"):
            var = subOtp.objects.all()
            ind = False
            for one in var:
                if(one.otp==otp):
                    coord1 = (latitude, longitude) # Coordinates of 2
                    coord2 = (latitude, longitude) # Coordinates of 1
                    displacement = calculate_displacement(coord1, coord2)
                    print(f'{displacement} this is displacement ')
                    if(displacement<=20):
                        ind = True
                        break
            if(ind):
                cseObj = cseData()
                cseObj.roll_no = roll_no
                cseObj.branch = branch
                cseObj.section = section
                cseObj.student_name = name
                cseObj.year = year
                cseObj.subCode = code
                # filter this 
                cseObj.save()
                # print("Attendance save successfully")
            else:
                # print('something wrong')
                return redirect('/profile_view')
        elif(branch=="IT"):
            pass
        elif(branch=="ECE"):
            pass
        elif(branch=="MC"):
            pass
    return render(request, './AttendanceApp/profile.html')

def superUser_view(request):
    
    if request.method=='POST':
        sub_otp = random.randint(100000,999999)
        email = request.user.email
        if request.method == "POST":
            s = subOtp()
            londitude1 = request.POST.get('londitude')
            # print(londitude1)
            # print("DMMMMMMMMMMMMMMMMMMMMMMMMMM")
            langitude2 = request.POST.get('langitude')
            s.otp = sub_otp
            s.londitude = londitude1
            s.langitude = langitude2
            s.save()

        send_otp(email, sub_otp)
        # print("email send successfully")
        time.sleep(120)
        # print("Sleep time over")
        branch = request.POST.get('branch').upper()
        subCode = request.POST.get('subCode').upper()
        sec = request.POST.get('sec').upper()
        year = request.POST.get('year')
        # removeotp from object
        code = str(sub_otp)
        obj = subOtp.objects.filter(otp=code)
        obj.delete()
        # print("objext delete successfully")
        # today code for this subject
        # wait 5 min then process all data and delete one by one
        # print('5 min time is over')
        if(branch=="CSE"):
            # print("cse")
            objAll = cseData.objects.all()
            data = []
            for obj in objAll:
                print(f'{obj.year} and {year} {obj.section} {sec} {subCode} {obj.subCode} {obj.student_name} {obj.roll_no}')
                if((obj.year==int(year)) and (obj.section == sec) and (obj.subCode==subCode)):
                    print(f'{obj.subCode} and {obj.section} {obj.section}{obj.student_name} {obj.student_name}')
                    data.append({
                        "student_name":obj.student_name,
                        "roll_no":obj.roll_no,
                        "year":obj.year,
                        "branch":obj.branch,
                        "section":obj.section,
                        "subCode":obj.subCode,
                    })
                    obj.delete()
            
            print(data)
            send_file(email, data)
            file_path = f"output_{branch}_{sec}_{year}.xlsx"
            pd.DataFrame(data).to_excel(file_path, index=False)

            # #######################################
            receiver_email = email
            # sender_email = "eurekadigital6@gmail.com"
            # password = "yags nldl objv doyv"
            subject = "Email with attachment"
            content = "This is the content of the email."
            # Replace with the actual path to your file

            send_email_with_attachment(receiver_email, subject, content, file_path)
            # print("Email sent successfully!")

            return JsonResponse({
                'status':200
            })
        elif(branch=="IT"):
            pass
        elif(branch=="ECE"):
            pass
        elif(branch=="MC"):
            pass


        # delete waha pr karna ok buddy
        
        

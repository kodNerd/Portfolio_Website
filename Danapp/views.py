from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        
        send_mail(
            subject,  
            message,  
            email,  
            ['bencoder9@gmail.com'], 
        )
    return render(request, 'Danapp/index.html')

# def courses(request):
#     return render(request,'Home/courses.html')
# def events(request):
#     return render(request,'Home/events.html')
# def teacherProfile(request):
#     return render(request,'Home/teacherProfile.html')
# def blog(request):
#     return render(request,'Home/blog.html')
# def about(request):
#     return render(request,'Danapp/about.html')
# def login(request):
#     return render(request,'Home/login.html')

# def careers(request):
#     return render(request, 'Home/careers.html')
# def register(request):
#     if request.method == 'POST':
#         UserCred = request.POST['UserCred']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         fname=request.POST['fname']
#         if password2 == password:
#             if User.objects.filter(UserCred=UserCred).exists():
#                 messages.info(request,'User already registered')
#                 return redirect('Home/register.html')
#             if User.objects.filter(password=password).exists():
#                 messages.info(request,'Password too easy!') 
#                 return redirect('Home/register.html')
#             else:
#                 user = User.objects.create_user(password=password2,UserCred=UserCred) 
#                 user.save()
#                 return redirect('login.html')
#         elif password != password2:
#             messages.info(request,'Passwords did not match!')
#         else:
#             return redirect('Home/register.html')
#     return render(request, 'Home/register.html')
def portfolio_details(request):
    return render(request, 'Danapp/portfolio-details.html')
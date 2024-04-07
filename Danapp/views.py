from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'Danapp/index.html')

def portfolio_view(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}
        Message:\n\t\t{}\n
        Email:\n\t\t{}
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        send_mail('You got a mail Ben!', message, '', ['bencoder9@gmail.com']) # TODO: enter your email address
        
    return render(request, 'Danapp/success.html', {})
def contact(request):
    return render(request,'Danapp/contact.html')
def portfolio_details(request):
    return render(request, 'Danapp/portfolio-details.html')
def about(request):
    return render(request,'Danapp/about.html')
def portfolio(request):
    return render(request,'Danapp/portfolio.html')
def resume(request):
    return render(request, 'Danapp/resume.html')
def services(request):
    return render(request, 'Danapp/services.html')
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import  send_mail,EmailMessage
from django.template.loader import get_template
from django.conf import settings
from .models import Room,Review,feedback
from .forms import feedbackForm


from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.decorators import login_required


def home(request):
    rooms=Room.objects.all()
    reviews=Review.objects.all()
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            feedback_name = request.POST.get('feedback_name')
            feedback_email = request.POST.get('feedback_email')
            feedback = request.POST.get('feedback')
            template = get_template('contact/feedback.txt')
            context = {'feedback_name' : feedback_name,'feedback_email' : feedback_email,'feedback' : feedback,}
            content = template.render(context)
            email = EmailMessage("Ekam Feedback",content,"Ekam villas",['prajapatideepak244@gmail.com'],
            headers = { 'Reply To': feedback_email })
            email.send()
            form.save()
            return redirect('home')
    else:
        form = feedbackForm()
        context = {'rooms':rooms,'reviews':reviews,'form':form}
    return render(request, 'home/home.html',context)

def room(request):
    return render(request, 'room/room.html')

def contact(request):
    return render(request, 'contact/contact.html')

def about(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            feedback_name = request.POST.get('feedback_name')
            feedback_email = request.POST.get('feedback_email')
            feedback = request.POST.get('feedback')
            template = get_template('contact/feedback.txt')
            context = {'feedback_name' : feedback_name,'feedback_email' : feedback_email,'feedback' : feedback,}
            content = template.render(context)
            email = EmailMessage("Ekam Feedback",content,"Ekam villas",['prajapatideepak244@gmail.com'],
            headers = { 'Reply To': feedback_email })
            email.send()
            form.save()
            return redirect('about')
    else:
        form = feedbackForm()
        context = {'form':form}
    return render(request, 'about/about.html')

def facilities(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            feedback_name = request.POST.get('feedback_name')
            feedback_email = request.POST.get('feedback_email')
            feedback = request.POST.get('feedback')
            template = get_template('contact/feedback.txt')
            context = {'feedback_name' : feedback_name,'feedback_email' : feedback_email,'feedback' : feedback,}
            content = template.render(context)
            email = EmailMessage("Ekam Feedback",content,"Ekam villas",['prajapatideepak244@gmail.com'],
            headers = { 'Reply To': feedback_email })
            email.send()
            form.save()
            return redirect('facilities')
    else:
        form = feedbackForm()
        context = {'form':form}
    return render(request, 'facilities/facilities.html')
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import  send_mail,EmailMessage
from django.template.loader import get_template
from hotel.models import feedback
from hotel.forms import feedbackForm
from .models import Room

# Create your views here.

def rooms(request):
    rooms=Room.objects.all()
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
            return redirect('room')
    else:
        form = feedbackForm()
        context = {'rooms':rooms,'form':form}
    return render (request,'room/room.html',context)
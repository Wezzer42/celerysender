from django.shortcuts import render, redirect
from .forms import EmailForm
from .tasks import send_email_task

def email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_email_task.delay(email, subject, message)
            return render(request, 'emailer/success.html')
    else:
        form = EmailForm()
    return render(request, 'emailer/email_form.html', {'form': form})

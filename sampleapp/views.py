from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

from .form import MailForm
import sendgrid


def index(request):
    if request.method == 'POST':

        form = MailForm(request.POST)
        if form.is_valid():
            from_mail = form.cleaned_data['from_mail']
            to_mail = form.cleaned_data['to_mail']
            subject_mail = form.cleaned_data['subject_mail']
            content_mail = form.cleaned_data['content_mail']

            sg = sendgrid.SendGridClient(
                settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            message = sendgrid.Mail()
            message.set_from(from_mail)
            message.add_to(to_mail)
            message.set_subject(subject_mail)
            message.set_html(content_mail)
            message.set_text(content_mail)

            status, msg = sg.send(message)

            if status == 200:
                messages.success(request, 'Your email was successfully sent.')
            else:
                messages.error(request, msg)
    else:
        form = MailForm()

    return render(request, 'index.html', {
        'form': form,
    })

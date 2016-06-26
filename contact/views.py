from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['email'])
        subject = "Message from djangostripe.com"
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        message = "{}{}".format(comment,name)
        email_from = form.cleaned_data['email']
        email_to = ["violetstd002@gmail.com"]
        send_mail(
            subject,
            message,
            email_from,
            [email_to],
            fail_silently=False,
        )
    context = locals()
    template = 'contact.html'
    return render(request, template, context)
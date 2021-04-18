from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


def send_mail(request):

    form_class = ContactForm
    if request.method == "POST":
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name',
                ''
            )
            contact_email = request.POST.get(
                'contact_email',
                '',
            )
            subject = request.POST.get(
                'subject',
                ''
            )
            content = request.POST.get(
                'content',
                ''
            )
            template = get_template('contact/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'subject': subject,
                'form_content': content,
            }
            content = template.render(context)
            email = EmailMessage(
                    "New contact form submission",
                    content,
                    contact_email +'',
                    ['innomightmail@gmail.com'],
                    headers={'Reply-To': contact_email}
                )
            email.send()
            return redirect('contact')

    return render(request, "contact/contact_form.html", {'form': form_class})

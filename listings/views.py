from django.shortcuts import render
from listings.models import Project
from listings.models import Language
from listings.models import Framework
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def portfolio(request):
    projects = Project.objects.all()
    languages = Language.objects.all()
    frameworks = Framework.objects.all() 

    #Partie contact
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["nom"]} via Portfolio Contact Me form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['saad.rafiqul1@gmail.com'],
        )
            return redirect('portfolio')
    else:
        form = ContactUsForm()

    return render(request, 'listings/index.html', {'projects': projects, 'languages': languages, 'frameworks': frameworks, 'form': form})


def project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'listings/project.html', {'project': project})
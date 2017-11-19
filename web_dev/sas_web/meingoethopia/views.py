from django.shortcuts import render
from django import forms
from captcha.fields import CaptchaField
from .models import Betrieb, Partei, PresidentCandidate, Question


class BetriebForm(forms.Form):
    name = forms.CharField(label='Name des Betriebs', max_length=100)
    manager = forms.CharField(label='Betriebsleiter', max_length=200)
    email = forms.EmailField(label='Kontakt Email')
    business_idea = forms.CharField(label='Idee')
    captcha = CaptchaField()


class ParteiForm(forms.Form):
    name = forms.CharField(label='Name der Partei', max_length=100)
    abbreviation = forms.CharField(label='Abkürzung', max_length=5)
    chef = forms.CharField(label='Parteivorsitzende', max_length=200)
    email = forms.EmailField(label='Kontakt Email')
    description = forms.CharField(label='Beschreibung')
    captcha = CaptchaField()


class PresidentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Kontakt Email')
    motivation = forms.CharField(label='Motivation')
    captcha = CaptchaField()


class QuestionForm(forms.Form):
    subject = forms.CharField(label='Thema', max_length=100)
    email = forms.EmailField(label='Kontakt Email')
    content = forms.CharField(label='Frage')
    captcha = CaptchaField()


# Create your views here.
def index(request):
    return render(request, "meingoethopia/index.html")


def betrieb_new(request):
    if request.method == 'POST':
        form = BetriebForm(request.POST)
        if form.is_valid():
            betrieb = Betrieb(name=form.cleaned_data.get('name'),
                              manager=form.cleaned_data.get('manager'),
                              email=form.cleaned_data.get('email'),
                              business_idea=form.cleaned_data.get('business_idea'),
                              ip_address=get_client_ip(request),
                              confirmed=False)
            betrieb.save()
            return render_confirmation(request)
    else:
        form = BetriebForm()
    return render(request, "meingoethopia/betrieb_new.html", {'form': form})


def partei_new(request):
    if request.method == 'POST':
        form = ParteiForm(request.POST)
        if form.is_valid():
            partei = Partei(name=form.cleaned_data.get('name'),
                            abbreviation=form.cleaned_data.get('abbreviation'),
                            chef=form.cleaned_data.get('chef'),
                            email=form.cleaned_data.get('email'),
                            description=form.cleaned_data.get('description'),
                            confirmed=False)
            partei.save()
            return render_confirmation(request)
    else:
        form = ParteiForm()
    return render(request, "meingoethopia/partei_new.html", {'form': form})


def praesident_werden(request):
    if request.method == 'POST':
        form = PresidentForm(request.POST)
        if form.is_valid():
            president = PresidentCandidate(name=form.cleaned_data.get('name'),
                                           email=form.cleaned_data.get('email'),
                                           motivation=form.cleaned_data.get('motivation'),
                                           confirmed=False)
            president.save()
            return render_confirmation(request)
    else:
        form = PresidentForm()
    return render(request, "meingoethopia/president.html", {'form': form})


def question_new(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question(subject=form.cleaned_data.get('subject'),
                                email=form.cleaned_data.get('email'),
                                content=form.cleaned_data.get('content'),
                                answered=False)
            question.save()
            return render_confirmation(request)
    else:
        form = QuestionForm()
    return render(request, "meingoethopia/question_new.html", {'form': form})


def render_confirmation(request):
    return render(request, "meingoethopia/confirmed.html")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

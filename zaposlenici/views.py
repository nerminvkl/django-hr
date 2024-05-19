from django.shortcuts import render
from .models import Zaposleni
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ZaposleniForm
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, 'zaposlenici/index.html', {
        'zaposleni': Zaposleni.objects.all()
    })
    
def info(request):
    return render(request, 'zaposlenici/info.html', {
    })

def kabinet(request):
    return render(request, 'zaposlenici/kabinet.html', {
    })
    
def opca_uprava(request):
    return render(request, 'zaposlenici/opca_uprava.html', {
    })
    
def view_zaposlenik(request, id):
    zaposlenik = Zaposleni.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def dodaj(request):
    if request.method == 'POST':
       form = ZaposleniForm(request.POST)
       if form.is_valid():
           novi_sifra_zaposlenog = form.cleaned_data['sifra_zaposlenog']
           novi_ime = form.cleaned_data['ime']
           novi_prezime = form.cleaned_data['prezime']
           novi_email = form.cleaned_data['email']
           novi_strucna_sprema = form.cleaned_data['strucna_sprema']
           novi_ocjena_zaposlenog = form.cleaned_data['ocjena_zaposlenog']
           
           novi_zaposleni = Zaposleni(
               sifra_zaposlenog = novi_sifra_zaposlenog,
               ime = novi_ime,
               prezime = novi_prezime,
               email = novi_email,
               strucna_sprema = novi_strucna_sprema,
               ocjena_zaposlenog = novi_ocjena_zaposlenog
           )
           
           novi_zaposleni.save()
           return render(request, 'zaposlenici/dodaj.html', {
               'form': ZaposleniForm(),
               'success': True
           })
    else:
           form = ZaposleniForm()
           return render(request, 'zaposlenici/dodaj.html', {
               'form': ZaposleniForm()
           })
           
def uredi(request, id):
    if request.method == 'POST':
        zaposlenik = Zaposleni.objects.get(pk=id)
        form = ZaposleniForm(request.POST, instance=zaposlenik)
        if form.is_valid():
            form.save()
            return render(request, 'zaposlenici/uredi.html', {
                'form': form,
                'success': True
            })
    else:
        zaposlenik = Zaposleni.objects.get(pk=id)
        form = ZaposleniForm(instance=zaposlenik)
        return render(request, 'zaposlenici/uredi.html', {
            'form': form
        })
        
def obrisi(request, id):
    if request.method == 'POST':
        zaposlenik = Zaposleni.objects.get(pk=id)
        zaposlenik.delete()
    return HttpResponseRedirect(reverse('index'))

def pretraga(request):
    if request.method == 'POST':
        trazeno = request.POST['pretraga']
        zaposleni = Zaposleni.objects.filter(Q(ime__contains=trazeno) | Q(prezime__contains=trazeno))
        return render(request, 'zaposlenici/pretraga.html', {
            'trazeno': trazeno,
            'zaposleni': zaposleni
        })
    else:
        return render(request, 'zaposlenici/pretraga.html', {
       
        })
    
        

                  
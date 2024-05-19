from django import forms
from .models import Zaposleni

class ZaposleniForm(forms.ModelForm):
    class Meta:
        model = Zaposleni
        fields = ['sifra_zaposlenog','ime','prezime','email','strucna_sprema','ocjena_zaposlenog']
        labels = {
            'sifra_zaposlenog': 'Šifra zaposlenog',
            'ime': 'Ime',
            'prezime': 'Prezime',
            'email': 'E-mail',
            'strucna_sprema': 'Stručna sprema',
            'ocjena_zaposlenog': 'Ocjena',
        }
        widgets = {
            'sifra_zaposlenog': forms.NumberInput(attrs={'class':'form-control'}),
            'ime': forms.TextInput(attrs={'class':'form-control'}),
            'prezime': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'strucna_sprema': forms.TextInput(attrs={'class':'form-control'}),
            'ocjena_zaposlenog': forms.NumberInput(attrs={'class':'form-control'}),
        }
from django.db import models


class Zaposleni(models.Model):
    sifra_zaposlenog = models.PositiveIntegerField()
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    strucna_sprema = models.CharField(max_length=100)
    ocjena_zaposlenog = models.FloatField()
    
    def __str__(self):
        return f'Zaposleni: {self.ime} {self.prezime}'

    class Meta:
        verbose_name_plural = "Zaposleni"
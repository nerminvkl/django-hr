# Generated by Django 4.2.7 on 2023-12-09 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zaposlenici', '0002_alter_zaposleni_options_zaposleni_datum_rodjenja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaposleni',
            name='datum_rodjenja',
        ),
    ]

from django.db import models



class Author(models.Model):

    COLOMBIA = 'CO'
    ECUADOR = 'EC'
    VENEZUELA = 'VE'

    COUNTRY_CHOICES = [
        (COLOMBIA, 'Colombia'),
        (ECUADOR, 'Ecuador'),
        (VENEZUELA, 'Venezuela')
    ]

    name = models.CharField(max_length=60, verbose_name='Nombre', unique=True) 
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, verbose_name='Pais de nacimiento')
    age = models.PositiveIntegerField(verbose_name='edad')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'







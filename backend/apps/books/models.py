from django.db import models

from apps.author.models import Author



class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author')
    year_edition = models.DateField(verbose_name='año de edicion')
    number_pages = models.PositiveIntegerField(verbose_name='Numero de paginas')
    language = models.CharField(max_length=50, verbose_name='Idioma')
    editorial = models.CharField(max_length=255, verbose_name='Editorial')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
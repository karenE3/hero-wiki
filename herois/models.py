from django.db import models

# Create your models here.


class Universo(models.Model):
    nome = models.CharField(max_length=255)


class Heroi(models.Model):
    nome = models.CharField(
        max_length=255
    )
    idade = models.IntegerField(
        max_length=255
    )
    universo = models.CharField(
        max_length=255
    )
    habilidade = models.CharField(
        max_length=255
    )
    categoria_heroi = models.CharField(
        max_length=255
    )


class Habilidade(models.Model):
    nome = models.CharField(
        max_length=255
    )
    nivel_hab = models.CharField(
        max_length=255
    )

class Categoria

    nivel_habilidade = models.IntegerField()
    hab_heroi = models.ManyToManyField(Heroi, related_name='habilidade')


    universo = models.ForeignKey(Universo, on_delete=models.CASCADE)
    heroi = models.ForeignKey(Heroi, on_delete=models.CASCADE)

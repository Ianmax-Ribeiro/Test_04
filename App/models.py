from django.db import models


class test01(models.Model):
    nome = models.CharField(
        max_length=30,
    )


class test02(models.Model):
    idade = models.CharField(
        max_length=30,
    )

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Visit(models.Model):
    """
    Modelo para almacenar contactos de damnificados
    """

    nombre       = models.CharField(max_length=100)

    creado       = models.DateTimeField(auto_now_add = True)
    modificado   = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "%s" % (self.nombre)

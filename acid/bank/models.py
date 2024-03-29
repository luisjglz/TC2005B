#https://pastebin.com/wDguk119
# bank/models.py
from django.db import models

class cliente(models.Model):
  nombre = models.CharField(max_length=50)
  saldo = models.DecimalField(max_digits=5, decimal_places=2)
  creado = models.DateTimeField(auto_now_add=True)
  modificado = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.nombre
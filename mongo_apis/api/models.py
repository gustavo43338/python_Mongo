# from django.db import models
from mongoengine import Document, StringField, IntField, DateTimeField
# Create your models here.

class Halo(Document):
    nombre = StringField()
    marca = StringField()
    stock = IntField()
    precio = StringField()
    cducidad = DateTimeField()
    lote = DateTimeField()
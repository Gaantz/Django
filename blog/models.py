from django.db import models
from django.conf import settings

class Tienda(models.Model):
    TIPO_TIENDA = (('mujer', 'MUJER'), ('hombre', 'HOMBRE'), ('mixta', 'MIXTA'))

    class Meta:
        db_table = 'Tienda'

    name = models.CharField(max_length=20)
    ruc = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_TIENDA, default='--ELIJA--')
    imagen = models.ImageField(upload_to='Tiendas')

    def __str__(self):
        return self.name

class Ropa(models.Model):
    TALLA_ROPA = (('xl', 'XL'), ('l', 'L'), ('m', 'M'), ('s', 'S'))

    class Meta:
        db_table = 'Ropa'

    tienda = models.ForeignKey('Tienda')
    name = models.CharField(max_length=50)
    talla = models.CharField(max_length=5, choices=TALLA_ROPA, default='--ELIJA--')
    descripcion = models.TextField(max_length=100);
    imagen = models.ImageField(upload_to='Ropas')

    def __str__(self):
        return self.name

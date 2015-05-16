from django.db import models


class Tienda(models.Model):
    TIPO_TIENDA = (('MUJER', 'mujer'), ('HOMBRE', 'hombre'), ('MIXTA', 'mixto'))

    class Meta:
        db_table = 'Tienda'

    name = models.CharField(max_length=20)
    ruc = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_TIENDA, default='--ELIJA--')
    latitud = models.DecimalField(decimal_places=5, max_digits=10)
    longitud = models.DecimalField(decimal_places=5, max_digits=10)
    imagen = models.ImageField()


class Ropa(models.Model):
    TALLA_ROPA = (('XL', 'xl'), ('L', 'l'), ('M', 'm'),('S', 's'))
    class Meta:
        db_table = 'Ropa'

    tienda = models.ForeignKey('Tienda')
    name = models.CharField(max_length=50)
    talla = models.CharField(max_length=5, choices=TALLA_ROPA, default='--ELIJA--')
    descripcion = models.TextField(max_length=100);
    imagen = models.ImageField()

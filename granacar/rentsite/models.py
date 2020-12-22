from django.db import models

class Factura(models.Model):
    #Hay que fijar en el formulario que la longitud mínima sea tmb 5, el id siempre tiene longitud 5
    id=models.CharField(max_length=5, primary_key=True)
    fecha=models.DateField()
    proveedor=models.CharField(max_length=50,blank=True,null=True)
    total=models.DecimalField("Precio total",max_digits=5,decimal_places=2)

    def __str__(self):
        return "Factura " + self.id + " con fecha " + '{}'.format(self.fecha)


class InformeContable(models.Model):
    id=models.CharField(max_length=5, primary_key=True)
    fecha=models.DateField("Fecha de realización del informe")

    def __str__(self):
        return "Informe " + self.id + " con fecha " + '{}'.format(self.fecha)

    class Meta:
	    verbose_name_plural ="InformesContables"

class Bien(models.Model):
    #falta poner el id del informe que va asociado a este, pero no sé como hacerlo y ambos ids son la clave primaria
    id=models.CharField(max_length=5, primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True,max_length=200,null=True)
    valor=models.DecimalField(max_digits=8,decimal_places=2)
    informe=models.ForeignKey(InformeContable,on_delete=models.CASCADE)

    def __str__(self):
        return "Bien: " + self.nombre + " con identificador: " + self.id + " asociado al informe: " + '{}'.format(self.informe.id)

    class Meta:
	    verbose_name_plural ="bienes"


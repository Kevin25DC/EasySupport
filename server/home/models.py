from django.db import models
from django.utils import timezone
import uuid

class Roles(models.Model):
    ADMINISTRATOR = 'admin'
    STANDARD = 'estandar'
    TIPO_CHOICES = [
        (ADMINISTRATOR, 'Administrador'),
        (STANDARD, 'Estándar'),
    ]

    id = models.BigAutoField(primary_key=True, null=False)
    Type = models.CharField(max_length=10, choices=TIPO_CHOICES, verbose_name="Tipo de rol")
    creation_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

    def save(self, *args, **kwargs):
        # Si el objeto no tiene una fecha de creación establecida, se establecerá la fecha actual
        if not self.fecha_creacion:
            self.fecha_creacion = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo}"
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
    
class User(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    Username = models.TextField(max_length =250) 
    Name = models.CharField(max_length= 200, verbose_name="Nombre")
    lastName = models.CharField(max_length= 200, verbose_name="Apellido")
    citizenshipCard = models.IntegerField(verbose_name = "Cedula de ciudadania")
    Email = models.EmailField(null=True)
    Phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    roles = models.ForeignKey(Roles, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.Username}"
    
class Tikest(models.Model):
    Title = models.TextField(max_length=200, verbose_name="titulo")
    Description = models.TextField(max_length=200, verbose_name="descripcion")
    State = models.BooleanField(default=False)
    Creation_Date = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Title}"

class History(models.Model):
    title = models.ForeignKey(Tikest, on_delete=models.CASCADE)
    action = models.CharField(max_length=250, verbose_name="Accion")
    Date = models.DateField(auto_now_add=True)
    Username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    
    def __str__(self) -> str:   
        return f"{self.title},{self.Date}"


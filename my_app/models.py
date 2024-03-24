from django.db import models

# Create your models here.


class RiceviRequest(models.Model):
    nome = models.CharField(max_length=20)

    cognome = models.CharField(max_length=20)

    email = models.EmailField()

    contenuto = models.TextField()

    def __str__(self):
        return f"{self.nome} {self.cognome} {self.email} {self.contenuto}"



class TracciaDB(models.Model):
    name                = models.CharField(max_length = 100)
    ip                  = models.CharField(max_length = 100)
    timestamp           = models.CharField(max_length = 100)
    normalTime          = models.CharField(max_length = 100)
    name                = models.CharField(max_length = 100)
    operative_system    = models.CharField(max_length = 100)
    page_name           = models.CharField(max_length = 100, default = "impossibile identificare page") # il default è perchè questa colonna l'ho aggiunta dopo 
    city                = models.CharField(max_length = 100, default = "impossibile identificare la citta")
    region              = models.CharField(max_length = 100, default = "impossibile identificare la regione")
    country             = models.CharField(max_length = 100, default = "impossibile identificare il paese")
    type_method         = models.CharField(max_length = 100, default = "impossibile identificare il metodo di richiesta")

    def __str__(self) -> str:
        return f"{self.name} {self.ip} {self.timestamp} {self.normalTime} {self.page_name} {self.city} {self.region} {self.country}"

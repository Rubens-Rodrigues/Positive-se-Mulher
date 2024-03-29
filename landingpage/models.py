from django.db import models

TITLE_CHOICES = {
    "Landing Page": "Landing Page",
    "Portal admin": "Portal admin"
}

class LeadsForm(models.Model):
    nome=models.CharField(max_length=100, null=False, blank=False)
    email=models.EmailField(max_length=200, null=False, unique=True, blank=False, verbose_name="E-mail")
    phone=models.CharField(max_length=16, blank=False, verbose_name="Celular")
    date_created=models.DateField(auto_now=True, verbose_name="Data de cadastro")
    leadsource=models.CharField(max_length=20,verbose_name="Origem cadastro", choices=TITLE_CHOICES)

    def __str__(self) -> str:
        return self.nome

class PreInscricao(models.Model):
    nome=models.CharField(max_length=50, null=False, blank=False)
    telefone=models.CharField(max_length=15, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.nome
from django.db import models

class cadProcesso(models.Model):

    nome = models.CharField(max_length=150)
    cliente = models.CharField(max_length=150)
    arquivo = models.FileField(upload_to='processo/')
    enviado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
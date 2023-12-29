from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    altura = models.FloatField()
    peso = models.FloatField()
    def __str__(self) -> str:
        return self.nome

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    crm = models.CharField(max_length=5, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    
    def __str__(self) -> str:
        return self.nome

class Atendimento(models.Model):
    data_hora = models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional_saude = models.ForeignKey(Profissional, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('data_hora', 'paciente', 'profissional_saude')
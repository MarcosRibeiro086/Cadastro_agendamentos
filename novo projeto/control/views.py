from django import forms
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect,render
from django.shortcuts import render, redirect
from .models import Atendimento, Paciente, Profissional


def home(request):
    return  render(request,'control/home.html')
# paciente
class PacListView(ListView):
    model = Paciente
    template_name = 'control/paciente/paciente_list.html' 
#cadasto
class PacCreateView(CreateView):
    model=Paciente
    template_name = 'control/paciente/paciente_form.html' 
    fields =[ "nome","cpf", "data_nascimento","sexo", "altura", "peso"]

    success_url= reverse_lazy ("paciente_list")
#atualização
class PacUpdateView(UpdateView):
    model =Paciente
    template_name = 'control/paciente/paciente_form.html' 
    fields =[ "nome","cpf", "data_nascimento","sexo", "altura", "peso"]
    success_url=reverse_lazy ("paciente_list")
#delete
class PacDeleteView(DeleteView):
    model=Paciente
    template_name = 'control/paciente/paciente_confirm_delete.html'
    success_url = reverse_lazy("paciente_list")

# profissional de saúde

class ProListView(ListView):
    model =Profissional
    template_name = 'control/profissional/profissional_list.html' 
#cadasto
class ProCreateView(CreateView):
    model=Profissional
    template_name = 'control/profissional/profissional_form.html'   
    fields =[ "nome","cpf","crm", "data_nascimento","sexo"]
    success_url= reverse_lazy ("profissional_list")
#atualização
class ProUpdateView(UpdateView):
    model =Profissional   
    template_name = 'control/profissional/profissional_form.html'  
    fields =[ "nome","cpf","crm", "data_nascimento","sexo"]
    success_url=reverse_lazy ("profissional_list")
#delete
class ProDeleteView(DeleteView):
    template_name = 'control/profissional/profissional_confirm_delete.html'
    model=Profissional
    success_url = reverse_lazy("profissional_list")

# atendimento
class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ["data_hora", "paciente", "profissional_saude"]

    def clean(self):
        cleaned_data = super().clean()
        data_hora = cleaned_data.get("data_hora")
        profissional_saude = cleaned_data.get("profissional_saude")

        # Verifica se já existe um agendamento para o mesmo médico na mesma data/hora
        agendamentos_conflitantes = Atendimento.objects.filter(
            data_hora=data_hora, profissional_saude=profissional_saude
        )

        if agendamentos_conflitantes.exists():
            msg = "Este médico já possui um agendamento para esta data/hora."
            self.add_error("data_hora", msg)
            self.add_error("profissional_saude", msg)

        return cleaned_data

class AtListView(ListView):
    model =Atendimento
    template_name = 'control/atendimento/atendimento_list.html'  
#cadasto


class AtCreateView(CreateView):
    model=Atendimento
    form_class = AtendimentoForm
    template_name = 'control/atendimento/atendimento_form.html'  
    success_url= reverse_lazy ("atendimento_list")


#atualização
class AtUpdateView(UpdateView):
    model =Atendimento
    template_name = 'control/atendimento/atendimento_form.html'  
    fields =[ "data_hora","paciente","profissional_saude"]
    success_url=reverse_lazy ("atendimento_list")
#delete
class AtDeleteView(DeleteView):
    model=Atendimento
    template_name = 'control/atendimento/atendimento_confirm_delete.html'
    success_url = reverse_lazy("atendimento_list")

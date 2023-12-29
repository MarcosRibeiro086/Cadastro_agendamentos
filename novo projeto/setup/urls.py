"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path, include
from control import views
from control.views import PacListView,PacCreateView,PacDeleteView,PacUpdateView,ProListView,ProCreateView,ProDeleteView,ProUpdateView,AtListView,AtCreateView,AtDeleteView,AtUpdateView

urlpatterns = [

    path("",views.home,name="home"),
    path("home",views.home,name="home1"),
    path("paciente_list",PacListView.as_view(),name="paciente_list"),
    path("paciente_create",PacCreateView.as_view(), name="paciente_create"),
    path("paciente_delete/<int:pk>",PacDeleteView.as_view(), name="paciente_delete"),
    path("paciente_update/<int:pk>",PacUpdateView.as_view(), name="paciente_update"),
    path("profissional_list",ProListView.as_view(),name="profissional_list"),
    path("profissional_create",ProCreateView.as_view(), name="profissional_create"),
    path("profissional_delete/<int:pk>",ProDeleteView.as_view(), name="profissional_delete"),
    path("profissional_update/<int:pk>",ProUpdateView.as_view(), name="profissional_update"),
    path("atendimento_list",AtListView.as_view(),name="atendimento_list"),
    path("atendimento_create", AtCreateView.as_view(), name="atendimento_create"),
    path("atendimento_delete/<int:pk>",AtDeleteView.as_view(), name="atendimento_delete"),
    path("atendimento_update/<int:pk>",AtUpdateView.as_view(), name="atendimento_update"),
]

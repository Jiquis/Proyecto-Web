from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views

from .models import Usuario

# Create your views here.
class Index(generic.View):
    template_name = "Principal/index.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "Usuario": Usuario.objects.all() 
        }
        return render(request, self.template_name, self.context)

class DetailUsuario(generic.View):
    template_name = "Principal/detail_usuarios.html"
    context = {}

    def get(self, request, pk, *args, **kwargs):
        self.context = {
            "Usuario": Usuario.objects.get(pk=pk)
        }
        return render(request, self.template_name, self.context)

def login(request):
    context = {
        
    }
    return render(request, "Htmls/login.html", context)

def Apuestas(request):
    context = {
        
    }
    return render(request, "Htmls/apuestas.html", context)

def Payment(request):
    context = {
        
    }
    return render(request, "Htmls/PaymentM.html", context)

def Paybet(request):
    context = {
        
    }
    return render(request, "Htmls/PayBet.html", context)

def ProfileSet(request):
    context = {
        
    }
    return render(request, "Htmls/profilesettings.html", context)

def ProfileView(request):
    context = {
        
    }
    return render(request, "Htmls/ProfileView.html", context)

def TablaOpciones(request):
    context = {
        
    }
    return render(request, "Htmls/tabladeopciones.html", context)

def Register(request):
    context = {
        
    }
    return render(request, "Htmls/register.html", context)

def Problems(request):
    context = {
        
    }
    return render(request, "Htmls/Problems.html", context)
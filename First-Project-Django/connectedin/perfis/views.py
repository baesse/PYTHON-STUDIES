from django.shortcuts import render,redirect
from perfis.models import Perfil


def index (request):  
   return render(request,'index.html',{'users':Perfil.objects.all()})

def show(request, perfil_id):   
    perfil=Perfil.objects.get(id=perfil_id)    
    return render(request,'perfil.html',{"perfil":perfil})

def invite(request, perfil_id):   
    perfil_invite =Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.invite(perfil_invite)
    return redirect('index')
def get_perfil_logado(request):
    return Perfil.objects.get(id=1)


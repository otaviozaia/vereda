from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from core.models import User,Aluno,Professor,Assistente
import random
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
import vereda.settings

def index(request):
    return render(request,'index.html')

def detalhedisciplina(request):
    return render(request,'detalhedisciplina.html')

def disciplinasAno(request):
    return render(request,'disciplinasAno.html')

def matricula(request):
    return render(request,'matricula.html')

def novaDisciplina(request):
    return render(request,'novaDisciplina.html')

def novoAno(request):
    return render(request,'novoAno.html')

def getAnos(request):
    return render(request,'anos.html')

def novaHabilidade(request):
    return render(request,'novaHabilidade.html')

def getHabilidades(request):
    return render(request,'habilidades.html')

def novaTurma(request):
    return render(request,'novaTurma.html')

def getTurmas(request):
    return render(request,'turmas.html')


def NovoAluno(request):
    User = request.user
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        if request.method == "GET":
            return render (request,"NovoAluno.html")
        else:
            username = request.POST.get("login")
            password = str(random.randrange(10**6,(10**7)-1,1))+random.choice('abcd')
            name = request.POST.get("nome")
            email = request.POST.get("email")
            celular = request.POST.get("celular")
            turma = request.POST.get("turma")
            ra = request.POST.get("ra")
            tipo = "A"
            Aluno.objects.create_user(username = username,password = password,name = name,email= email,celular = celular,turma = turma,ra = ra,tipo = tipo)
            user = authenticate(username=username,password=password)
            login(request, user)
            return render(request,"first_edit_senha.html")

def NovoCoordenador(request):
    Usuario = request.user
    if Usuario.is_authenticated:
        return render(request,"index.html")
    else:
        if request.method == "GET":
            return render (request,"NovoCoordenador.html")
        else:
            username = request.POST.get("login")
            password = str(random.randrange(10**6,(10**7)-1,1))+random.choice('abcd')
            name = request.POST.get("nome")
            email = request.POST.get("email")
            celular = request.POST.get("celular")
            User.objects.create_user(username = username,password = password,name = name,email= email,celular = celular)
            user = authenticate(username=username,password=password)
            login(request, user)
            return render(request,"first_edit_senha.html")

def NovoProfessor(request):
    User = request.user
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        if request.method == "GET":
            return render (request,"NovoProfessor.html")
        else:
            username = request.POST.get("login")
            password = str(random.randrange(10**6,(10**7)-1,1))+random.choice('abcd')
            name = request.POST.get("nome")
            email = request.POST.get("email")
            celular = request.POST.get("celular")
            ano = request.POST.get("ano")
            Professor.objects.create_user(username = username,password = password,name = name,email= email,celular = celular,tipo = "P",ano = ano)
            user = authenticate(username=username,password=password)
            login(request, user)
            return render(request,"first_edit_senha.html")

def NovoAssistente(request):
    User = request.user
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        if request.method == "GET":
            return render (request,"NovoAssistente.html")
        else:
            username = request.POST.get("login")
            password = str(random.randrange(10**6,(10**7)-1,1))+random.choice('abcd')
            name = request.POST.get("nome")
            email = request.POST.get("email")
            celular = request.POST.get("celular")
            ano = request.POST.get("ano")
            Assistente.objects.create_user(username = username,password = password,name = name,email= email,celular = celular,tipo = "S",ano = ano)
            user = authenticate(username=username,password=password)
            login(request, user)
            return render(request,"first_edit_senha.html")


def recover(request):
    User = request.user
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        return render(request,'recover.html')



def teste_coordenador(user):
    return user.tipo == 'C'

def teste_aluno(user):
    return user.tipo == 'A'

def teste_professor(user):
    return user.tipo == 'P'

def teste_assistente(user):
    return user.tipo == 'S'
    
@login_required(login_url='/core/login')
@user_passes_test(teste_coordenador,login_url='/core/index',redirect_field_name=None)
def areaUser(request):
    return render(request,"areaUser.html")


@login_required(login_url='/core/login')
@user_passes_test(teste_aluno,login_url='/core/index',redirect_field_name=None)
def areaAluno(request):
    return render(request,"areaAluno.html")


@login_required(login_url='/core/login')
@user_passes_test(teste_professor,login_url='/core/index',redirect_field_name=None)
def areaProfessor(request):
    return render(request,"areaProfessor.html")

@login_required(login_url='/core/login')
@user_passes_test(teste_assistente,login_url='/core/index',redirect_field_name=None)
def areaAssistente(request):
    return render(request,"areaAssistente.html")

@login_required(login_url='/core/index')
def first_edit_senha(request):
    if request.method == "GET":
        return render(request,"first_edit_senha.html")
    else:
        Usuario = request.user
        new_password = request.POST.get("novasenha")
        confirm_senha = request.POST.get("confirmsenha")
        if new_password == confirm_senha:
            Usuario.set_password(new_password)
            Usuario.save()
            return render(request,"index.html")
        else:
            return render(request,"first_edit_senha.html")



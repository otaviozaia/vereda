from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('detalhedisciplina/',detalhedisciplina, name='detalhedisciplina'),
    path('disciplinasAno/',disciplinasAno, name='disciplinasAno'),
    path('login/', auth_views.login,{'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('matricula/',matricula, name='matricula'),
    path('novadisciplina/',novaDisciplina, name='novaDisciplina'),
    path('novoano/',novoAno, name='novoAno'),
    path('anosEnsino/',getAnos, name='anosEnsino'),
    path('novahabilidade/',novaHabilidade, name='novaHabilidade'),
    path('habilidades/',getHabilidades, name='habilidades'),
    path('novaturma/',novaTurma, name='novaTurma'),
    path('turmas/',getTurmas, name='turmas'),
    path('novoaluno/',NovoAluno, name='NovoAluno'),
    path('novocoordenador/',NovoCoordenador, name='NovoCoordenador'),
    path('novoprofessor/',NovoProfessor, name='NovoProfessor'),
    path('novoassistente/',NovoAssistente, name='NovoAssistente'),
    path('recover/',recover, name='recover'),
    path('areaUser/',areaUser, name='areaUser'),
    path('areaAluno/',areaAluno, name='areaAluno'),
    path('areaProfessor/',areaProfessor, name='areaProfessor'),
    path('areaAssistente/',areaAssistente, name='areaAssistente'),
    path('first_edit_senha/',first_edit_senha, name='first_edit_senha'),

]
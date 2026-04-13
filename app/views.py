from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *
class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Coletando todos os dados do banco
        contexto = {
            'area_saber': AreaSaber.objects.all(),
            'instituicao_ensino': InstituicaoEnsino.objects.all(),
            'ufs': UF.objects.all(), # Note o nome 'ufs' para bater com o HTML
            'avaliacao': Avaliacao.objects.all(),
            'avaliacao_tipo': AvaliacaoTipo.objects.all(),
            'disciplina': Disciplina.objects.all(),
            'pessoa': Pessoa.objects.all(),
            'cidade': Cidade.objects.all(),
            'turno': Turno.objects.all(),
            'turma': Turma.objects.all(),
            'ocupacao': Ocupacao.objects.all(),
            'matricula': Matricula.objects.all(),
            'frequencia': Frequencia.objects.all(),
            'ocorrencia': Ocorrencia.objects.all(),
            'curso': Curso.objects.all(),
            'curso_disciplina': CursoDisciplina.objects.all(),
        }
        return render(request, 'index.html', contexto)
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import (
    AvaliacaoTipo, Cidade, Turno, Turma, AreaSaber, Ocupacao, 
    Pessoa, InstituicaoEnsino, Curso, Disciplina, Matricula, 
    Avaliacao, Frequencia, Ocorrencia, CursoDisciplina
)

# --- LISTAGENS SIMPLES (Sem chaves estrangeiras) ---
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class AvaliacaoTipoView(View):
    def get(self, request, *args, **kwargs):
        dados = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacao_tipo.html', {'dados': dados, 'titulo': 'Tipos de Avaliação'})

class TurnoView(View):
    def get(self, request, *args, **kwargs):
        dados = Turno.objects.all()
        return render(request, 'turno.html', {'dados': dados, 'titulo': 'Turnos'})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        dados = Turma.objects.all()
        return render(request, 'turma.html', {'dados': dados, 'titulo': 'Turmas'})

class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        dados = AreaSaber.objects.all()
        return render(request, 'area_saber.html', {'dados': dados, 'titulo': 'Áreas do Saber'})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        dados = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'dados': dados, 'titulo': 'Ocupações'})

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        dados = Cidade.objects.all()
        return render(request, 'cidade.html', {'dados': dados, 'titulo': 'Cidades'})

# --- LISTAGENS COM RELACIONAMENTOS (Usando select_related para performance) ---

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.select_related('cidade', 'ocupacao').all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class InstituicaoEnsinoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.select_related('cidade').all()
        return render(request, 'instituicao_ensino.html', {'instituicoes': instituicoes})

class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.select_related('area_saber', 'instituicao_ensino').all()
        return render(request, 'curso.html', {'cursos': cursos})

class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.select_related('area_saber').all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})

class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.select_related('instituicao_ensino', 'curso', 'pessoa').all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.select_related('curso', 'disciplina', 'avaliacao_tipo').all()
        return render(request, 'templates/avaliacao.html', {'avaliacoes': avaliacoes})

class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.select_related('curso', 'disciplina', 'pessoa').all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.select_related('curso', 'disciplina', 'pessoa').all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})

class CursoDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        relacoes = CursoDisciplina.objects.select_related('disciplina', 'curso').all()
        return render(request, 'curso_disciplina.html', {'relacoes': relacoes})
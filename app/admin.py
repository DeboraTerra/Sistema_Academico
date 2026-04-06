from django.contrib import admin
from .models import *
from django.contrib import admin

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na listagem
    search_fields = ('nome',)# Campos que serão pesquisados
    inlines = [PessoaInline]
    

# i) Ocupação e pessoas 
#  ii) Instituição e cursos 
#  iii) Área do saber e cursos 
--feito ate aq
#  iv) Cursos e disciplinas 
#  v) Disciplinas e avaliações 
#  vi) Turmas e alunos 
#  vii) UF e cidades 
#  ix) Estudantes, disciplinas, avaliações, frequência

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1
    
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'telefone', 'cidade__nome',)
    search_fields = ('nome', 'site', 'telefone', 'cidade__nome',)
    inlines = [CursoInline]

    
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber__nome')
    search_fields  =('nome', 'area_saber__nome')
    inlines = [CursoInline], [AvaliacaoInline]


class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1
    
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [MatriculaInline]





admin.site.register(AvaliacaoTipo)
admin.site.register(Cidade)
admin.site.register(Turno)
admin.site.register(Turma)
admin.site.register(AreaSaber)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(InstituicaoEnsino)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
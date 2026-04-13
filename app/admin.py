from django.contrib import admin
from .models import *

# --- DEFINIÇÃO DOS INLINES ---

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class CidadeInline(admin.TabularInline):
    model = Cidade 
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

# --- CONFIGURAÇÃO DOS ADMINS ---

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome_completo')
    search_fields = ('sigla', 'nome_completo')
    inlines = [CidadeInline]

@admin.register(InstituicaoEnsino)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'telefone', 'get_cidade_nome')
    search_fields = ('nome', 'site', 'telefone', 'cidade__nome')
    inlines = [CursoInline]

    def get_cidade_nome(self, obj):
        return obj.cidade.nome
    get_cidade_nome.short_description = 'Cidade'

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao_ensino', 'area_saber')
    # viii e ix: Mostra disciplinas, avaliações e matrículas (estudantes) vinculadas ao curso
    inlines = [CursoDisciplinaInline, AvaliacaoInline, MatriculaInline]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber__nome')
    search_fields = ('nome', 'area_saber__nome')
    # ix: Mostra frequências e avaliações específicas desta disciplina
    inlines = [FrequenciaInline, AvaliacaoInline]
    
@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [MatriculaInline]

# --- REGISTRO DOS MODELOS RESTANTES ---
# Nota: Modelos com Admin customizado acima já foram registrados via @admin.register

admin.site.register(AvaliacaoTipo)
admin.site.register(Cidade)
admin.site.register(Turno)
admin.site.register(Pessoa)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
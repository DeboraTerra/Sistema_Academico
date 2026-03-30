from django.contrib import admin
from django.urls import path
from app.views import * # Certifique-se de que seu app se chama 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoaView.as_view(), name='pessoa'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('instituicao/', InstituicaoEnsinoView.as_view(), name='instituicao'),
    path('area_saber/', AreaSaberView.as_view(), name='area_saber'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('curso_disciplina/', CursoDisciplinaView.as_view(), name='curso_disciplina'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('turno/', TurnoView.as_view(), name='turno'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
    path('tipo_avaliacao/', AvaliacaoTipoView.as_view(), name='tipo_avaliacao'),
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
]
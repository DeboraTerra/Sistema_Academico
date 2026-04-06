from django.db import models

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo da avaliação:")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Avaliação Tipo"
        verbose_name_plural = "Avaliações tipos"
        
class Cidade (models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade:")
    uf = models.CharField(max_length=3, verbose_name="Nome do Estado/Unidade Federativa:")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Turno (models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Turno:")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma:")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área:")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Area do Saber"
        verbose_name_plural = "Areas dos Saberes"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupação:")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa (models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa:")
    pai = models.CharField(max_length=100, verbose_name="Nome do Pai:")
    mae = models.CharField(max_length=100, verbose_name="Nome da mae:")
    cpf = models.IntegerField(verbose_name="CPF:")
    data_nasc = models.DateField(verbose_name="Data Nascimento:")
    email = models.CharField(max_length=100, verbose_name="Email:")
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, verbose_name = "Cidade do Pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete = models.CASCADE, verbose_name = "Ocupação da pessoa")

    def __str__(self):
        return f"{self.nome}, {self.pai}, {self.mae}, {self.cpf}, {self.data_nasc}, {self.email}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição:")
    site = models.CharField(max_length=100, verbose_name="link:")
    telefone = models.IntegerField(verbose_name="Número Telefone:")
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, verbose_name = "Cidade da Instituição:")
    def __str__(self):
        return f"{self.nome}, {self.site}, {self.telefone}"
    class Meta:
        verbose_name = "InstituiçãoEnsino"
        verbose_name_plural = "InstituiçõesEnsino"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina:")
    area_saber = models.ForeignKey(AreaSaber,on_delete = models.CASCADE,verbose_name = "Area do saber:")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso:")
    carga_horaria_total = models.CharField(max_length=100, verbose_name="Quantidade de horas:")
    duracao_meses = models.IntegerField(verbose_name = "Quantidade de meses do Curso:")
    area_saber = models.ForeignKey(AreaSaber,on_delete = models.CASCADE,verbose_name = "Area do saber:")
    instituicao_ensino=models.ForeignKey(InstituicaoEnsino,on_delete = models.CASCADE, verbose_name="Instituição de Ensino:")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, default = '1', verbose_name = "Disciplina")
    def __str__(self):
        return f"{self.nome}, {self.carga_horaria_total}, {self.duracao_meses}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    

        
class Matricula(models.Model):
    instituicao_ensino=models.ForeignKey(InstituicaoEnsino,on_delete = models.CASCADE, verbose_name="Instituição de Ensino:")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name="Nome Curso:")
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name="Nome Curso:")
    data_inicio = models.DateField(verbose_name = "Data da Matricula:")
    data_previsao_termino = models.DateField(verbose_name = "Previsão do termino:")
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE, default = '1',verbose_name="Turma Aluno:")
    def __str__(self):
        return f"{self.data_inicio}, {self.data_previsao_termino}"
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"
        
class Avaliacao(models.Model):
    descricao = models.CharField(max_length = 100, verbose_name = "Descrição da avaliação")
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE, verbose_name="Nome do curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Nome Disciplina:")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete = models.CASCADE, verbose_name = "Tipo avaliação:")
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")
    def __str__(self):
        return f"{self.pessoa.nome} - {self.numero_faltas} faltas"
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"
# ocorrencia e cursoDisciplina
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length = 100, verbose_name = "Descricao da Ocorrencia")
    data = models.DateField(verbose_name = "Data da Ocorrencia")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso do Ocorrenciado")
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE,  verbose_name = "Disciplina em que ocorreu")
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Pessoa que tomou a ocorrencia")
    def __str__(self):
        return f"{self.descricao}, {self.data}"
    class Meta:
        verbose_name = "Ocorrencia"
        verbose_name_plural = "Ocorrencias"

class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina,on_delete = models.CASCADE, verbose_name = "Curso da disciplina")
    carga_horaria = models.CharField(max_length = 10, verbose_name = "Carga horaria da disciplina no curso")
    curso =  models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Curso da Disciplina")
    periodo = models.CharField(max_length = 100, default = '1', verbose_name = "Periodo")
    def __str__(self):
        return self.carga_horaria
    class Meta:
        verbose_name = "Curso Disciplina"
        verbose_name_plural = "Cursos Disciplinas"
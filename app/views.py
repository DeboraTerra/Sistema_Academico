from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import *

# --- Auxiliares e Mixins ---

def obter_usuario_logado(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return None
    return get_object_or_404(Usuario, id=usuario_id)


class LoginRequiredMixin:
    """Mixin que valida dinamicamente se o usuário está logado antes de processar a view."""
    def dispatch(self, request, *args, **kwargs):
        self.usuario_logado = obter_usuario_logado(request)
        if not self.usuario_logado:
            return redirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin(LoginRequiredMixin):
    """Garante que o usuário está logado E pertence ao tipo Administrador."""
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if response.status_code == 302:
            return response

        # CORRIGIDO: de tipo.nome para tipo.nome
        if self.usuario_logado.tipo.nome != 'Administrador':
            messages.error(request, "Acesso negado. Esta área é restrita a administradores.")
            return redirect(reverse('dashboard_usuario')) 
        return response


class ComumRequiredMixin(LoginRequiredMixin):
    """Garante que o usuário está logado E pertence ao tipo Cidadão."""
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if response.status_code == 302:
            return response
            
        # CORRIGIDO: Alterado de tipoUsuario para tipo (conforme models.py)
        if self.usuario_logado.tipo.nome != 'Cidadão':
            messages.error(request, "Acesso restrito a cidadãos.")
            return redirect(reverse('admin_dashboard'))
        return response


# --- Views de Autenticação e Cadastro ---

class CadastroUsuarioView(View):
    """View responsável pelo formulário e processamento do cadastro de novos usuários."""
    
    def get(self, request):
        if obter_usuario_logado(request):
            return redirect(reverse('dashboard_usuario'))
        return render(request, 'cadastro.html')

    def post(self, request):
        user_nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not all([user_nome, email, senha]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'cadastro.html')

        # CORRIGIDO: bloco except ajustado para TipoUser e variável corrigida
        try:
            tipo_cidadao = TipoUser.objects.get(nome='Cidadão')
        except TipoUser.DoesNotExist:
            messages.error(request, "Erro de configuração do sistema: Tipo 'Cidadão' não encontrado.")
            return render(request, 'cadastro.html')

        # CORRIGIDO: Atributos batendo com o seu models.py
        Usuario.objects.create(
            user_nome=user_nome,
            email=email,
            senha=make_password(senha),
            tipo=tipo_cidadao  # Nome do campo no model é 'tipo'
        )

        messages.success(request, "Cadastro realizado com sucesso! Faça seu login.")
        return redirect(reverse('login'))

class LoginView(View):
    """View responsável pelo login do usuário."""
    
    def get(self, request):
        usuario_logado = obter_usuario_logado(request)
        if usuario_logado:
            # CORRIGIDO: 'tipo' em vez de 'tipoUser' e padronizado 'Cidadão' com acento
            if usuario_logado.tipo.nome == 'Cidadão':
                return redirect(reverse('dashboard_usuario'))
            return redirect(reverse('admin_dashboard'))

        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not email or not senha:
            messages.error(request, "Por favor, preencha e-mail e senha.")
            return render(request, 'login.html')

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            messages.error(request, "E-mail ou senha inválidos.")
            return render(request, 'login.html')

        if check_password(senha, usuario.senha):
            request.session['usuario_id'] = usuario.id
            messages.success(request, f"Bem-vindo(a) de volta, {usuario.user_nome}!")
            
            # CORRIGIDO: Alterado de usuario.tipo.nome para verificar a rota correta
            if usuario.tipo.nome == 'Administrador':
                return redirect(reverse('admin_dashboard'))
            else:
                return redirect(reverse('tarefa'))
        else:
            messages.error(request, "E-mail ou senha inválidos.")
            return render(request, 'login.html')


class LogoutView(View):
    """View responsável por encerrar a sessão do usuário."""
    def get(self, request):
        if 'usuario_id' in request.session:
            del request.session['usuario_id']
        messages.success(request, "Você saiu da sua conta.")
        return redirect(reverse('login'))
    
# Adicione o AdminRequiredMixin aqui para proteger a página
class UsuarioView(AdminRequiredMixin, View):
    def get (self, request, *args, **kwargs):
        usuarios = Usuario.objects.all() 
        return render(request, 'usuario.html', {'usuarios': usuarios})
    
class TarefaView(View):
    def get (self, request, *args, **kwargs):
        tarefas = Tarefa.objects.all()
        return render(request, 'tarefa.html', {'tarefas': tarefas})
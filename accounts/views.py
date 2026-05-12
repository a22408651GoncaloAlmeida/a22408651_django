from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import MagicLink
from django.contrib.auth.models import Group

def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio_index')
        else:
            erro = 'Credenciais inválidas.'
    return render(request, 'accounts/login.html', {'erro': erro})

def logout_view(request):
    logout(request)
    return redirect('login')

def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        grupo, _ = Group.objects.get_or_create(name='autores')
        user.groups.add(grupo)
        return redirect('login')
    return render(request, 'accounts/registo.html', {'form': form})

# link mágico ----------------------------------

def magic_link_request(request):
    erro = None
    sucesso = None
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            link = MagicLink.objects.create(user=user)
            url = request.build_absolute_uri(f'/accounts/magic/{link.token}/')
            send_mail(
                subject='O teu link de acesso',
                message=f'Clica aqui para entrar: {url}\n\nEste link expira em 15 minutos.',
                from_email=None,
                recipient_list=[email],
            )
            sucesso = 'Link enviado! Verifica o teu email.'
        except User.DoesNotExist:
            erro = 'Nenhuma conta encontrada com esse email.'
    return render(request, 'accounts/magic_link_request.html', {'erro': erro, 'sucesso': sucesso})

def magic_link_login(request, token):
    try:
        link = MagicLink.objects.get(token=token)
        if link.is_valid():
            link.usado = True
            link.save()
            login(request, link.user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('portfolio_index')
        else:
            return render(request, 'accounts/magic_link_erro.html', {'erro': 'Link expirado ou já usado.'})
    except MagicLink.DoesNotExist:
        return render(request, 'accounts/magic_link_erro.html', {'erro': 'Link inválido.'})
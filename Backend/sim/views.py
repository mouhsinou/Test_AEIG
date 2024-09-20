from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({'message': 'CSRF cookie set'})


@require_http_methods(['POST'])
def login_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        password = data['password']
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON'}, status=400
        )

    user = authenticate(request, username=email, password=password)

    if user:
        login(request, user)
        return JsonResponse({'success': True})
    return JsonResponse(
        {'success': False, 'message': 'Invalid credentials'}, status=401
    )


def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})


@require_http_methods(['GET'])
def user(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {'username': request.user.username, 'email': request.user.email}
        )
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )


@require_http_methods(['POST'])
def register(request):
    data = json.loads(request.body.decode('utf-8'))
    form = CreateUserForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'User registered successfully'}, status=201)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'error': errors}, status=400)


from django.shortcuts import render, redirect, get_object_or_404
from .models import Tache, Permission
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Tache  # Assurez-vous que le modèle Tache est bien importé

from django.db.models import Q

@login_required
def dashboard(request):
    # Récupérer toutes les tâches créées par l'utilisateur actuel
    taches_creees = Tache.objects.filter(createur=request.user)
    
    # Tâches assignées à l'utilisateur
    taches_assignees = Tache.objects.filter(utilisateurs=request.user)

    # Tâches terminées créées par l'utilisateur ou lui étant assignées (en éliminant les doublons)
    taches_terminees = Tache.objects.filter(
        Q(createur=request.user) | Q(utilisateurs=request.user),
        est_terminee=True
    ).distinct()

    # Tâches non terminées créées par l'utilisateur ou lui étant assignées (en éliminant les doublons)
    taches_en_cours = Tache.objects.filter(
        Q(createur=request.user) | Q(utilisateurs=request.user),
        est_terminee=False
    ).distinct()

    utilisateurs = User.objects.all()
    taches = Tache.objects.all()

    context = {
        'utilisateurs': utilisateurs,
        'taches_creees': taches_creees,
        'taches_assignees': taches_assignees,
        'taches_terminees': taches_terminees,
        'taches_en_cours': taches_en_cours,
        'taches': taches
    }

    return render(request, 'dashboard.html', context)


@login_required
def creer_tache(request):
    if request.method == 'POST':
        if request.user.permission.peut_ajouter_tache:
            titre = request.POST['titre']
            description = request.POST['description']
            utilisateurs_assignes_ids = request.POST.getlist('utilisateurs_assignes')
            tache = Tache.objects.create(titre=titre, description=description, createur=request.user)
            tache.utilisateurs.set(utilisateurs_assignes_ids)
            return redirect('dashboard')
    return redirect('dashboard')  # Redirige si l'utilisateur n'a pas la permission

@login_required
def modifier_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    if request.method == 'POST':
        if request.user.permission.peut_modifier_tache:
            tache.titre = request.POST['titre']
            tache.description = request.POST['description']
            tache.utilisateurs.set(request.POST.getlist('utilisateurs_assignes'))
            tache.save()
            return redirect('dashboard')
    return redirect('dashboard')  

@login_required
def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    if request.user.permission.peut_supprimer_tache:
        tache.delete()
    return redirect('dashboard')


@login_required
def gerer_permissions(request):
    if request.method == 'POST':
        utilisateur_id = request.POST['utilisateur_id']
        utilisateur = User.objects.get(id=utilisateur_id)
        permission, created = Permission.objects.get_or_create(utilisateur=utilisateur)

        permission.peut_ajouter_tache = 'peut_ajouter_tache' in request.POST
        permission.peut_modifier_tache = 'peut_modifier_tache' in request.POST
        permission.peut_supprimer_tache = 'peut_supprimer_tache' in request.POST
        permission.peut_marquer_tache_terminee = 'peut_marquer_tache_terminee' in request.POST
        permission.save()

        return redirect('dashboard')


@login_required
def marquer_tache_terminee(request, tache_id):
    # Récupérer la tâche par son ID
    tache = get_object_or_404(Tache, id=tache_id)

   
    if request.user.permission.peut_marquer_tache_terminee:
        tache.est_terminee = True  # Marquer la tâche comme terminée
        tache.date_fin = timezone.now()  # Enregistrer la date de fin
        tache.save()  # Sauvegarder les changements
        # Rediriger vers le tableau de bord
        return redirect('dashboard')

   
    return redirect('dashboard') 


from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Tache
from .forms import TacheForm 

class ModifierTacheView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tache
    form_class = TacheForm
    template_name = 'modifier_tache.html'
    success_url = reverse_lazy('dashboard') 

    def test_func(self):
        # Vérifie si l'utilisateur a la permission de modifier la tâche
        tache = self.get_object()
        return self.request.user.permission.peut_modifier_tache

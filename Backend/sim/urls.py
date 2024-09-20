from django.urls import path
from . import views
from .views import ModifierTacheView

urlpatterns = [
    path('api/set-csrf-token', views.set_csrf_token, name='set_csrf_token'),
    path('api/login', views.login_view, name='login'),
    path('api/logout', views.logout_view, name='logout'),
    path('api/user', views.user, name='user'),
    path('api/register', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('creer_tache/', views.creer_tache, name='creer_tache'),
    path('gerer_permissions/', views.gerer_permissions, name='gerer_permissions'),

    path('supprimer_tache/<int:tache_id>/', views.supprimer_tache, name='supprimer_tache'),
    path('tache/marquer_terminee/<int:tache_id>/', views.marquer_tache_terminee, name='marquer_tache_terminee'),
    path('tache/modifier/<int:pk>/', ModifierTacheView.as_view(), name='modifier_tache'),
    
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('inmueble/agregar/', views.agregar_inmueble, name='agregar_inmueble'),
    path('inmuebles/mis_inmuebles/', views.mis_inmuebles, name='mis_inmuebles'),
    path('inmueble/<int:pk>/editar/', views.editar_inmueble, name='editar_inmueble'),
    path('inmueble/<int:pk>/borrar/', views.borrar_inmueble, name='borrar_inmueble'),
    path('inmuebles/', views.listar_inmuebles, name='listar_inmuebles'),
    path('api/comunas/', views.obtener_comunas_por_region, name='obtener_comunas_por_region'),
]


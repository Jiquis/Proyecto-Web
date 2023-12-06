from django.urls import path

from . import views

app_name = "home"


urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('detail_usuarioS/<int:pk>/', views.DetailUsuario.as_view(), name="detail_usuarioS"),
    path('login_usuario', views.login, name='login'),
    path('apuestas_usuario', views.Apuestas, name='Apuestas'),
    path('paybet_usuario', views.Paybet, name='Paybet'),
    path('payment_usuario', views.Payment, name='Payment'),
    path('profile_settings', views.ProfileSet, name='Profile settings'),
    path('profile_view', views.ProfileView, name='Profile view'),
    path('register_usuario', views.Register, name='Register'),
    path('tabla_opciones', views.TablaOpciones, name='Tabla de opciones'),
    path('problems', views.Problems, name='problems'),
]
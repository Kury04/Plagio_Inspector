from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home,name='login'),

    path('index/', views.index_view, name='index'),

    # Vista de login unificada
    path('login/', views.login_view, name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Vista de registro de usuario
    path('register/', views.register, name='register'),    
    
    path('compare/', views.fileCompare,name='compare'), 


    path('eliminar/<str:nombre_archivo>/', views.eliminar_archivo, name='eliminar_archivo'),
    path('subir_archivo/', views.subir_archivo, name='subir_archivo'),
    path('ejecutar_busqueda/<str:nombre_archivo>/', views.ejecutar_busqueda, name='ejecutar_busqueda'),
    path('ver_resultados/<str:nombre_archivo>/', views.ver_resultados, name='ver_resultados'),

    path('comparar_documentos/', views.comparar_documentos, name='comparar_documentos'),

    path('historial/', views.fileHistorial, name='historial'),

    path('revisar/', views.fileRevisar, name='revisar'), 

    path('test/', views.test,name='Test'),


    path('filetest/', views.filetest,name='filetest'),
    path('twofiletest1/', views.twofiletest1,name='twofiletest1'),
    path('twofilecompare1/', views.twofilecompare1,name='twofilecompare1'),


    path('ayuda/', views.fileAyuda, name='ayuda')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


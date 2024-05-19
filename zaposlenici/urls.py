from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_zaposlenik, name='view_zaposlenik'),
    path('dodaj/', views.dodaj, name='dodaj'),
    path('uredi/<int:id>/', views.uredi, name='uredi'),
    path('obrisi/<int:id>/', views.obrisi, name='obrisi'),
    path('pretraga/', views.pretraga, name='pretraga'),
    path('info', views.info, name='info'),
    path('kabinet/', views.kabinet, name='kabinet'),
    path('opca_uprava', views.opca_uprava, name='opca_uprava'),
]


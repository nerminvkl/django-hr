from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zaposlenici.urls')),
]

admin.site.site_header = 'HR - Općina Velika Kladuša'
admin.site.index_title = 'Kontrolna ploča'
admin.site.site_title = 'HR - Općina Velika Kladuša'
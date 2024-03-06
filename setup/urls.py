from django.contrib import admin
from django.urls import path
from faculdade.views import alunos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', alunos)
]

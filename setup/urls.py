from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from faculdade import views


router = routers.DefaultRouter()
router.register(r'alunos', views.AlunoViewSet)
router.register(r'cursos', views.CursoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))    
]

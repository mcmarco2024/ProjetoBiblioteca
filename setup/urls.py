from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library import views

router = DefaultRouter()
router.register (r 'autores', views.AutorViewSet)
router.register (r 'categorias', views.CategoriaViewSet)
router.register (r 'livros', views.LivroViewSet)
router.register (r 'emprestimos', views.EmprestimoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # API URLS

]

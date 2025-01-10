from django.contrib import admin
from .models import Livro, Usuário, Emprestimo

class Livro_Admin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'gênero',
    'data de publicação', 'ISBN', descrição)
    list_display = ('titulo', 'autor')
    list_per_page = 10
    search_fields = ('titulo', 'autor', 'gênero')

admin.site.register (Estudante, Estudante_Admin)
class Usuário_Admin(admin.ModelAdmin):
    list_display = ('Nome', 'e-mail', 'telefone', papel)
    list_display_links = ('Nome', 'e-mail')
    list_per_page = 10
    search_fields = ('Nome', 'e-mail')

class Empréstimo_Admin(admin.ModelAdmin):
    list_display = ('livros', 'usuários')
    list_display_links = ('livros', 'usuários')
    list_per_page = 10
    search_fields = ('estudante', 'curso')
admin.site.register (livro, usuários_Admin)
    

from rest_framework import serializers
from .models import Livro, Usuário, Empréstimo

class Livro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['Título', 'Autor', 'gênero', 'data de publicação', 'ISBN', 'descrição']

class Usuário_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer)
    livro = livroSerializer()

    class Meta:
        model = Emprestimo
        fields = '__all__'


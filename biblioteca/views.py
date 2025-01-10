from django.shortcuts import render

from rest_framework import viewsets
from .models import Autor, Categoria, livro, Emprestimo
from .serializers import AutorSerializer, CategoriaSerializer, LivroSerializer, EmprestimoSerializer

class Livro_viewset(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Estudante_Serializer

    def get_queryset(self):
        queryset = Livro.objects.all()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome=nome)
        return queryset

class Usuario_viewset(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    
    queryset = Usuário.objects.all()
    serializer_class = Empréstimo_Serializer 

class Matricula_viewset(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = matriculas.objects.all()
    serializer_class = Matricula_Serializer

class Título_lista_Emprestimo(generics.ListAPIView):
    def get_queryset(self):
        queryset = matriculas.objects.filter(estudante_id = self.kwargs ['pk'])
        return queryset

    serializer_class = Lista_Matricula_Estudante_Serializer

class Título_lista_Curso(generics.ListAPIView):
    def get_queryset(self):
        queryset = matriculas.objects.filter(estudante_id = self.kwargs ['pk'])
        return queryset

    serializer_class = Lista_Matricula_Curso_Serializer

from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_lenght=50)
    autor = models.CharField(max_lenght=30)
    genero = models.CharField(max_lenght=30)
    data de publicação = models.CharFields(max_lenght=8)
    ISBN = models.CharFields(max_lenght=15)
    descricão = models.CharFields(max_lenght=30)
    def __str__(self):
        return self.título
    
class Usuario(models.Model):
    nome = models.CharField(max_lenght=30)
    email = models.CharField(max_lenght=30)
    telefone = models.CharField(max_lenght=30)
    papel = models.CharFields(max_lenght=15)
    descricão = models.CharFields(max_lenght=30)
    def __str__(self):
        return self.título      

    
class Emprestimo (models.Model):
    livro = models.ForeignKey(Livro, related_name = 'emprestimos', on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null = True, blank=true)
    Usuario_nome = models.CharField(max_lenght=30)
    def __str__(self):
        return f'{self.usuario_nome} - {self.livro.titulo}
    


   




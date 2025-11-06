from tabnanny import verbose
import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instace, filename):
    ext = filename.split('.') [-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    class Meta:
        abstract = True

class Servico(Base):
    ICONES_CHOICES = (
        ('lni-cog','Engrenagem'),
        ('lni-stats-up','Gráfico'),
        ('lni-users','Usuário'),
        ('lni-layers','Design'),
        ('lni-mobile','Mobile'),
        ('lni-rocket','Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=12, choices=ICONES_CHOICES)
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico
    
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Colaborador(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome
    
class Recursos(Base):
    ICONES_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone','Laptop & Celular'),
        ('lni-cog','Engrenagem'),
        ('lni-leaf','Folha'),
        ('lni-layers','Camada'),
        ('lni-leaf','Folha')
    )

    recurso = models.CharField('Recurso', max_length=100)
    desc = models.CharField('Descrição', max_length=200)
    icone = models.ImageField('Ícone',max_length=16, choices=ICONES_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

        def __str__(self):
            return self.recurso

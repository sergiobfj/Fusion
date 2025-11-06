from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView
from .models import Servico, Colaborador, Recursos
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        total_recursos = Recursos.objects.count()
        i = total_recursos // 2

        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['colaborador'] = Colaborador.objects.order_by('?').all()
        context['recursos_left'] = Recursos.objects.order_by('?')[:i]
        context['recursos_right'] = Recursos.objects.order_by('?')[i:]
        return context

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o e-mail.')
        return super().form_invalid(form)

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Mediator
from .forms import SearchForm
from . import services


class MediatorListView(ListView):
    """Відображає сторінку зі списком медіаторів."""
    model = Mediator
    paginate_by = 9
    template_name = 'registry/list/index.html'

    def get_queryset(self):
        return services.get_mediators_qs(
            not self.request.user.is_staff,
            self.request.GET,
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context


class MediatorDetailView(DetailView):
    """Відображає сторінку з детальною інформацією медіатора."""
    model = Mediator
    template_name = 'registry/detail/index.html'

    def get_queryset(self):
        return services.get_mediators_qs(only_active=not self.request.user.is_staff)

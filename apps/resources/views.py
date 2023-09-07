from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Resource
from . import services


class ResourceListView(ListView):
    """Відображає сторінку зі списком ресурсів."""
    model = Resource
    template_name = 'resources/list/index.html'

    def get_queryset(self):
        return services.get_resources_qs()

class ResourceDetailView(DetailView):
    """Відображає сторінку з детальною інформацією ресурса."""
    model = Resource
    template_name = 'resources/detail/index.html'

    def get_queryset(self):
        return services.get_resources_qs()

from django.views.generic import ListView
from rooms.models import Room


class Home(ListView):
    template_name = "home/index.html"
    model = Room
    context_object_name = 'rooms'

    def get_queryset(self):
        return self.model.objects.all()

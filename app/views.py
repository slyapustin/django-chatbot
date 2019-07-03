from django.views.generic.edit import FormView
from .forms import AddForm


class IndexView(FormView):
    template_name = 'app/index.html'
    form_class = AddForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.calculate()
        return super().form_valid(form)

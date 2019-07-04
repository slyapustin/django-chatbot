from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import AddForm


class IndexView(FormView):
    template_name = 'app/index.html'
    form_class = AddForm
    success_url = '/'

    def form_valid(self, form):
        result = form.create_calculate_task()
        messages.add_message(self.request, messages.INFO, 'Task {} was created.'.format(result.id))
        return super().form_valid(form)

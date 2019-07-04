from django import forms
from celery import group
from .tasks import add

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

    number = forms.IntegerField(label='Number of tasks', min_value=1, max_value=100000)

    def create_calculate_task(self):
        return group(add.s(self.cleaned_data['a'], self.cleaned_data['b']) for i in range(self.cleaned_data['number']))()

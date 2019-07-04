from django import forms
from .tasks import add

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

    def create_calculate_task(self):
        return add.apply_async(args=[self.cleaned_data['a'], self.cleaned_data['b']])

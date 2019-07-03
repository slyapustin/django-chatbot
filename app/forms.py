from django import forms
from .tasks import add

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

    def calculate(self):
        add.delay(self.cleaned_data['a'], self.cleaned_data['b'])

from django import forms
from .models import pizza

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='topping1', max_length=100)
#     topping2 = forms.CharField(label='topping2', max_length=100)
#     size = forms.ChoiceField(label='size', choices=[('small', 'small'),
#                                                    ('medium', 'medium'),
#                                                    ('large', 'large')])

#
class PizzaForm(forms.ModelForm): #django model form
    class Meta:
        model =pizza
        fields =['maindish', 'sidish', 'size']


class MultiplePizzaForms(forms.Form):
    number =forms.IntegerField(min_value=2,max_value=10)
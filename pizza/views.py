from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForms
from .models import pizza

# Create your views here.
def homepage(request):
    return render(request, 'pizza/home.html')
def order(request):
    form = PizzaForm()
    filled_form = PizzaForm(request.POST)
    if request.method == "POST":
        filled_form.save()
        return render(request, 'pizza/order.html', {'form': form})
    else:
        return render(request, 'pizza/order.html', {'form': form})


def pizzas(request):
    multiple_pizza_form = MultiplePizzaForms()  #empty form
    created_pizza_pk =None
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'nandri meendum varuga your order was place successfully !! %s,%s,%s size pizza' % (filled_form.cleaned_data['topping1'],filled_form.cleaned_data['topping2'],filled_form.cleaned_data['size'])

            created_pizza = filled_form.save()
            created_pizza_pk= created_pizza.id

        else:
            note = 'sorry please tryagain..'
            new_form = PizzaForm()
            return render(request,'pizza/order.html',{'note':note,'multiple_pizza_form':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})


    else:
        form = PizzaForm
        return render(request, 'pizza/order.html', {'pizzaform': form,'multiple_form':multiple_pizza_form})


def edit(request,pk):
    data= pizza.objects.get(pk=pk)
    form = PizzaForm(instance=data)
    if request.method == "POST":
        edit_form = PizzaForm(request.POST, instance=data)
        if edit_form.is_valid():
            edit_form.save()
            note = "Your information is successfully edited"
        else:
            note = 'Try again'
    return render(request,'pizza/edit.html', {'form': form, 'pk': pk})

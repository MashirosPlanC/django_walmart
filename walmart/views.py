from django.shortcuts import render
from .forms import MyForm
# Create your views here.
def mainsite(request):
    return render(request, 'main.html')

def cart(request):
    return render(request, 'cart.html')

def departments(request):
    return render(request, 'departments.html')

def myaccounts(request):
    return render(request, 'myaccounts.html')

def myitems(request):
    return render(request, 'myitems.html')

def services(request):
    return render(request, 'services.html')

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

def form(request):
    submitted_data = None
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
    else:
        form = MyForm()

    return render(request, 'app/form.html',{'form': form, 'submiited_data':submitted_data})

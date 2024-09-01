from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Author, Profile
from django.views.generic.base import TemplateView

# Create your views here.

def my_index(request):
    return render(request, 'index.html')

def my_view(request):
    car_list = Car.objects.all()
    
    context = {
        'car_list': car_list
    }
    return render(request, 'car_list.html',context)

class CarListView(TemplateView):
    template_name = 'my_second_app/car_list.html'
    
    def get_context_data(self, **kwargs):
        # Llamar al método base para obtener el contexto base
        context = super().get_context_data(**kwargs)
        
        # Agregar la lista de coches al contexto
        context['car_list'] = Car.objects.all()
        
        return context

def test_my_view(request,*args,**kwargs):
    print(args)
    print(kwargs)
    return HttpResponse('')


def author_view(request,*args,**kwargs):
    print(args)
    print(kwargs)
    
    author = Author.objects.get(id=kwargs['id'])
    profile = Profile.objects.get(id=kwargs['id'])
    return HttpResponse(f'Author: {author.name}, Website: {profile.website}, Biografia: {profile.biography}')
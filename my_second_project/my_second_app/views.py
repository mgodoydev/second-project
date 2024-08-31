from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list = [
        {'title': 'Mercedes'},
        {'title': 'Ferrari'},
        {'title': 'Kia'},
    ]
    context = {
        'car_list': car_list
    }
    return render(request, 'car_list.html',context)
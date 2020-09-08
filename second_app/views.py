from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {'insert_me': 'now hello from first app /, index '}
    return render(request, 'second_app/index.html', context=my_dict)

def help(request):
    dict = {'var_1': 'this is variable one', 'var_2': 'this is variable two'}
    return render(request, 'second_app/help.html', context = dict)
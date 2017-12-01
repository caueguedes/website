from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'megasolucoes/home.html')
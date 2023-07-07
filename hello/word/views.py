from django.shortcuts import render
from .models import Project
from django.views.generic import DetailView

def word_detail(request):
    index=Project.objects.all()
    return render(request, 'word/detail.html',{'index':index})
def word_index(request):
    return render(request, 'word/index.html')
def word_home(requset):
    return render(requset,'word/base.html')



class MoreDetailView(DetailView):
    model = Project
    template_name = 'word/more_detail.html'
    context_object_name = 'project'


# Create your views here.

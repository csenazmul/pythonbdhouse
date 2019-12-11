#from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

"""def homeView(request):
    return HttpResponse("Hello World")
"""
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['name'] = "Nazmul Sheikh"
        context['country'] = "Bangladesh"

        list = [1,2,3,4,5]
        context['list'] = list


        return context

class AboutMe(TemplateView):
    template_name = "about.html"
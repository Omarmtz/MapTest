from django.shortcuts import render
from django.views.generic import ListView,View
from django.http import HttpResponse
from models import Point

# Create your views here.

class MapPoints(ListView):
    model = Point
    context_object_name = 'points'

class Index(View):
    """Main View"""
    template_name = 'map/index.html'
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)

class Test(View):
    """TEST CLIENT"""

    def post(self, request, *args, **kwargs):
        location = Point()
        location.deserialize(request.body)
        location.save()
        return HttpResponse(location)


    def get(self, request, *args, **kwargs):
        return HttpResponse(Point.objects.all())

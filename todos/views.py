from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# The index action for the todo list view
def index(request):
    template = loader.get_template('todos/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "kb_app/home.html"
    extra_content = {
        "title": "Главная страница",
    }

from django.views.generic import DetailView, ListView, TemplateView

from .models import KeyBoard


class Home(TemplateView):
    template_name = "kb_app/home.html"
    extra_content = {
        "title": "Главная страница",
    }


class KeyBoardList(ListView):
    model = KeyBoard
    template_name = "kb_app/keyboard_list.html"
    context_object_name = "kb_list"
    extra_context = {
        "title": "Каталог",
    }


class KeyBoardDetails(DetailView):
    model = KeyBoard
    template_name = "kb_app/keyboard_details.html"
    slug_url_kwarg = "keyboard_slug"
    context_object_name = "keyboard"

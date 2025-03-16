from django.urls import path

from . import views

app_name = "keyboards"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("catalog/", views.KeyBoardList.as_view(), name="keyboard_list"),
    path(
        "catalog/<slug:keyboard_slug>/",
        views.KeyBoardDetails.as_view(),
        name="keyboard_details",
    ),
]

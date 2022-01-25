from django.contrib import admin
from django.urls import path
from Post_n_Publication import views

urlpatterns = [
    path(
        "comren_publications",
        views.publicationFetchAPI.as_view(),
        name="comren_publications",
    ),
    path("comren_projects", views.projectFetchAPI.as_view(), name="comren_projects"),
]

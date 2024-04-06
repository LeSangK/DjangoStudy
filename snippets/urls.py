from django.urls import path

from snippets.views import (
    snippet_detail,
    snippet_list,
    snippet_new,
)


urlpatterns = [
    path("", snippet_list, name="snippet-list"),
    path("new/", snippet_new, name="snippet_new"),
    path("<int:snippet_id>/", snippet_detail, name="snippet_detail"),
]

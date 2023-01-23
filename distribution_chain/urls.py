from django.urls import path
from .views import ChainLinkCreateView, ChainLinkListView, ChainLinkView, ProductCreateView, ProductView

urlpatterns = [
    path("link/create/", ChainLinkCreateView.as_view()),
    path("link/list/", ChainLinkListView.as_view()),
    path("link/<pk>/", ChainLinkView.as_view()),
    path("product/create/", ProductCreateView.as_view()),
    path("product/<pk>/", ProductView.as_view())
]

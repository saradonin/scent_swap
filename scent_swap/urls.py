"""
URL configuration for scent_swap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from scent_app.views import IndexView, SearchView, PerfumeListView, BrandListView, BrandAddView, BrandUpdateView, \
    PerfumerListView, PerfumerAddView, PerfumerUpdateView, NoteAddView, PerfumeAddView, PerfumeUpdateView, \
    PerfumeDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('search', SearchView.as_view(), name="search"),

    path('brands', BrandListView.as_view(), name="brand-list"),
    path('brand/add', BrandAddView.as_view(), name="brand-add"),
    path('brand/edit/<pk>', BrandUpdateView.as_view(), name="brand-update"),

    path('perfumers', PerfumerListView.as_view(), name="perfumer-list"),
    path('perfumer/add', PerfumerAddView.as_view(), name="perfumer-add"),
    path('perfumer/edit/<pk>', PerfumerUpdateView.as_view(), name="perfumer-update"),

    path('note/add', NoteAddView.as_view(), name="note-add"),

    path('perfumes', PerfumeListView.as_view(), name="perfume-list"),
    path('perfume/add', PerfumeAddView.as_view(), name="perfume-add"),
    path('perfume/edit/<pk>', PerfumeUpdateView.as_view(), name="perfume-update"),
    path('perfume/details/<int:perfume_id>', PerfumeDetailsView.as_view(), name="perfume-details"),
]

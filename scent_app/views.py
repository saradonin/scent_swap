from django.shortcuts import render
from django.views import View

from scent_app.forms import SearchForm
from scent_app.models import Brand, Perfume, Category, User


# Create your views here.
class IndexView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_value = form.cleaned_data['value']
            matched_brands = Brand.objects.filter(name__icontains=search_value)
            matched_perfumes = Perfume.objects.filter(name__icontains=search_value)
            matched_offers = Perfume.objects.filter(requested_perfume__name__icontains=search_value)
            matched_users = User.objects.filter(username__icontains=search_value)
            if not matched_products.exists() and not matched_categories.exists():
                message = "Sorry, nothing to show you"
            else:
                message = ''

            ctx = {
                'form': form,
                'brands': matched_brands,
                'perfumes': matched_perfumes,
                'offers': matched_offers,
                'users': matched_users,
                'message': message
            }
            return render(request, 'search.html', ctx)

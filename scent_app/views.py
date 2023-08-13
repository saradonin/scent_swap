from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from scent_app.forms import SearchForm
from scent_app.models import Brand, Perfume, Category, User, SwapOffer


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class SearchView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'search.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_value = form.cleaned_data['value']
            matched_brands = Brand.objects.filter(name__icontains=search_value)
            matched_perfumes = Perfume.objects.filter(name__icontains=search_value)
            matched_offers = SwapOffer.objects.filter(requested_perfume__perfume__name__icontains=search_value)
            matched_users = User.objects.filter(username__icontains=search_value)

            if (not matched_brands.exists()
                    and not matched_perfumes.exists()
                    and not matched_offers.exists()
                    and not matched_users.exists()):
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


class PerfumeListView(ListView):
    model = Perfume
    template_name = "perfume_list.html"
    paginate_by = 50 # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

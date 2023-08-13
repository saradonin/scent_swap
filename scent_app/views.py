from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from scent_app.forms import SearchForm
from scent_app.models import Brand, Perfume, Category, User, SwapOffer, Perfumer, Note


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
            matched_perfumers = Perfumer.objects.filter(last_name__icontains=search_value)
            matched_offers = SwapOffer.objects.filter(requested_perfume__perfume__name__icontains=search_value)
            matched_users = User.objects.filter(username__icontains=search_value)

            if (not matched_brands.exists()
                    and not matched_perfumes.exists()
                    and not matched_perfumers.exists()
                    and not matched_offers.exists()
                    and not matched_users.exists()):
                message = "Sorry, nothing to show you"
            else:
                message = ''

            ctx = {
                'form': form,
                'brands': matched_brands,
                'perfumes': matched_perfumes,
                'perfumers': matched_perfumers,
                'offers': matched_offers,
                'users': matched_users,
                'message': message
            }
            return render(request, 'search.html', ctx)


class BrandListView(ListView):
    model = Brand
    template_name = "brand_list.html"
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BrandAddView(CreateView):
    model = Brand
    fields = "__all__"
    template_name = "brand_add_form.html"
    success_url = reverse_lazy('brand-list')


class BrandUpdateView(UpdateView):
    model = Brand
    fields = "__all__"
    template_name = "brand_update_form.html"
    success_url = reverse_lazy('brand-list')


class PerfumerListView(ListView):
    model = Perfumer
    template_name = "perfumer_list.html"
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PerfumerAddView(CreateView):
    model = Perfumer
    fields = "__all__"
    template_name = "perfumer_add_form.html"
    success_url = reverse_lazy('perfumer-list')


class PerfumerUpdateView(UpdateView):
    model = Perfumer
    fields = "__all__"
    template_name = "perfumer_update_form.html"
    success_url = reverse_lazy('perfumer-list')


class NoteAddView(CreateView):
    model = Note
    fields = "__all__"
    template_name = "note_add_form.html"
    success_url = reverse_lazy('note-add')


class PerfumeListView(ListView):
    model = Perfume
    template_name = "perfume_list.html"
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PerfumeAddView(CreateView):
    model = Perfume
    fields = "__all__"
    template_name = "perfume_add_form.html"
    success_url = reverse_lazy('perfume-list')


class PerfumeUpdateView(UpdateView):
    model = Perfume
    fields = "__all__"
    template_name = "perfume_update_form.html"
    success_url = reverse_lazy('perfume-list')

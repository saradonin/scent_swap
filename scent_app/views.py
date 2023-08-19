from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from scent_app.forms import SearchForm, UserLoginForm
from scent_app.models import Brand, Perfume, Category, User, SwapOffer, Perfumer, Note


# Create your views here.
class IndexView(View):
    def get(self, request):
        brands_count = Brand.objects.count()
        perfumer_count = Perfumer.objects.count()
        perfumes_count = Perfume.objects.count()
        offers_count = SwapOffer.objects.count()
        users_count = User.objects.count()

        ctx = {
            'brands_count': brands_count,
            'perfumer_count': perfumer_count,
            'perfumes_count': perfumes_count,
            'offers_count': offers_count,
            'users_count': users_count,
        }
        return render(request, 'index.html', ctx)


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


class BrandListView(View):
    def get(self, request):
        form = SearchForm()
        brands = Brand.objects.all().order_by("name")
        # Paginator object with plans and 50 per page
        paginator = Paginator(brands, 20)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        ctx = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, "brand_list.html", ctx)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_value = form.cleaned_data['value']
            brands = Brand.objects.filter(name__icontains=search_value).order_by("name")
        else:
            brands = Brand.objects.all().order_by("name")

        paginator = Paginator(brands, 20)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        ctx = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, "brand_list.html", ctx)


class BrandAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'scent_app.add_brand'
    model = Brand
    fields = "__all__"
    template_name = "brand_add_form.html"
    success_url = reverse_lazy('brand-list')


class BrandUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'scent_app.change_brand'
    model = Brand
    fields = "__all__"
    template_name = "brand_update_form.html"
    success_url = reverse_lazy('brand-list')


class BrandPerfumeListView(View):
    def get(self, request, brand_id):
        brand = Brand.objects.get(id=brand_id)
        perfumes = Perfume.objects.filter(brand=brand).order_by("name")
        # Paginator object with plans and 50 per page
        paginator = Paginator(perfumes, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        ctx = {
            'brand': brand,
            'page_obj': page_obj,
        }
        return render(request, "brand_perfumes_list.html", ctx)


class PerfumerListView(ListView):
    model = Perfumer
    template_name = "perfumer_list.html"
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PerfumerAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'scent_app.add_perfumer'
    model = Perfumer
    fields = "__all__"
    template_name = "perfumer_add_form.html"
    success_url = reverse_lazy('perfumer-list')


class PerfumerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'scent_app.change_perfumer'
    model = Perfumer
    fields = "__all__"
    template_name = "perfumer_update_form.html"
    success_url = reverse_lazy('perfumer-list')


class NoteAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'scent_app.add_note'
    model = Note
    fields = "__all__"
    template_name = "note_add_form.html"
    success_url = reverse_lazy('note-add')


class PerfumeListView(View):
    def get(self, request):
        form = SearchForm()
        perfumes = Perfume.objects.all().order_by("name")
        # Paginator object with plans and 50 per page
        paginator = Paginator(perfumes, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        ctx = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, "perfume_list.html", ctx)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_value = form.cleaned_data['value']
            perfumes = Perfume.objects.filter(name__icontains=search_value).order_by("name")
        else:
            perfumes = Perfume.objects.all().order_by("name")

        paginator = Paginator(perfumes, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        ctx = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, "perfume_list.html", ctx)


class PerfumeAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'scent_app.add_perfume'
    model = Perfume
    fields = "__all__"
    template_name = "perfume_add_form.html"
    success_url = reverse_lazy('perfume-list')


class PerfumeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'scent_app.change_perfume'
    model = Perfume
    fields = "__all__"
    template_name = "perfume_update_form.html"
    success_url = reverse_lazy('perfume-list')


class PerfumeDetailsView(View):
    def get(self, request, perfume_id):
        ctx = {
            'perfume': Perfume.objects.get(id=perfume_id)
        }
        return render(request, 'perfume_details.html', ctx)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        ctx = {'form': form}
        return render(request, 'user_login_form.html', ctx)

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = "Invalid input"

            ctx = {
                'form': form,
                'message': message
            }
            return render(request, 'user_login_form.html', ctx)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user-login')


class UserListView(LoginRequiredMixin, View):
        def get(self, request):
            form = SearchForm()
            users = User.objects.all().order_by("username")
            # Paginator object with plans and 50 per page
            paginator = Paginator(users, 20)
            # current page
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)

            ctx = {
                'page_obj': page_obj,
                'form': form,
            }
            return render(request, "user_list.html", ctx)

        def post(self, request):
            form = SearchForm(request.POST)
            if form.is_valid():
                search_value = form.cleaned_data['value']
                users = User.objects.filter(name__icontains=search_value).order_by("username")
            else:
                users = User.objects.all().order_by("username")

            paginator = Paginator(users, 20)
            # current page
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            ctx = {
                'page_obj': page_obj,
                'form': form,
            }
            return render(request, "user_list.html", ctx)

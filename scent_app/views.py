from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from scent_app.forms import SearchForm, UserLoginForm, UserAddForm, UserPerfumeAddForm
from scent_app.models import Brand, Perfume, Category, User, SwapOffer, Perfumer, Note, UserPerfume


# Create your views here.
class IndexView(View):
    """
    View for rendering the index page with statistics.
    """

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


class BrandListView(View):
    """
    View for displaying a list of brands with search functionality.
    """

    def get(self, request):
        """
        Handle GET requests and display the paginated list of brands.
        """
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
        """
        Handle POST requests and display the filtered list of brands based on search.
        """
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
    """
    View for adding new brands.
    """
    permission_required = 'scent_app.add_brand'
    model = Brand
    fields = "__all__"
    template_name = "brand_add_form.html"
    success_url = reverse_lazy('brand-list')


class BrandUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating brand details.
    """
    permission_required = 'scent_app.change_brand'
    model = Brand
    fields = "__all__"
    template_name = "brand_update_form.html"
    success_url = reverse_lazy('brand-list')


class BrandPerfumeListView(View):
    """
    View for displaying a list of perfumes of the specific brand..
    """

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
    """
    View for displaying a list of perfumers.
    """
    model = Perfumer
    template_name = "perfumer_list.html"
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PerfumerAddView(PermissionRequiredMixin, CreateView):
    """
    View for adding new perfumers.
    """
    permission_required = 'scent_app.add_perfumer'
    model = Perfumer
    fields = "__all__"
    template_name = "perfumer_add_form.html"
    success_url = reverse_lazy('perfumer-list')


class PerfumerUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating perfumers details.
    """
    permission_required = 'scent_app.change_perfumer'
    model = Perfumer
    fields = "__all__"
    template_name = "perfumer_update_form.html"
    success_url = reverse_lazy('perfumer-list')


class NoteAddView(PermissionRequiredMixin, CreateView):
    """
    View for adding new notes used in perfumes.
    """
    permission_required = 'scent_app.add_note'
    model = Note
    fields = "__all__"
    template_name = "note_add_form.html"
    success_url = reverse_lazy('note-add')


class PerfumeListView(View):
    """
    View for displaying a list of perfumes with search functionality.
    """

    def get(self, request):
        """
        Handle GET requests and display the paginated list of perfumes.
        """
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
        """
        Handle POST requests and display the filtered list of perfumes based on search.
        """
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
    """
    View for adding new perfumes.
    """
    permission_required = 'scent_app.add_perfume'
    model = Perfume
    fields = "__all__"
    template_name = "perfume_add_form.html"
    success_url = reverse_lazy('perfume-list')


class PerfumeUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating perfume details.
    """
    permission_required = 'scent_app.change_perfume'
    model = Perfume
    fields = "__all__"
    template_name = "perfume_update_form.html"
    success_url = reverse_lazy('perfume-list')


class PerfumeDetailsView(View):
    """
    View for displaying details of specific perfume.
    """

    def get(self, request, perfume_id):
        ctx = {
            'perfume': Perfume.objects.get(id=perfume_id)
        }
        return render(request, 'perfume_details.html', ctx)


class UserLoginView(View):
    """
    View for user login.
    """

    def get(self, request):
        """
        Handle GET requests and display the user login form.
        """
        form = UserLoginForm()
        ctx = {'form': form}
        return render(request, 'user_login_form.html', ctx)

    def post(self, request):
        """
        Handle POST requests and authenticate users.

        Redirects to the appropriate page after successful login.
        """
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
    """
    View for user logout.
    """

    def get(self, request):
        logout(request)
        return redirect('user-login')


class UserAddView(View):
    """
    View for adding new users.
    """

    def get(self, request):
        """
        Handle GET requests and display the user registration form.
        """
        form = UserAddForm()
        ctx = {'form': form}
        return render(request, 'user_add.html', ctx)

    def post(self, request):
        """
        Handle POST requests and create new user accounts.
        """
        form = UserAddForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('user-login')
        else:
            ctx = {
                'form': form
            }
            return render(request, 'user_add.html', ctx)


class UserListView(LoginRequiredMixin, View):
    """
    View for displaying a list of users with search functionality.
    """

    def get(self, request):
        """
        Handle GET requests and display the paginated list of users.
        """
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
        """
        Handle POST requests and display the filtered list of users based on search.
        """
        form = SearchForm(request.POST)
        if form.is_valid():
            search_value = form.cleaned_data['value']
            users = User.objects.filter(username__icontains=search_value).order_by("username")
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


# TODO finish adding
class UserPerfumeAddView(LoginRequiredMixin, View):
    """
    View for adding new perfumes to user's collection.
    """

    def get(self, request, perfume_id):
        form = UserPerfumeAddForm()
        user = request.user
        perfume = Perfume.objects.get(id=perfume_id)
        ctx = {
            'form': form,
            'user': user,
            'perfume': perfume
        }
        return render(request, 'userperfume_add_form.html', ctx)

    def post(self, request, perfume_id):
        form = UserPerfumeAddForm(request.POST)
        user = request.user
        perfume = Perfume.objects.get(id=perfume_id)

        if form.is_valid():
            volume = form.cleaned_data['volume']
            status = form.cleaned_data['status']
            to_exchange = form.cleaned_data['to_exchange']
            UserPerfume.objects.create(user=user, perfume=perfume, volume=volume, status=status, to_exchange=to_exchange)
            return redirect('userperfume-list', user_id=request.user.id)
        else:
            ctx = {
                'form': form
            }
            return render(request, 'userperfume_add_form.html', ctx)


class UserPerfumeListView(View):
    """
    View for displaying a list of perfumers in user's collection.
    """

    def get(self, request, user_id):
        """
        Handle GET requests and display the paginated list of perfumes in user's collection.
        """
        user = User.objects.get(id=user_id)
        perfumes = UserPerfume.objects.filter(user=user)
        # Paginator object with plans and 50 per page
        paginator = Paginator(perfumes, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        ctx = {
            'page_obj': page_obj,
        }
        return render(request, "userperfume_list.html", ctx)


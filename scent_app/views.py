from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from scent_app.forms import SearchForm, UserLoginForm, UserAddForm, UserPerfumeAddForm, OfferAddForm, MessageAddForm
from scent_app.models import Brand, Perfume, User, SwapOffer, Perfumer, Note, UserPerfume, Message


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
    View for displaying a list of perfumes of the specific brand.
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


class NoteListView(ListView):
    """
    View for displaying a list of notes.
    """
    model = Note
    template_name = "note_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
            perfumes = Perfume.objects.filter(
                Q(name__icontains=search_value) | Q(brand__name__icontains=search_value)).order_by("name")
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


class UserPerfumeListView(View):
    """
    View for displaying a list of perfumers in user's collection.
    """

    def get(self, request, user_id):
        """
        Handle GET requests and display the paginated list of perfumes in user's collection.
        """
        user = User.objects.get(id=user_id)
        perfumes = UserPerfume.objects.filter(user=user).order_by("perfume__brand", "perfume__name")
        # Paginator object with plans and 50 per page
        paginator = Paginator(perfumes, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        ctx = {
            'page_obj': page_obj,
            'user': user
        }
        return render(request, "userperfume_list.html", ctx)


class UserPerfumeAddView(LoginRequiredMixin, View):
    """
    View for adding new perfumes to user's collection.
    """

    def get(self, request, perfume_id):
        """
        Handle GET requests and display the form for adding a perfume to user's collection
        """
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
        """
        Handle POST requests and add perfume to user's collection
        """
        form = UserPerfumeAddForm(request.POST)
        user = request.user
        perfume = Perfume.objects.get(id=perfume_id)

        if form.is_valid():
            volume = form.cleaned_data['volume']
            status = form.cleaned_data['status']
            to_exchange = form.cleaned_data['to_exchange']
            UserPerfume.objects.create(user=user, perfume=perfume, volume=volume, status=status,
                                       to_exchange=to_exchange)
            return redirect('userperfume-list', user_id=request.user.id)
        else:
            ctx = {
                'form': form
            }
            return render(request, 'userperfume_add_form.html', ctx)


class UserPerfumeUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating perfume in user's collection.
    """
    model = UserPerfume
    fields = "volume", "status"
    template_name = "userperfume_update_form.html"

    def get_success_url(self):
        return reverse_lazy('userperfume-list', kwargs={'user_id': self.request.user.id})


class UserPerfumeDeleteView(LoginRequiredMixin, View):
    """
    Display confirmation to delete perfume from users collection and handle room deletion.
    """

    def get(self, request, userperfume_id):
        """
        Handle GET requests and display confirmation window.
        """
        user = request.user
        userperfume = UserPerfume.objects.get(id=userperfume_id)
        if not userperfume.user == user:
            return HttpResponseForbidden()

        ctx = {
            'userperfume': userperfume
        }
        return render(request, 'userperfume_delete_confirmation.html', ctx)

    def post(self, request, userperfume_id):
        """
        Handle POST requests and deletes perfume from collection.
        """
        confirm = request.POST.get('confirm')
        userperfume = UserPerfume.objects.get(id=userperfume_id)
        if confirm == "Yes":
            userperfume.delete()
            return redirect('userperfume-list', user_id=request.user.id)
        else:
            return redirect('userperfume-list', user_id=request.user.id)


class OfferListView(LoginRequiredMixin, View):
    """
    View for displaying a list of offers.
    """

    def get(self, request):
        """
        Handle GET requests and display the paginated list of swap offers.
        """
        form = SearchForm()
        offers = SwapOffer.objects.filter(is_completed=False).order_by("-created_at")
        # Paginator object with plans and 50 per page
        paginator = Paginator(offers, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        ctx = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, "offer_list.html", ctx)

    def post(self, request):
        """
        Handle POST requests and display the filtered list of swap offers based on search.
        """
        form = SearchForm(request.POST)
        if form.is_valid():
            search_value = form.cleaned_data['value']
            offers = SwapOffer.objects.filter(is_completed=False).filter(
                Q(offering_perfume__perfume__name__icontains=search_value) |
                Q(offering_perfume__perfume__brand__name__icontains=search_value)).order_by("-created_at")
        else:
            offers = SwapOffer.objects.filter(is_completed=False).order_by("-created_at")

        paginator = Paginator(offers, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        ctx = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, "offer_list.html", ctx)


class OfferListByUserView(LoginRequiredMixin, View):
    """
    View for displaying a list of offers created by logged user.
    """

    def get(self, request, user_id):
        """
        Handle GET requests and display the paginated list of swap offers.
        """
        user = User.objects.get(id=user_id)
        offers = SwapOffer.objects.filter(offering_perfume__user=user, is_completed=False).order_by("-created_at")
        # Paginator object with plans and 50 per page
        paginator = Paginator(offers, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        ctx = {
            'page_obj': page_obj,
            'user': user
        }
        return render(request, "offer_list_by_user.html", ctx)


class OfferAddView(LoginRequiredMixin, View):
    """
    View for adding new swap offer.
    """

    def get(self, request):
        """
        Handle GET requests and display the form for adding new swap offer.
        """
        form = OfferAddForm(request.user)
        ctx = {
            'form': form,
        }
        return render(request, 'offer_add_form.html', ctx)

    def post(self, request):
        """
        Handle POST requests and adds swap offer
        """
        form = OfferAddForm(request.user, request.POST)

        if form.is_valid():
            offering_perfume = form.cleaned_data['offering_perfume']
            requested_perfume = form.cleaned_data['requested_perfume']
            SwapOffer.objects.create(offering_perfume=offering_perfume, requested_perfume=requested_perfume)

            offering_perfume.to_exchange = True
            offering_perfume.save()

            return redirect('offer-list')
        else:
            ctx = {
                'form': form
            }
            return render(request, 'offer_add_form.html', ctx)


class OfferUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating offer details.
    """
    model = SwapOffer
    fields = "__all__"
    template_name = "offer_update_form.html"
    success_url = reverse_lazy('offer-list')


class OfferCloseView(LoginRequiredMixin, View):
    """
    Display confirmation prompt and close the offer.
    """

    def get(self, request, offer_id):
        """
        Handle GET requests and display confirmation window.
        """
        user = request.user
        offer = SwapOffer.objects.get(id=offer_id)

        if not offer.offering_perfume.user == user:
            return HttpResponseForbidden()

        ctx = {
            'offer': offer
        }
        return render(request, 'offer_close_confirmation.html', ctx)

    def post(self, request, offer_id):
        """
        Handle POST requests and closes the swap offer
        """
        confirm = request.POST.get('confirm')
        offer = SwapOffer.objects.get(id=offer_id)
        if confirm == "Yes":
            offer.is_completed = True
            offer.save()
            return redirect('offer-list')
        else:
            return redirect('offer-list')


class MessageListView(LoginRequiredMixin, View):
    """
    View for displaying a list of messages.
    """

    def get(self, request):
        """
        Handle GET requests and display the paginated list of messages
        """
        user = request.user

        messages = Message.objects.filter(Q(sender=user) | Q(receiver=user)).order_by("-timestamp")

        paginator = Paginator(messages, 25)
        # current page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        ctx = {
            'page_obj': page_obj
        }
        return render(request, 'message_list.html', ctx)


class MessageAddView(LoginRequiredMixin, View):
    """
    View for sending a message to other user.
    """

    def get(self, request, user_id):
        """
        Handle GET requests and display the form for sending a message.
        """
        form = MessageAddForm()
        sender = request.user
        receiver = User.objects.get(id=user_id)

        ctx = {
            'form': form,
            'sender': sender,
            'receiver': receiver
        }
        return render(request, 'message_add_form.html', ctx)

    def post(self, request, user_id):
        """
        Handle POST requests and create message
        """
        form = MessageAddForm(request.POST)
        sender = request.user
        receiver = User.objects.get(id=user_id)

        if form.is_valid():
            content = form.cleaned_data['content']

            Message.objects.create(sender=sender,
                                   receiver=receiver,
                                   content=content)
            return redirect('message-list')

        else:
            ctx = {
                'form': form,
                'sender': sender,
                'receiver': receiver,
            }
            return render(request, 'message_add_form.html', ctx)


class MessageDetailsView(LoginRequiredMixin, View):
    """
    View for displaying message details and sending a message.
    """

    def get(self, request, message_id):
        """
        Handle GET requests and display message details.
        """
        user = request.user
        form = MessageAddForm()
        message = Message.objects.get(id=message_id)
        other_user = message.sender if message.receiver == user else message.receiver

        message_history = Message.objects.filter(
            Q(sender=user) | Q(receiver=user),
            Q(sender=other_user) | Q(receiver=other_user),
        ).order_by("timestamp")

        if not (message.receiver == user or message.sender == user):
            return HttpResponseForbidden()

        # mark message as read if displayed by receiver
        for msg in message_history:
            if msg.receiver == user and not msg.is_read:
                msg.is_read = True
                msg.save()

        ctx = {
            'user': user,
            'other_user': other_user,
            'form': form,
            'message': message,
            'message_history': message_history,
        }
        return render(request, 'message_details.html', ctx)

    def post(self, request, message_id):
        """
        Handle POST requests and create respond message
        """
        form = MessageAddForm(request.POST)
        user = request.user
        original_message = Message.objects.get(id=message_id)
        other_user = original_message.sender if original_message.receiver == user else original_message.receiver
        message_history = Message.objects.filter(
            Q(sender=user) | Q(receiver=user),
            Q(sender=other_user) | Q(receiver=other_user),
        ).order_by("timestamp")

        if form.is_valid():
            content = form.cleaned_data['content']

            Message.objects.create(sender=user,
                                   receiver=other_user,
                                   content=content)
            return redirect('message-list')

        else:
            ctx = {
                'user': user,
                'other_user': other_user,
                'form': form,
                'message': original_message,
                'message_history': message_history,
            }
            return render(request, 'message_details.html', ctx)

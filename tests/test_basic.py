import pytest
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import resolve_url

from django.test import Client, RequestFactory
from django.urls import reverse

from scent_app.models import Perfume, Brand, UserPerfume, SwapOffer, User, Perfumer, Note, Message
from scent_app.views import BrandListView, PerfumeListView


@pytest.mark.django_db
def test_get_index_page():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_list_not_logged():
    client = Client()
    response = client.get(reverse("brand-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_search_form(set_up):
    # example data
    Brand.objects.create(name="First brand")
    Brand.objects.create(name="Some other brand")

    # post search query
    factory = RequestFactory()
    request = factory.post(reverse("brand-list"), {"value": "other"})
    # have to set the user, because request object doesn't have user attribute
    request.user = AnonymousUser()

    view = BrandListView.as_view()
    response = view(request)
    assert response.status_code == 200

    # assert results
    assert "Some" in response.content.decode()
    assert "other" in response.content.decode()
    assert "First" not in response.content.decode()


@pytest.mark.django_db
def test_brand_details(set_up):
    client = Client()
    brand = Brand.objects.first()
    # response = client.get(reverse("brand-perfumes", args=(brand.id,)))
    response = client.get(resolve_url("brand-perfumes", brand.id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_add_not_logged():
    client = Client()
    response = client.get(reverse("brand-add"))
    assert response.status_code == 302  # redirect to login page

    new_brand = {
        "name": "Test Brand Name",
        "description": "Test description"
    }
    response = client.post(reverse("brand-add"), new_brand)
    assert response.status_code == 302


@pytest.mark.django_db
def test_brand_add_logged(user_logged_in, set_up):
    user = user_logged_in
    response = user.client.get(reverse("brand-add"))
    assert response.status_code == 403

    new_brand = {
        "name": "Test Brand Name",
        "description": "Test description"
    }
    response = user.client.post(reverse("brand-add"), new_brand)
    assert response.status_code == 403


@pytest.mark.django_db
def test_brand_add_logged_superuser(superuser_logged_in, set_up):
    user = superuser_logged_in
    brand_count = Brand.objects.count()
    response = user.client.get(reverse("brand-add"))
    assert response.status_code == 200

    new_brand = {
        "name": "Test Brand Name",
        "description": "Test description"
    }
    response = user.client.post(reverse("brand-add"), new_brand)
    assert response.status_code == 302
    assert Brand.objects.count() == brand_count + 1
    assert Brand.objects.filter(name=new_brand["name"]).exists()


@pytest.mark.django_db
def test_brand_update_logged_superuser(superuser_logged_in, set_up):
    brand = Brand.objects.first()

    # get update page
    response = superuser_logged_in.client.get(reverse("brand-update", args=(brand.id,)))
    assert response.status_code == 200

    # update brand data
    updated_brand_data = {
        "name": "New Brand Name",
        "description": "New updated description"
    }
    response = superuser_logged_in.client.post(reverse("brand-update", args=(brand.id,)), updated_brand_data)
    assert response.status_code == 302

    # check if updated
    updated_brand = Brand.objects.get(id=brand.id)
    assert updated_brand.name == updated_brand_data["name"]


@pytest.mark.django_db
def test_perfume_list():
    client = Client()
    response = client.get(reverse("perfume-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_perfume_search_form(set_up):
    # get data
    perfume_to_find = Perfume.objects.first()
    perfume_not_to_find = Perfume.objects.last()

    # post search query
    factory = RequestFactory()
    request = factory.post(reverse("perfume-list"), {"value": perfume_to_find.name[:-2]})
    # have to set the user, because request object doesn't have user attribute
    request.user = AnonymousUser()

    view = PerfumeListView.as_view()
    response = view(request)
    assert response.status_code == 200

    # assert results
    assert perfume_to_find.name in response.content.decode()
    assert perfume_not_to_find.name not in response.content.decode()


@pytest.mark.django_db
def test_perfume_details(set_up):
    client = Client()
    perfume = Perfume.objects.first()
    response = client.get(reverse("perfume-details", args=(perfume.id,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_perfume_add_not_logged(set_up, new_perfume_data):
    client = Client()
    response = client.get(reverse("perfume-add"))
    assert response.status_code == 302  # redirect to login page

    response = client.post(reverse("perfume-add"), new_perfume_data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_perfume_add_logged(user_logged_in, set_up, new_perfume_data):
    user = user_logged_in
    response = user.client.get(reverse("perfume-add"))
    assert response.status_code == 403

    response = user.client.post(reverse("perfume-add"), new_perfume_data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_perfume_add_logged_superuser(superuser_logged_in, set_up, new_perfume_data):
    user = superuser_logged_in
    perfume_count = Perfume.objects.count()
    response = user.client.get(reverse("perfume-add"))
    assert response.status_code == 200

    response = user.client.post(reverse("perfume-add"), new_perfume_data)
    assert response.status_code == 302
    assert Perfume.objects.count() == perfume_count + 1
    assert Perfume.objects.filter(name=new_perfume_data["name"]).exists()


@pytest.mark.django_db
def test_perfume_update_logged_superuser(superuser_logged_in, set_up, new_perfume_data):
    user = superuser_logged_in
    perfume = Perfume.objects.first()
    response = user.client.get(reverse("perfume-update", args=(perfume.id,)))
    assert response.status_code == 200

    updated_perfume_data = new_perfume_data
    updated_perfume_data["name"] = "Updated name"
    response = user.client.post(reverse("perfume-update", args=(perfume.id,)), updated_perfume_data)
    assert response.status_code == 302
    assert Perfume.objects.filter(name=updated_perfume_data["name"]).exists()


@pytest.mark.django_db
def test_perfumers_list():
    client = Client()
    response = client.get(reverse("perfumer-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_perfumer_add_not_logged():
    client = Client()
    response = client.get(reverse("perfumer-add"))
    assert response.status_code == 302  # redirect to login page


@pytest.mark.django_db
def test_perfumer_add_logged(user_logged_in):
    response = user_logged_in.client.get(reverse("perfumer-add"))
    assert response.status_code == 403


@pytest.mark.django_db
def test_perfumer_add_logged_superuser(superuser_logged_in):
    user = superuser_logged_in
    response = user.client.get(reverse("perfumer-add"))
    assert response.status_code == 200

    perfumer_count = Perfumer.objects.count()
    new_perfumer = {
        "first_name": "John",
        "last_name": "Faketestlastname"
    }
    response = user.client.post(reverse("perfumer-add"), new_perfumer)
    assert response.status_code == 302
    assert Perfumer.objects.count() == perfumer_count + 1
    assert Perfumer.objects.filter(last_name=new_perfumer["last_name"]).exists()


@pytest.mark.django_db
def test_note_list():
    client = Client()
    response = client.get(reverse("note-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_note_add_not_logged():
    client = Client()
    response = client.get(reverse("note-add"))
    assert response.status_code == 302  # login page


@pytest.mark.django_db
def test_note_add_logged(user_logged_in):
    response = user_logged_in.client.get(reverse("note-add"))
    assert response.status_code == 403

    response = user_logged_in.client.post(reverse("note-add"), {"name": "note name"})
    assert response.status_code == 403


@pytest.mark.django_db
def test_note_add_logged_superuser(superuser_logged_in):
    user = superuser_logged_in
    note_count = Note.objects.count()
    response = user.client.get(reverse("note-add"))
    assert response.status_code == 200

    response = user.client.post(reverse("note-add"), {"name": "weird note"})
    assert response.status_code == 302
    assert Note.objects.count() == note_count + 1
    assert Note.objects.filter(name="weird note").exists()


@pytest.mark.django_db
def test_collection_list(user_logged_in):
    user = user_logged_in
    response = user.client.get(resolve_url("userperfume-list", user.id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_collection_add_logged(user_logged_in, set_up, new_userperfume_data):
    collection_count = UserPerfume.objects.count()

    response = user_logged_in.client.post(reverse(
        "userperfume-add",
        args=(new_userperfume_data["perfume"].id,)),
        new_userperfume_data)

    assert response.status_code == 302
    assert UserPerfume.objects.count() == collection_count + 1

    assert UserPerfume.objects.filter(perfume=new_userperfume_data["perfume"]).exists()


@pytest.mark.django_db
def test_collection_update_logged(user_logged_in, set_up, new_userperfume_data):
    user = user_logged_in
    UserPerfume.objects.create(**new_userperfume_data)
    userperfume = UserPerfume.objects.filter(user=user).first()

    # get update page
    response = user.client.get(reverse("userperfume-update", args=(userperfume.id,)))
    assert response.status_code == 200

    # update data
    updated_userperfume_data = {
        "user": user,
        "perfume": userperfume.perfume,
        "volume": 75,
        "status": "almost full",
        "to_exchange": False
    }
    response = user.client.post(reverse("userperfume-update", args=(userperfume.id,)),
                                updated_userperfume_data)
    assert response.status_code == 302

    # check if updated
    updated_userperfume = UserPerfume.objects.get(id=userperfume.id)
    assert updated_userperfume.volume == updated_userperfume_data["volume"]
    assert updated_userperfume.status == updated_userperfume_data["status"]


@pytest.mark.django_db
def test_collection_delete_logged(user_logged_in, set_up, new_userperfume_data):
    user = user_logged_in
    UserPerfume.objects.create(**new_userperfume_data)
    userperfume = UserPerfume.objects.filter(user=user).first()

    # get delete page
    response = user.client.get(reverse("userperfume-delete", args=(userperfume.id,)))
    assert response.status_code == 200

    # delete item when confirm = "Yes"
    response = user.client.post(reverse("userperfume-delete", args=(userperfume.id,)), {"confirm": "Yes"})
    assert response.status_code == 302
    assert userperfume.id not in [item.id for item in UserPerfume.objects.all()]


@pytest.mark.django_db
def test_offer_list_not_logged():
    client = Client()
    response = client.get(reverse("offer-list"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_offer_list_logged(user_logged_in):
    response = user_logged_in.client.get(reverse("offer-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_offer_list_logged_superuser(superuser_logged_in):
    response = superuser_logged_in.client.get(reverse("offer-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_offer_list_by_user_logged(user_logged_in, set_up):
    user = User.objects.order_by('?').first()
    response = user_logged_in.client.get(reverse("offer-list-by-user", args=(user.id,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_offer_add_logged(user_logged_in, set_up, new_userperfume_data):
    user = user_logged_in
    offer_count = SwapOffer.objects.count()
    UserPerfume.objects.create(**new_userperfume_data)
    userperfume = UserPerfume.objects.filter(user=user).first()

    # get add offer page
    response = user.client.get(reverse("offer-add"))
    assert response.status_code == 200

    # post - .id when using form
    offer_data = {
        "offering_perfume": userperfume.id,
        "requested_perfume": Perfume.objects.order_by('?').first().id,
        "is_completed": False
    }
    response = user.client.post(reverse("offer-add"), offer_data)
    assert response.status_code == 302

    # test if created
    assert SwapOffer.objects.count() == offer_count + 1
    assert SwapOffer.objects.filter(offering_perfume=userperfume,
                                    requested_perfume=offer_data["requested_perfume"]).exists()


@pytest.mark.django_db
def test_offer_update_logged(user_logged_in, set_up, new_userperfume_data):
    user = user_logged_in
    UserPerfume.objects.create(**new_userperfume_data)
    userperfume = UserPerfume.objects.filter(user=user).first()
    # create offer - objects when creating directly
    offer_data = {
        "offering_perfume": userperfume,
        "requested_perfume": Perfume.objects.order_by('?').first(),
    }
    offer = SwapOffer.objects.create(**offer_data)

    # get update page
    response = user.client.get(reverse("offer-update", args=(offer.id,)))
    assert response.status_code == 200

    # update data - object.id when using form
    updated_offer_data = {
        "offering_perfume": userperfume.id,
        "requested_perfume": Perfume.objects.order_by('?')[2].id,
    }
    response = user.client.post(reverse("offer-update", args=(offer.id,)), updated_offer_data)
    assert response.status_code == 302

    # check if updated
    updated_offer = SwapOffer.objects.get(id=offer.id)
    assert updated_offer.requested_perfume.id == updated_offer_data["requested_perfume"]


@pytest.mark.django_db
def test_offer_close_logged(user_logged_in, set_up, new_userperfume_data):
    user = user_logged_in
    UserPerfume.objects.create(**new_userperfume_data)
    userperfume = UserPerfume.objects.filter(user=user).first()
    # create offer - objects when creating directly
    offer_data = {
        "offering_perfume": userperfume,
        "requested_perfume": Perfume.objects.order_by('?').first(),
    }
    offer = SwapOffer.objects.create(**offer_data)

    # get update page
    response = user.client.get(reverse("offer-close", args=(offer.id,)))
    assert response.status_code == 200

    # update data - object.id when using form
    response = user.client.post(reverse("offer-close", args=(offer.id,)), {"confirm": "Yes"})
    assert response.status_code == 302

    # check if closed
    closed_offer = SwapOffer.objects.get(id=offer.id)
    assert closed_offer.is_completed


@pytest.mark.django_db
def test_offer_close_unauthorized_user(user_logged_in, set_up):
    user = user_logged_in
    # pick random other user who is not user
    other_user = None
    while other_user is None or other_user == user:
        other_user = User.objects.order_by('?').first()

    # create userperfume and offer for the other_user

    userperfume_data = {
        "user": other_user,
        "perfume": Perfume.objects.order_by('?').first(),
        "volume": 50,
        "status": "full",
        "to_exchange": False
    }
    userperfume = UserPerfume.objects.create(**userperfume_data)

    offer_data = {
        "offering_perfume": userperfume,
        "requested_perfume": Perfume.objects.order_by('?').first(),
    }
    offer = SwapOffer.objects.create(**offer_data)

    # get update page by user who is not the owner of the offer - should cause 403 forbidden
    response = user.client.get(reverse("offer-close", args=(offer.id,)))
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_add():
    client = Client()
    response = client.get(reverse("user-add"))
    assert response.status_code == 200
    user_count = User.objects.count()

    user_data = {
        "username": "alreadytaken",
        "email": "already.taken@django.com",
        "password1": "password123",
        "password2": "password123"
    }
    response = client.post(reverse("user-add"), user_data)
    assert response.status_code == 302

    # test if created
    assert User.objects.count() == user_count + 1
    assert User.objects.filter(username=user_data["username"]).exists()


@pytest.mark.django_db
def test_user_login(user_logged_in):
    User.objects.create_user(username='test_user_login', password='test_password')
    client = Client()
    response = client.get(reverse("user-login"))
    assert "Login" in response.content.decode()
    assert response.status_code == 200

    user_data = {
        "username": 'test_user',
        "password": 'test_password'
    }
    response = client.post(reverse("user-login"), user_data)
    assert response.status_code == 302
    # test if logout possibility is active
    response = client.get(reverse("index"))
    assert "Login" not in response.content.decode()
    assert "Logout" in response.content.decode()


@pytest.mark.django_db
def test_user_logout(user_logged_in):
    user = user_logged_in
    response = user.client.get(reverse("user-logout"))
    assert response.status_code == 302
    # test if login possibility is active
    response = user.client.get(reverse("index"))
    assert "Login" in response.content.decode()
    assert "Logout" not in response.content.decode()


@pytest.mark.django_db
def test_user_list_not_logged():
    client = Client()
    response = client.get(reverse("user-list"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_list_logged(user_logged_in):
    response = user_logged_in.client.get(reverse("user-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_message_list_not_logged():
    client = Client()
    response = client.get(reverse("message-list"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_message_list_logged(user_logged_in):
    user = user_logged_in
    response = user.client.get(reverse("message-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_message_details_logged(user_logged_in, set_up):
    user = user_logged_in

    message = Message.objects.filter(sender=user).order_by("-timestamp").first()
    response = user.client.get(reverse("message-details", args=(message.id,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_message_respond_logged(user_logged_in, set_up):
    user = user_logged_in
    message_count = Message.objects.count()

    message = Message.objects.filter(receiver=user).order_by("-timestamp").first()
    response_data = {
        'sender': user,
        'receiver': message.sender,
        'content': "test response content"
    }
    response = user.client.post(reverse("message-details", args=(message.id,)), response_data)
    assert response.status_code == 302
    assert Message.objects.count() == message_count + 1
    assert Message.objects.filter(content=response_data["content"]).exists()

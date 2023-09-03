from scent_app.models import Message


def message_icon(request):
    """
    A context processor that adds a variable indicating whether the current user has unread messages.
    """
    if request.user.is_authenticated:
        unread_messages = Message.objects.filter(receiver=request.user, is_read=False)
        unread_messages_exist = unread_messages.exists()
    else:
        unread_messages_exist = False

    return {'unread_messages_exist': unread_messages_exist}

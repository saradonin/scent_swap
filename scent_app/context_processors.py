from scent_app.models import Message


def message_icon(request):
    """
    A context processor that adds a variable indicating whether the current user has unread messages.
    """
    unread_messages_exist = request.user.is_authenticated and Message.objects.filter(
        receiver=request.user, is_read=False).exists()
    return {'unread_messages_exist': unread_messages_exist}

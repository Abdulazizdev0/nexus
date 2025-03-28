def use_context(request):
    return {
        'user': request.user,
        'username': ''
    }
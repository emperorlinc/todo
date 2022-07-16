from django.shortcuts import redirect

def already_login(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        return func(request, *args, **kwargs)
    return wrapper

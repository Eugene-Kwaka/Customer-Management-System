from django.http import HttpResponse
from django.shortcuts import redirect


# This decorator will be placed above RegisterPge & LoginPage as it is meant to lead a user to either Home page or the said view pages.
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# This decorator is for the allowed roles where some pages will be available for only the 'Admin' or the 'Customer'
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


# This decorator is for the Dashboard which is for the 'Admin alone'
def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user_page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func

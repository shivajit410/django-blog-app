from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # TODO log the user
            login(request, user)
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # TODO login the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:article')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:article')

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('blog:article')  # TODO login page
#     template_name = 'accounts/signup.html'

# class LoginView(FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('blog:article')  # TODO login page
#     template_name = 'accounts/login.html'


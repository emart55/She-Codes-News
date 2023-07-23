from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class MyAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'my_account.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
    def my_account_view(request):
        user = request.user
        account_activated_duration = timezone.now() - user.date_joined
        return render(request, 'my_account.html', {'user': user, 'account_activated_duration': account_activated_duration})

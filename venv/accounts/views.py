from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import get_user_model

from .forms import UserSignUpForm

User = get_user_model()

class UserSignUpView(View):
    model = User
    form_class = UserSignUpForm
    success_url = reverse_lazy('posts:list')
    template_name = "accounts/signup.html"
#
#     def get(self, request):
#         pass


from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class HelloView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'message': "Hello World",
        }
        return TemplateResponse(request, 'accounts/hello.html', context)

hello = HelloView.as_view()
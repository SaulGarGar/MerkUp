from django.shortcuts import render
from form.forms import Log_user
from django.views.generic.edit import FormView

class UserView(FormView):
    template_name = 'formulario.html'
    form_class = User
    success_url = '/thanks/'

# Create your views here.
def post_new(request):
        form = Log_user()
        return render(request, '/MerkUp/formulario.html', {'form': form})
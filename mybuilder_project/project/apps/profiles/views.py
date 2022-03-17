from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin   # CBV
from django.views import generic    # CBV
from .forms import UserModelForm
from .models import User

# Create your views here.
class edit_user(LoginRequiredMixin, generic.UpdateView):
    template_name = 'profiles/edit_user.html'
    context_object_name = 'object' 
    form_class = UserModelForm

    def get_queryset(self):
        print('update myaccount queryset')
        print(self.request.user.id)
        return User.objects.filter(pk=self.request.user.id)   # user=self.request.user
        # return get_user_model()
        
    def post(self, request, pk):
        print('update myaccount post')
        object = User.objects.get(pk=pk)
        form = UserModelForm(request.POST or None, instance=object)

        if form.is_valid():
            object = form.save()
            # return object.get_detail_url  # don't know how to get this to work yet
            return redirect("home")
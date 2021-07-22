from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from .models import Tasks
from .forms import AddTask

# Create your views here.
class AddTask(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = ["task"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddTask, self).form_valid(form)

class UserTaskList(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = "users/home.html"
    context_object_name = "works"

    def get_queryset(self):
        name = self.request.user
        return Tasks.objects.filter(author=name.id)

def userregister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("username")
            messages.success(request, f"Account for {name} created successfully!")
            return redirect("user-login")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form":form})

def userlogout(request):
    messages.info(request, "You have logged out!")
    redirect("user-login")

@login_required
def deletetask(request):
    if request.method == "POST":
        task_id = request.POST.getlist("instance")
        for tid in task_id:
            Tasks.objects.filter(author=request.user.id).get(id=tid).delete()
    return redirect("user-home")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateAccountForm

# Create your views here.
@login_required
def view(request):
    if request.method == "GET":
        user = User.objects.get(id=request.user.id)
        form = UpdateAccountForm(instance=user)
        return render(request, "account/view.html", {"form": form})
    else:
        form = UpdateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:view")
        else:
            user = User.objects.get(id=request.user.id)
            form = UpdateAccountForm(instance=user)
            return render(request, "account/view.html", {"form": form})
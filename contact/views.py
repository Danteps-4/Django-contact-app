from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Contact
from .forms import ContactForm

# Create your views here.
def view(request):
    contacts = Contact.objects.filter(created_by=request.user)
    query = request.GET.get("query", "")

    if query:
        contacts = contacts.filter(Q(name__icontains=query) | Q(email__icontains=query))

    return render(request, "contact/view.html", {"contacts": contacts, "query": query})

def detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, created_by=request.user)
    if request.method == "GET":
        form = ContactForm(instance=contact)
        return render(request, "contact/detail.html", {"contact":contact, "form": form})
    else:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact:view")
        else:
            form = ContactForm(instance=contact)
            return render(request, "contact/detail.html", {"contact":contact, "form": form, "error": "Invalid data"})
        
def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.created_by = request.user
            contact.save()
            return redirect("contact:view")
        else:
            form = ContactForm()
            return render(request, "contact/create.html", {"form": form, "error": "Invalida data"})
    else:
        form = ContactForm()
        return render(request, "contact/create.html", {"form": form})
    
def delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, created_by=request.user)
    contact.delete()
    return redirect("contact:view")
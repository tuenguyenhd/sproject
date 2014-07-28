from django.shortcuts import render
from django.views.generic import ListView
from scontacts.models import Contact

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    
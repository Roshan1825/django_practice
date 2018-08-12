from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from django.http import HttpResponse

# Create your views here.

def index(request):
   latest_note_list = Notes.objects.order_by('-created_date')[:5]
   context = {'latest_note_list': latest_note_list}
   return  render(request, 'lists/index.html', context)


def detail(request, note_id):
   note = get_object_or_404(Notes, pk=note_id)
   return render(request, 'lists/detail.html', {'note': note})

def list_add_edit(request):
   if request.method == "POST":
      title = request.POST.get("title")
      description = request.POST.get("description")
      Notes.objects.create(title=title, description=description)
      messages.success(request, "Note has been succesfully created")
      print("Notes created")
      return redirect('lists')
   return render(request, 'lists/list_add_edit.html')
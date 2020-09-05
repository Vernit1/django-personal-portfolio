from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    if request.method=="GET":
        notes = Note.objects.all()
        return render(request, 'keepnote/home.html', {'notes':notes})
    else:
        try:
            note=NoteForm(request.POST)
            newnote = note.save(commit=False)
            newnote.user = request.user
            newnote.save()

            return redirect('keepnote:home')
        except ValueError:
            return render(request, 'keepnote/home.html', {'note':Note(), 'error':'Bad data passed in, Try again'})

def login(request):
    if request.user.is_authenticated:
        return redirect('keepnote:home')
    return render(request, 'keepnote/login.html')

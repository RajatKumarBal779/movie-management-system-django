from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def list_movies(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/movies_list.html',{'movies_list':movies_list})

def add_movie_view(request):
    if request.method == "POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Record Inserted Successfully.")
    form=MovieForm()
    return render(request,'testapp/addmovie.html',{'form':form})
    
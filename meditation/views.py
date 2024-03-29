from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import YogaArticle
@login_required(login_url='accounts:login')
def meditation(request):
    return render(request,'meditation/meditation.html')

@login_required(login_url='accounts:login')
def yoga_main(request):
    yoga_articles = YogaArticle.objects.all()
    context = {'articles':yoga_articles}
    return render(request,'meditation/yoga_main.html',context)

@login_required(login_url='accounts:login')
def yoga_detailed(request,pk):
    article = YogaArticle.objects.get(id=pk)
    context = {'article':article}
    return render(request,'meditation/yoga_detailed.html',context)


    
@login_required(login_url='accounts:login')
def breathing_app(request):
    return render(request,'meditation/breathing_app.html')




@login_required(login_url='accounts:login')
def music_meditation(request):
    return render(request,'meditation/music_meditation.html')
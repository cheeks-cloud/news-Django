from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt 
from .models import Article,NewsLetterRecipients
from .forms import NewsLetterForm

def news_of_day(request):
    date = dt.date.today()
  
    return render(request,'all-news/todays-news.html', {"date":date})


def past_days_news(request,past_date):
        # Converts data from the string Url
    try:
        #useing the date function we convert the stringfrom the url into a dateobject
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        #raise 404 if the value error is thrown
        raise Http404
        assert False

    if date == dt.date.today():  
        return redirect(news_today)  

    news = Article.days_news(date)
    return render(request,'all-news/past-news.html',{"date": date,"news":news})

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def article(request,article_id):

    try:
        article = Article.objects.get(id = article_id)
    except Exception:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})


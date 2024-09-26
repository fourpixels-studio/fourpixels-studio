import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from seo_management.models import SEO
from django.views.decorators.debug import sensitive_variables

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"
seo = SEO.objects.get(pk=2)


@sensitive_variables('BLOOMBERG_RAPID_API_KEY')
def fetch_bloomberg_news(keyword):
    headers = {
        "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com",
        "X-RapidAPI-Key": settings.BLOOMBERG_RAPID_API_KEY,
    }

    query_params = {"query": keyword}

    try:
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()
        data = response.json()

        if len(data.get('news', [])) == 0:
            return f'We\'ve got nothing on "{keyword}"', []
        else:
            return keyword, data['news'][:20]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bloomberg news: {e}")
        return "Failed to load news. Please try again later.", []


def bloomgerg_news_finder(request):
    loading_text = ""
    news_items = []

    if request.method == 'POST':
        keyword = request.POST.get('search_box', '').strip()
        if keyword:
            loading_text, news_items = fetch_bloomberg_news(keyword)
            return JsonResponse({
                'loading_text': loading_text,
                'news_items': news_items
            })
        else:
            loading_text = "Enter a word to search"
    context = {
        'loading_text': loading_text,
        'news_items': news_items,
        'title_tag': seo.meta_description,
        'meta_description': seo.meta_description,
        'meta_keywords': seo.meta_keywords,
        'meta_thumbnail': seo.meta_thumbnail.url,
    }

    return render(request, 'bloomgerg_news_finder.html', context)

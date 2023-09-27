from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Page, MenuItem, RealEstatePage

def home(request):
    articles = Article.objects.filter(show_on_home=True)
    menu_items = MenuItem.objects.filter(show_in_menu=True).order_by('order')
    context = {
        'articles': articles,
        'menu_items': menu_items,
    }
    return render(request, 'home.html', context)


def page_detail(request, slug):
    page = Page.objects.get(slug=slug)
    menu_items = MenuItem.objects.filter(show_in_menu=True).order_by('order')
    context = {
        'page': page,
        'menu_items': menu_items,
    }
    return render(request, 'page_detail.html', context)


def real_estate_page_detail(request, slug):
    real_estate_page = get_object_or_404(RealEstatePage, slug=slug)
    articles = real_estate_page.articles.all()
    return render(request, 'real_estate_page_detail.html', {'real_estate_page': real_estate_page, 'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    template_name = 'article_detail.html'

    menu_items = MenuItem.objects.filter(show_in_menu=True).order_by('order')

    context = {
        'article': article,
        'menu_items': menu_items,
    }
    return render(request, template_name, context)

def bulk_upload(request, gallery_id):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('images'):
                Image.objects.create(gallery_id=gallery_id, image=image)
            return redirect('image_list', gallery_id=gallery_id)
    else:
        form = ImageUploadForm()

    return render(request, 'bulk_upload.html', {'form': form})
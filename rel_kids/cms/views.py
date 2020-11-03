from django.shortcuts import render, HttpResponse, redirect
from .models import Page, Category, Block, Map, FAQ, Link, Encyclopedia_of_knowledge, Connect_with_us, Counter_children, Search
from MainPagePomogut.models import ContactInformation
from collections import defaultdict
import json
from django.contrib.auth.models import User
from django.core.validators import validate_email
from time import time
import re


def get_client_ip(request):#for ip
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(ip)


def get_my_please_pages(request):
    req = request.GET['categories']
    req = eval(req)
    res = {}
    for r in req:
        cat = Category.objects.get(id=r)
        pages = Page.objects.filter(category=cat.get_family()).distinct()
        for p in pages:
            res[p.id] = p.title
    res = json.dumps(res, ensure_ascii=False)
    return HttpResponse(res)


def get_pages(request):#ajax
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    phones = [i.phone for i in cont]
    r = request.GET['categories']
    pages = {}
    cat = Category.objects.get(id=r)
    if cat.level == 1:
        for pag in Page.objects.filter(category=cat.get_family()).distinct():
            if pag.is_active():
                pages[pag.title] = [pag.url_img, pag.slug]
    elif cat.level == 2:
        for pag in Page.objects.filter(category=cat):
            if pag.is_active():
                pages[pag.title] = [pag.url_img, pag.slug]
    pages = json.dumps([pages, phones], ensure_ascii=False)
    return HttpResponse(pages)


def category1(request):#ajax
    cats = Category.objects.filter(level=request.GET["lvl"])
    res = {}
    for c in cats:
        res[c.title] = c.id
    res = json.dumps(res, ensure_ascii=False)
    return HttpResponse(res)


def category2(request):#ajax
    r = json.loads(request.GET['categories'])
    cats = {}
    for id in r:
        for c in Category.objects.get(id=id).get_children():
            cats[c.title] = c.id
    cats = json.dumps(cats)
    return HttpResponse(cats)


def getcategory(request):#ajax
    slug = request.GET['slug']
    pag = Page.objects.get(slug=slug)
    cats = [i for i in pag.category.all()]
    cats.extend([i.parent for i in pag.category.all()])
    res = defaultdict(lambda :{})
    for c in cats:
        if c.level == 2:
            res["select#id_category3"].update({c.title:c.id})
        elif c.level == 1:
            res["select#id_category2"].update({c.title:c.id})
    cats = json.dumps(res)
    return HttpResponse(cats)


def get_level_category(request):#ajax
    if request.GET['element']:
        level = Category.objects.get(id=request.GET['element']).level
        return HttpResponse(level)
    return HttpResponse(0)


def get_data_map(request):#ajax
    points = Map.objects.all()
    data = []
    for point in points:
        address = [float(i) for i in point.address.split(',')]
        data.append({"type": "Feature", "id": point.id, "geometry": {"type": "Point", "coordinates": address}, "properties": {"balloonContent":point.description, "hintContent": point.title}})
    data = {"type": "FeatureCollection",  "features": data}
    data = json.dumps(data)
    return HttpResponse(data)


def raiting(request):#ajax
    page = Page.objects.get(id=request.GET['id'])
    stars = page.stars
    stars += int(request.GET['raiting'])
    count = page.count_for_r
    count += 1
    page.raiting = round(stars / count, 2)
    page.stars = stars
    page.count_for_r = count
    page.save()
    return HttpResponse('')


def fortemplate(request):#ajax
    kwargs = {}
    kwargs['cats'] = [i for i in Category.objects.all() if i.level == 0]
    kwargs['cats'].sort(key=lambda x: x.id)
    kwargs['cats'] = [[i.slug, i.id, i.title] for i in kwargs['cats']]
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    kwargs['emails'] = [i.email for i in cont]
    kwargs['links'] = [[i.title, i.link] for i in Link.objects.all()]
    kwargs = json.dumps(kwargs)
    return HttpResponse(kwargs)


def search_ajax(request):#ajax
    name_pages = list(set([i.title for i in Page.objects.all()]))
    name_pages.extend([i.word for i in Search.objects.all()])
    name_pages = json.dumps(name_pages, ensure_ascii=False)
    return HttpResponse(name_pages)


def get_girls(request):
    id = request.GET['url'].split('/')[-2]
    cat = Category.objects.get(id=id)
    try:
        response = {",".join([str(i.id), i.title, i.url_img]):[[j.id, j.title] for j in i.get_children()] for i in cat.get_children()}
    except:
        return HttpResponse(json.dumps({}, ensure_ascii=False))
    response = json.dumps(response, ensure_ascii=False)
    return HttpResponse(response)


def index_handler(request):
    kwargs = {}
    kwargs['cats'] = [i for i in Category.objects.all() if i.level == 0]
    kwargs['cats'].sort(key=lambda x: x.id)
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    kwargs['emails'] = [i.email for i in cont]
    kwargs['links'] = Link.objects.all()
    kwargs['blocks'] = Block.objects.all()
    return render(request, 'page/index.html', kwargs)


def razdel_handler(request, type, slug, id):
    kwargs = {'type':type}
    kwargs['cats']= [i for i in Category.objects.all() if i.level == 0]
    kwargs['cats'].sort(key=lambda x: x.id)
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    kwargs['emails'] = [i.email for i in cont]
    kwargs['links'] = Link.objects.all()
    if type not in ['category', 'block']:
        return render(request, 'error/error.html', kwargs)                                #404
    if type == "category":
        try:
            cat = Category.objects.get(id=id)
        except:
            return render(request, 'error/error.html', kwargs)                            #404
        kwargs['pages'] = [i for i in Page.objects.filter(category=cat.get_children()).distinct() if i.is_active()]
        if cat.flag and cat.level == 0:
            return render(request, "page-in-development/page-in-development.html", kwargs)#development_stage
    elif type == 'block':
        try:
            block = Block.objects.get(id=id)
        except:
            return render(request, 'error/error.html', kwargs)                            #404
        kwargs['pages'] = [i for i in Page.objects.filter(block=block).distinct() if i.is_active()]
        kwargs['title_block'] = block.title
    return render(request, 'page_with_article/articles1.html', kwargs)


def handler404(request):
    kwargs = {}
    kwargs['cats'] = [i for i in Category.objects.all() if i.level == 0]
    kwargs['cats'].sort(key=lambda x: x.id)
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    kwargs['emails'] = [i.email for i in cont]
    kwargs['links'] = Link.objects.all()
    kwargs['error'] = True
    return render(request, 'error/error.html', kwargs)


def search_helper(request):
    kwargs = {}
    kwargs['cats'] = [i for i in Category.objects.all() if i.level == 0]
    kwargs['cats'].sort(key=lambda x: x.id)
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    kwargs['emails'] = [i.email for i in cont]
    kwargs['links'] = Link.objects.all()
    kwargs['error'] = True
    if request.GET:
        name_page = request.GET['search']
        if name_page:
            res = set()
            for name in name_page.lower().split():
                s = Search.objects.filter(word=name)
                if s:
                    s = s[0]
                    res = res | set(s.pages.all())
            pages = [i for i in Page.objects.all() if name_page.lower() in i.title.lower()]
            pages = set(pages) | res
            kwargs['pages'] = [i for i in pages if i.is_active() and i.in_navigation]
            kwargs['response'] = True
        return render(request, 'search/search.html', kwargs)
    return render(request, 'search/search.html', kwargs)


def FAQs(request):
    kwargs = {}
    kwargs['cats'] = [i for i in Category.objects.all() if i.level == 0]
    kwargs['cats'].sort(key=lambda x: x.id)
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    kwargs['emails'] = [i.email for i in cont]
    kwargs['links'] = Link.objects.all()
    kwargs['faqs'] = FAQ.objects.all()
    kwargs['title'] = 'Часто задаваемые вопросы'
    return render(request, 'FAQs/FAQs.html', kwargs)


def Encyclopedia(request):
    kwargs = {}
    kwargs['cats'] = [i for i in Category.objects.all() if i.level == 0]
    kwargs['cats'].sort(key=lambda x: x.id)
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    kwargs['emails'] = [i.email for i in cont]
    kwargs['links'] = Link.objects.all()
    kwargs['faqs'] = Encyclopedia_of_knowledge.objects.all()
    kwargs['title'] = 'Энциклопедия знаний'
    return render(request, 'FAQs/FAQs.html', kwargs)


def widget_form_connect_with_us(request):
    if not re.findall(r'^\+?\d{0,3}\(?\d{2}\)?\d{2,7}$', request.GET['phone'].replace('-', '')):
        return HttpResponse('error_phone')
    try:
        validate_email(request.GET['email'])
    except:
        return HttpResponse('error_email')

    con = Connect_with_us(name=request.GET['name'],
                          phone=request.GET['phone'],
                          text=request.GET['comment'],
                          target_message=request.GET['sell'],
                          email=request.GET['email'])
    con.save()
    return HttpResponse('done')


def counter_children(request):
    #cou = Counter_children(time=time())
    #cou.save()
    x = 86400
    cou = Counter_children.objects.all()[0]
    if time() - cou.time > x:
        cou.couner1 += 1
        cou.couner2 += 1
        cou.couner3 += 1
        cou.time += x
        cou.save()
    cou = [cou.couner1, cou.couner2, cou.couner3]
    cou = json.dumps(cou)
    return HttpResponse(cou)

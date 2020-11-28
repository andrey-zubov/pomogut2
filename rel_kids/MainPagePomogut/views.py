from django.shortcuts import render
from django.http import HttpResponse
from .models import Help_for_addicts_links, Network_security_links, To_contact_us, Partners
from .models import ContactInformation, MainPageBlock
from django.core.validators import validate_email


def hello(request):
    kwargs = {}
    cont = [i for i in ContactInformation.objects.all() if i.flag]
    kwargs['phones'] = [i.phone for i in cont]
    # kwargs['addicts'] = Help_for_addicts_links.objects.all()
    # kwargs['security'] = Network_security_links.objects.all()
    kwargs['partners'] = Partners.objects.all()
    kwargs['page_blocks'] = MainPageBlock.objects.all()
    return render(request, 'MainPage/pomogut-page1.html', kwargs)


def add_the_information_about_us(request):
    try:
        validate_email(request.GET['email'])
    except:
        return HttpResponse('error')
    else:
        to = To_contact_us(email=request.GET['email'], text=request.GET['text'])
        to.save()
        return HttpResponse('done')
# Create your views here.


def admin_choice(request):
    return render(
        request,
        template_name='admin-choicer/index.html'
    )

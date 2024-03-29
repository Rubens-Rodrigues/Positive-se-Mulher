from django.shortcuts import get_object_or_404,render
from store.models import Product, Category
from django.http import HttpResponseRedirect, HttpResponse
from . forms import LeadsFomul, PreInscricaoForm
from django.db import IntegrityError
from . utils import validar_numero_telefone
import logging

logger = logging.getLogger(__name__)

def index(request):
    
    products_anual=Product.objects.filter(status=True, category__name__icontains="anual").values()
    products_mensal=Product.objects.filter(status=True, category__name__icontains="mensal").values()
    categories=Category.objects.all().order_by('name')
    
    # logger.warning(products_anual)
    
    context={
        'products_anual':products_anual,
        'products_mensal':products_mensal,
        'categories':categories,
        'title': 'Positive-se Mulher',
        'form': LeadsFomul,
    }
    
    return render(request, 'home.html', context)

def send_lead(request):
    submitted = False
    erro = False
    if request.method == "POST":
        lead = LeadsFomul(request.POST)
        valida_phone = validar_numero_telefone(request.POST['phone'])
        if valida_phone:
            try: 
                lead.is_valid()
                lead.save()
                # return HttpResponseRedirect('/?submitted=True#form')
                return HttpResponse(status=202)

            except Exception as err:
                erro = lead.errors.items
                print (err)
                # return HttpResponseRedirect(f"/?erro=True#form")
                return HttpResponse(status=409)
        else:
            return HttpResponse(status=400)
    else:
        lead = LeadsFomul
        if 'submitted' in request.GET:
            submitted = True

def pre_inscricao(request):
    if request.method == "POST":
        inscricao = PreInscricaoForm(request.POST)
        valid_telefone = validar_numero_telefone(request.POST['telefone'])
        if valid_telefone:
            try: 
                inscricao.is_valid()
                inscricao.save()
                context = {
                    'title': 'Positive-se Mulher | Grupo WhatsApp',
                    'nome': request.POST['nome']
                }
                return render(request, 'grupo_whatsapp.html', context)
            except Exception as err:
                context = {
                    'title': 'Positive-se Mulher | Pré inscrição',
                    'form': inscricao,
                    'erro': err    
                }
                return render(request, 'pre_inscricao.html', context)
        else:
            context = {
                'title': 'Positive-se Mulher | Pré inscrição',
                'form': inscricao,
                'erro': "Numero de telefone no formato inválido"
            }
            return render(request, 'pre_inscricao.html', context)
    else:
        
        context={
            'title': 'Positive-se Mulher | Pré inscrição',
            'form': PreInscricaoForm,
        }
        return render(request, 'pre_inscricao.html', context)
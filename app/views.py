from django.shortcuts import render
from .card_identify import cardType
import json
import time
from datetime import datetime ,timedelta
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views import View
import os ,requests
from PocketAssist import settings
from PocketAssist.settings import MEDIA_ROOT
from cryptography.fernet import Fernet
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.response import Response
# from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from .models import *
# def cust_403(request,exception=None):
#     return render(request,'page-403.html',{})

# Create your views here.
def subscriptions(request):
    context = {}
    context['segment']='Subscriptions'
    context['page_root']='Applications'
    subscriptions = SubscriptionHistory.objects.all().order_by('end_date')
    print(subscriptions)
    for subscription in subscriptions:
        print(subscription.start_date)
    context['subscriptions']= subscriptions
    
    html_template = loader.get_template('app/subscriptions.html')
    return HttpResponse(html_template.render(context, request))

def accounts(request):
    context = {}
    context['segment']='Accounts'
    context['page_root']='Finance'
    
    html_template = loader.get_template('finance/accounts.html')
    return HttpResponse(html_template.render(context, request))

def transactions(request):
    context = {}
    context['segment']='Transactions'
    context['page_root']='Finance'
    transactions = Transaction.objects.all().order_by('-date_of_transaction')
    context['transactions']= transactions
    html_template = loader.get_template('finance/transactions.html')
    return HttpResponse(html_template.render(context, request))


# ######################################## Dashboards
def index(request):
    context = {}
    context['segment']='index'
    html_template = loader.get_template('dashboards/default.html')
    return HttpResponse(html_template.render(context, request))

def smart_home(request):
    context = {}
    context['segment']='smart-home'
    html_template = loader.get_template('dashboards/smart-home.html')
    return HttpResponse(html_template.render(context, request))

def automotive(request):
    context = {}
    context['segment']='automotive'
    html_template = loader.get_template('dashboards/automotive.html')
    return HttpResponse(html_template.render(context, request))

def crm(request):
    context = {}
    context['segment']='index'
    html_template = loader.get_template('dashboards/crm.html')
    return HttpResponse(html_template.render(context, request))

def vr(request):
    context = {}
    context['segment']='vr'
    html_template = loader.get_template('dashboards/vr/vr-default.html')
    return HttpResponse(html_template.render(context, request))

def vr_info(request):
    context = {}
    context['segment']='vr-info'
    html_template = loader.get_template('dashboards/vr/vr-info.html')
    return HttpResponse(html_template.render(context, request))


# ######################################## Authentication


def error_404(request):
    context = {}
    context['segment']='error_404'
    html_template = loader.get_template('authentication/error/404.html')
    return HttpResponse(html_template.render(context, request))

def error_500(request):
    context = {}
    context['segment']='error_500'
    html_template = loader.get_template('authentication/error/500.html')
    return HttpResponse(html_template.render(context, request))

def lock_basic(request):
    context = {}
    context['segment']='lock-basic'
    html_template = loader.get_template('authentication/lock/basic.html')
    return HttpResponse(html_template.render(context, request))

def lock_cover(request):
    context = {}
    context['segment']='lock-cover'
    html_template = loader.get_template('authentication/lock/cover.html')
    return HttpResponse(html_template.render(context, request))

def lock_illustration(request):
    context = {}
    context['segment']='lock_illustration'
    html_template = loader.get_template('authentication/lock/illustration.html')
    return HttpResponse(html_template.render(context, request))
# reset
def reset_basic(request):
    context = {}
    context['segment']='reset-basic'
    html_template = loader.get_template('authentication/reset/basic.html')
    return HttpResponse(html_template.render(context, request))

def reset_cover(request):
    context = {}
    context['segment']='reset-cover'
    html_template = loader.get_template('authentication/reset/cover.html')
    return HttpResponse(html_template.render(context, request))

def reset_illustration(request):
    context = {}
    context['segment']='reset_illustration'
    html_template = loader.get_template('authentication/reset/illustration.html')
    return HttpResponse(html_template.render(context, request))

# signin
def signin_basic(request):
    context = {}
    context['segment']='signin-basic'
    html_template = loader.get_template('authentication/signin/basic.html')
    return HttpResponse(html_template.render(context, request))

def signin_cover(request):
    context = {}
    context['segment']='signin-cover'
    html_template = loader.get_template('authentication/signin/cover.html')
    return HttpResponse(html_template.render(context, request))

def signin_illustration(request):
    context = {}
    context['segment']='signin_illustration'
    html_template = loader.get_template('authentication/signin/illustration.html')
    return HttpResponse(html_template.render(context, request))

# signup
def signup_basic(request):
    context = {}
    context['segment']='signup-basic'
    html_template = loader.get_template('authentication/signup/basic.html')
    return HttpResponse(html_template.render(context, request))

def signup_cover(request):
    context = {}
    context['segment']='signup-cover'
    html_template = loader.get_template('authentication/signup/cover.html')
    return HttpResponse(html_template.render(context, request))

def signup_illustration(request):
    context = {}
    context['segment']='signup_illustration'
    html_template = loader.get_template('authentication/signup/illustration.html')
    return HttpResponse(html_template.render(context, request))

# verification
def verification_basic(request):
    context = {}
    context['segment']='verification-basic'
    html_template = loader.get_template('authentication/verification/basic.html')
    return HttpResponse(html_template.render(context, request))

def verification_cover(request):
    context = {}
    context['segment']='verification-cover'
    html_template = loader.get_template('authentication/verification/cover.html')
    return HttpResponse(html_template.render(context, request))

def verification_illustration(request):
    context = {}
    context['segment']='verification_illustration'
    html_template = loader.get_template('authentication/verification/illustration.html')
    return HttpResponse(html_template.render(context, request))


def application_analytics(request):
    context = {}
    context['segment']='analytics'
    html_template = loader.get_template('applications/analytics.html')
    return HttpResponse(html_template.render(context, request))

def application_calendar(request):
    context = {}
    context['segment']='calendar'
    html_template = loader.get_template('applications/calendar.html')
    return HttpResponse(html_template.render(context, request))

def application_datatables(request):
    context = {}
    context['segment']='datatables'
    html_template = loader.get_template('applications/datatables.html')
    return HttpResponse(html_template.render(context, request))

def application_kanban(request):
    context = {}
    context['segment']='kanban'
    html_template = loader.get_template('applications/kanban.html')
    return HttpResponse(html_template.render(context, request))

def application_wizard(request):
    context = {}
    context['segment']='wizard'
    html_template = loader.get_template('applications/wizard.html')
    return HttpResponse(html_template.render(context, request))

def settingspage(request):
    context = {}
    context['segment']='settings'
    html_template = loader.get_template('pages/account/settings.html')
    return HttpResponse(html_template.render(context, request))



    
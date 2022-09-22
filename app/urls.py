from django.urls import path, re_path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [

    path('', index, name='index'),
    path('subscriptions', subscriptions, name='subscriptions'),
    
    # Finance
    path('account-sumary', accounts, name='accounts'),
    path('transactions', transactions, name='transactions'),
    
    path('smart-home', smart_home, name='smart-home'),
    path('automotive', automotive, name='automotive'),
    path('crm', crm, name='crm'),
    path('vr', vr, name='vr'),
    path('vr-info', vr_info, name='vr-info'),
    
    
    path('error-404', error_404, name='error-404'),
    path('error-500', error_500, name='error-500'),
    
    path('lock-basic', lock_basic, name='lock-basic'),
    path('lock-cover', lock_cover, name='lock-cover'),
    path('lock-illustration', lock_illustration, name='lock-illustration'),
    
    path('reset-basic', reset_basic, name='reset-basic'),
    path('reset-cover', reset_cover, name='reset-cover'),
    path('reset-illustration', reset_illustration, name='reset-illustration'),
    
    path('signin-basic', signin_basic, name='signin-basic'),
    path('signin-cover', signin_cover, name='signin-cover'),
    path('signin-illustration', signin_illustration, name='signin-illustration'),
    
    path('signup-basic', signup_basic, name='signup-basic'),
    path('signup-cover', signup_cover, name='signup-cover'),
    path('signup-illustration', signup_illustration, name='signup-illustration'),
    
    path('verification-basic', verification_basic, name='verification-basic'),
    path('verification-cover', verification_cover, name='verification-cover'),
    path('verification-illustration', verification_illustration, name='verification-illustration'),
    
    path('application-analytics', application_analytics, name='application-analytics'),
    path('application-calendar', application_calendar, name='application-calendar'),
    path('application-datatables', application_datatables, name='application-datatables'),
    path('application-kanban', application_kanban, name='application-kanban'),
    path('application-wizard', application_wizard, name='application-wizard'),
    path('settings', settingspage, name='settings'),
    # path('abcd', signup_illustration, name='abcd'),
    # path('abcd', signup_illustration, name='abcd'),
    
]


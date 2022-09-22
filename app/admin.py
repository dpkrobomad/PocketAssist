from django.contrib import admin
from .models import *
    

class CategoryModelAdmin(admin.ModelAdmin):
    list_display= ('name','created_at')


admin.site.register(Category,CategoryModelAdmin)

class TagModelAdmin(admin.ModelAdmin):
    list_display= ('name','created_at')


admin.site.register(Tag,TagModelAdmin)

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display= ('name','category','billing_cycle_days','created_at','updated_at')


admin.site.register(Subscription,SubscriptionModelAdmin)

class SubscriptionHistoryModelAdmin(admin.ModelAdmin):
    list_display= ('subscription','start_date','end_date','amount','created_at','updated_at')


admin.site.register(SubscriptionHistory,SubscriptionHistoryModelAdmin)

class BankAccountModelAdmin(admin.ModelAdmin):
    list_display= ('name','account_number','bank_name','account_type','ifsc_code','mmid','vpa')


admin.site.register(BankAccount,BankAccountModelAdmin)

class CardModelAdmin(admin.ModelAdmin):
    list_display= ('card_name','account','card_number','expire_on','card_type')


admin.site.register(Card,CardModelAdmin)

class PaymentTypeModelAdmin(admin.ModelAdmin):
    list_display= ('name','created_at')
admin.site.register(PaymentType,PaymentTypeModelAdmin)

# class PaymentGatewayModelAdmin(admin.ModelAdmin):
#     list_display= ('name','created_at')
# admin.site.register(PaymentGateway,PaymentGatewayModelAdmin)

class PaymentMethodModelAdmin(admin.ModelAdmin):
    list_display= ('name','payment_type','account')
admin.site.register(PaymentMethod,PaymentMethodModelAdmin)

class TransactionModelAdmin(admin.ModelAdmin):
    list_display= ('name','payment_method','transaction_type','date_of_transaction','date_of_return')
admin.site.register(Transaction,TransactionModelAdmin)

class TransactionCategoryModelAdmin(admin.ModelAdmin):
    list_display= ('name','created_at')
admin.site.register(TransactionCategory,TransactionCategoryModelAdmin)

# class ModelAdmin(admin.ModelAdmin):
#     list_display= ('name','created_at')
# admin.site.register(Category,ModelAdmin)

# class ModelAdmin(admin.ModelAdmin):
#     list_display= ('name','created_at')
# admin.site.register(Category,ModelAdmin)

# class ModelAdmin(admin.ModelAdmin):
#     list_display= ('name','created_at')
# admin.site.register(Category,ModelAdmin)

# class ModelAdmin(admin.ModelAdmin):
#     list_display= ('name','created_at')
# admin.site.register(Category,ModelAdmin)


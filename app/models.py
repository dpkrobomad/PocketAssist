from unicodedata import category
from django.db import models
from datetime import datetime,date

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Categories'
        
    def __str__(self):
        return self.name

class BankAccount(models.Model):
    name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    mmid = models.CharField(max_length=50)
    vpa = models.CharField(max_length=50)
    balance = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'BankAccounts'
    
    def __str__(self):
        return self.name
    
class Card(models.Model):
    card_name = models.CharField(max_length=50)
    account = models.ForeignKey(BankAccount,on_delete=models.RESTRICT)
    card_number = models.CharField(max_length=20)
    expire_on = models.DateField()
    card_type = models.CharField(max_length=10,choices=[('Credit','Credit'),('Debit','Debit')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Cards'
        
    def __str__(self):
        return self.card_name+"-"+self.card_type
    
class PaymentType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'PaymentTypes'
        
    def __str__(self):
        return self.name
    
# class PaymentGateway(models.Model):
    # name = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # class Meta:
    #     db_table = 'PaymentGateways'
        
    # def __str__(self):
    #     return self.name
    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.RESTRICT)
    account = models.ForeignKey(BankAccount, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'PaymentMethods'
        
    def __str__(self):
        return self.name

class TransactionCategory(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'TransactionCategories'
        
    def __str__(self):
        return self.name

class Transaction(models.Model):
    name  = models.CharField(max_length=100)
    category = models.ForeignKey(TransactionCategory,on_delete=models.RESTRICT,default='')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.RESTRICT)
    transaction_type = models.CharField(max_length=20,choices=[('Credit','Credit'),('Debit','Debit'),('Lent','Lent')])
    date_of_transaction = models.DateTimeField()
    date_of_return = models.DateField(null=True,blank=True)
    remark = models.CharField(max_length=255,null=True,blank=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Transactions'
        
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Tags'
    def __str__(self):
        return self.name

    

    
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete=models.RESTRICT)
    billing_cycle_days = models.IntegerField(null=True,blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Subscriptions'
        
    def __str__(self):
        return self.name
    
class SubscriptionHistory(models.Model):
    subscription = models.ForeignKey(Subscription,on_delete=models.RESTRICT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'SubscriptionsHistory'
        
    @property
    def age_in_days(self):
        today = datetime.now().date()
        result = self.end_date.date() - today
        print(self.end_date.date(),today,result.days)
        return result.days
        
    
        
    def __str__(self):
        return self.subscription.name


    
    
    

# Create your models here.

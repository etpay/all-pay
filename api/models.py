from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    # profile_img = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    # id_card_img = models.ImageField(upload_to='id_card_images/', null=True, blank=True)
    email=models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    
    def __str__(self):
        return self.username

class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    # image=models.URLField()
    email = models.EmailField()
    phoneNumber=models.CharField(max_length=20)
    created_by=models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=100)
    tin=models.CharField(max_length=11)
    email = models.EmailField()
    phoneNumber=models.CharField(max_length=20)
    addres=models.CharField(max_length=100)
    created_by=models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.tin

class Service(models.Model):
    serviceProvider = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    regesterationNumber = models.CharField(max_length=20)
    owner=models.CharField(max_length=100)
    uid=models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.regesterationNumber
    
class Bill(models.Model):
    sid = models.ForeignKey(Service,on_delete=models.CASCADE)
    uid = models.ForeignKey(Account,on_delete=models.CASCADE)
    serviceProvider = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    paymentDate=models.DateTimeField(auto_now_add=True)
    amount=models.FloatField()

    def __str__(self):
        return self.amount
    
class PartnerEmploye(models.Model):
    # company_id_card = models.ImageField(upload_to='company_id_card/', null=True, blank=True)
    company_id = models.CharField(max_length=20)
    partner_id = models.ForeignKey(Partner,on_delete=models.CASCADE)
    user_id = models.ForeignKey(Account,related_name='user',on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    created_by=models.ForeignKey(Account,related_name='accountant',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PartnerService(models.Model):
    serviceProvider = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    regesterationNumber = models.CharField(max_length=20)
    owner=models.CharField(max_length=100)
    partnerEmploye=models.ForeignKey(PartnerEmploye,on_delete=models.CASCADE)

    def __str__(self):
        return self.owner

class BillPartner(models.Model):
    pe_id = models.ForeignKey(PartnerEmploye,on_delete=models.CASCADE)
    ps_id = models.ForeignKey(PartnerService,on_delete=models.CASCADE)
    uid = models.ForeignKey(Account,on_delete=models.CASCADE)
    serviceProvider = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner,on_delete=models.CASCADE)
    paymentDate=models.DateTimeField(auto_now_add=True)
    amount= models.FloatField()
    def __str__(self):
        return self.amount

   
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Tbluser(models.Model):
    user_id = models.AutoField(primary_key=True,auto_created=True)
    user_name = models.CharField(max_length=100,unique=True)
    user_password = models.CharField(max_length=100)
    user_status = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    term_date = models.DateField(null=True)

    def __str__(self):
        return self.user_name

class Tblpartner(models.Model):
    partner_id = models.AutoField(primary_key=True, auto_created=True)
    partner_name = models.CharField(max_length=100)
    address_site = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    address_zip = models.CharField(max_length=100)

    def __str__(self):
        return self.partner_name

class Tblbankinfo(models.Model):
    bankinfo_id = models.AutoField(primary_key=True,auto_created=True)
    route_num = models.IntegerField(null=True)
    acct_num = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    bank_loc = models.CharField(max_length=100)
    partner_id = models.IntegerField(null=True)

    def __str__(self):
        return self.bankinfo_id

class Tblinvestment(models.Model):
    investment_id = models.AutoField(primary_key=True,auto_created=True)
    property_id = models.IntegerField(null=True)
    partner_id = models.IntegerField(null=True)
    bankinfo_id = models.IntegerField(null=True)
    equity = models.DecimalField(decimal_places=2,max_digits=12,null=True)
    invest_amt = models.IntegerField(null=True)
    term = models.IntegerField(null=True)
    ret_rate = models.DecimalField(decimal_places=2,max_digits=12,null=True)
    days = models.IntegerField(null=True)
    buy_back_rate = models.IntegerField(null=True)
    distribution = models.DecimalField(decimal_places=2,max_digits=12,null=True)
    start_date = models.DateField(null=True)
    status = models.CharField(default='Active',max_length=100)

    def __str__(self):
        return str(self.equity)

class TblLog(models.Model):
    log_id = models.AutoField(primary_key=True,auto_created=True)
    lg_user_name = models.CharField(max_length=100,null=True)
    lg_date_time = models.DateTimeField(default=datetime.now)
    lg_action = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.lg_user_name

class Tblproperty(models.Model):
    property_id = models.AutoField(primary_key=True,auto_created=True)
    add_site = models.CharField(max_length=100,null=True)
    add_city = models.CharField(max_length=100,null=True)
    add_state = models.CharField(max_length=100,null=True)
    add_zip = models.CharField(max_length=100,null=True)
    purch_price = models.DecimalField(decimal_places=2,max_digits=12,null=True)
    close_date = models.DateField(null=True)

    def __str__(self):
        return self.add_site

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional UserAttributes
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

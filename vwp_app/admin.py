from django.contrib import admin
from vwp_app.models import UserProfileInfo, Tbluser, Tblpartner, Tblbankinfo, Tblproperty, Tblinvestment, TblLog

# Register your models here.
admin.site.register(Tbluser)
admin.site.register(Tblbankinfo)
admin.site.register(TblLog)
admin.site.register(Tblpartner)
admin.site.register(Tblproperty)
admin.site.register(Tblinvestment)
admin.site.register(UserProfileInfo)

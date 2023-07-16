from django.contrib import admin
from loginverify.models import user
# Register your models here.
class usersadmin(admin.ModelAdmin):
    pass

#register Here
admin.site.register(user,usersadmin)
from django.contrib import admin
from testapp.models import port_model
# Register your models here.
class port_admin(admin.ModelAdmin):
    list=['name','email','phone','feedback']
admin.site.register(port_model,port_admin)
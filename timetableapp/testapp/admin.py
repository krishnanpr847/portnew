from django.contrib import admin
from testapp.models import monday_model1# Register your models here.
class monday_admin1(admin.ModelAdmin):
    list=['day','firstperiod','secondperiod','thirdperiod','fourthperiod','fifthperiod','sixthperiod','seventhperiod','eightperiod']

admin.site.register(monday_model1,monday_admin1)

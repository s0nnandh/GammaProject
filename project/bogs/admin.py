from django.contrib import admin
from .models import Person,Group,Membership,Messageship
# Register your models here.
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Messageship)
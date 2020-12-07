from django.contrib import admin
from .models import Person,Group,Membership,Messageship,MessageForm
# Register your models here.
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(MessageForm)
admin.site.register(Messageship)
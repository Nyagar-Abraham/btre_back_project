from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
 list_display = ('id','name','listing','email','contact_date')
 search_fields = ('name','email','listing')
 list_display_links=('id','name')
 list_per_page = 25
 
admin.site.register(Contact,ContactAdmin)
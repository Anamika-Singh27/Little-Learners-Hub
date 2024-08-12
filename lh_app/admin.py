from django.contrib import admin
from .models import FeedBack,Contact,Event,Organization,Parent,Activity, Admission,OrgQr
# Register your models here.

class Feedback_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'ratings')
class Contact_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone') 
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_id', 'email', 'org_name', 'city', 'date')
    search_fields = ('city',)  
    list_filter = ('date',)   
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('activity', 'org', 'student_name')    

admin.site.register(FeedBack,Feedback_Admin)
admin.site.register(Contact,Contact_Admin)
admin.site.register(Event)
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Parent)
admin.site.register(Activity)
admin.site.register(Admission,AdmissionAdmin)
admin.site.register(OrgQr)


admin.site.site_header = "Little Learners Hub DashBoard"
admin.site.site_title = "Little Learners Hub"
admin.site.index_title = " Welcome to Little Learners Hub"



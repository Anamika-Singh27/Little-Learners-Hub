from django.urls import path
from . import views,parent_views,organization_views
urlpatterns =[
path("",views.home,name="home"),  
path("about/",views.about,name="about"),
path("contact/",views.contact,name="contact"),
path('feedback/',views.feedback,name="feedback"),
path("parent_login/",parent_views.login,name="parent_login"),
path("parent_registration/",parent_views.registration,name="parent_registration"),
path("org_registration/",organization_views.registration,name="org_registration"),
path("org_login/",organization_views.login,name="org_login"),
path("events/",views.event_update,name="events"),
path("more_feedback/",views.more_feedback,name="more_feedback"),
path("org_home/",organization_views.org_home,name="org_home"),
path("org_edit_profile/",organization_views.org_edit_profile,name="org_edit_profile"),
path("add_activity/",organization_views.add_activity,name="add_activity"),
path("parent_home/",parent_views.parent_home,name="parent_home"),
path("parent_edit_profile/",parent_views.parent_edit_profile,name="parent_edit_profile"),
path("org_logout/",organization_views.logout,name="org_logout"),
path("parent_logout/",parent_views.logout,name="parent_logout"),
path("all_organizer/",views.all_organizers,name="all_organizer"),
path("views_activity/<str:id>",views.view_activity,name="view_activity"),
path("message/",parent_views.compose,name="compose"),
path("message/",organization_views.compose,name="compose"),
path("parent_inbox/",parent_views.parent_inbox,name="parent_inbox"),
path("org_inbox/",organization_views.org_inbox,name="org_inbox"),
path("search_org/",views.search_org,name="search_org"),
path("parent_all_organizer/",parent_views.all_organizers,name="parent_all_organizer"),
path("parent_views_activity/<str:id>",parent_views.view_activity,name="view_activity"),
path("take_admission/<int:id>/<str:org_id>",parent_views.take_admission,name="take_admission"),
path("take_admission_final/",parent_views.take_admission_final,name="take_admission_final"),
path("upload_qr/",organization_views.upload_qr,name="upload_qr"),
path('checkId/',parent_views.checkId,name="checkId"),
path("show_msg/",parent_views.showmsg,name="show_msg"),
# path("show_msg/",organization_views.showmsg,name="show_msg"),














]
from django.shortcuts import render
from .models import FeedBack,Contact,Event,Organization,Activity
from django.contrib import messages

# Create your views here.

def more_feedback(request):
   feedback_list = FeedBack.objects.all()
   context={
      
      "feedback_list":feedback_list
   }
   return render(request,'lh_app/html/all_feedbacks.html',context)

def home(request):
    #feedback show query here
    feedback_list= FeedBack.objects.order_by('-date')[:3]#descending order data
    context = {'feedback_list' : feedback_list}

    return render(request,'lh_app/html/index.html',context)

def about(request):
    return render(request,'lh_app/html/about_us.html')

def contact(request):

    if request.method == 'GET':

     return render(request,'lh_app/html/contact_us.html')
    
    if request.method == 'POST':
       #fetching data from html controls
        user_name= request.POST["name"]
        user_email= request.POST["email"]
        user_phone= request.POST["number"]
        user_query= request.POST["question"]
        print(user_name, user_email, user_phone, user_query)
        #creating object of contact model
        contact_object=Contact(name=user_name,email=user_email,phone=user_phone,question=user_query)
        #save the object
        contact_object.save()
        messages.success(request,"Thank You for reaching out to us! Andwe will get back to you as soon as possible.")
        return render(request, 'lh_app/html/contact_us.html')

# Feedback--
def feedback(request):

    if request.method == 'GET':

     return render(request,'lh_app/html/feedback.html')
    
    if request.method == 'POST':
       #fetching data from html controls
        user_name= request.POST["name"]
        user_email= request.POST["email"]
        user_feedback= request.POST["feedback"]
        user_rating= request.POST["rating"]
        #print(user_name, user_email, user_feedback, user_rating)
        #creating object of feedback model
        feedback_object=FeedBack(name=user_name,email=user_email,remarks=user_feedback,ratings=user_rating)
        #save the object
        feedback_object.save()
        messages.success(request,"Thank You for Your Feedback and Time!!!!")
        return render(request, 'lh_app/html/feedback.html')
    
def event_update(request):
       
    event_list=Event.objects.all()#select*from event
    #print(type(event_list))
    #how to send data from views to templates

    context={
       "event_key":event_list
    }
       
    return render(request, 'lh_app/html/events_updates.html',context)

def all_organizers(request):
    org_list=Organization.objects.all()
    context={"org_list":org_list}
    return render(request,'lh_app/html/all_organizers.html',context)

def view_activity(request,id):
   activity_list = Activity.objects.filter(org_id=id)
   context={
      
      "activity_list":activity_list
   }
   return render(request,'lh_app/html/view_activity.html',context)

def search_org(request):
        
        if request.method=="GET":
             return render(request,'lh_app/html/search_org.html')
        
        if request.method=="POST":

            scity = request.POST['q']
        print(scity)
        if scity:
            org_list = Organization.objects.filter(city__icontains = scity)
            context = {'org_list' : org_list}
            return render(request,'lh_app/html/view_org.html',context)















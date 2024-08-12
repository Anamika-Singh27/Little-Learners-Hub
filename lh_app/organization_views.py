from django.shortcuts import render,redirect
from.models import Organization,Message,OrgQr
from django.contrib import messages
from django.http import JsonResponse


#edit profile code

def org_edit_profile(request):
     if request.method =="GET":
        id=request.session["session_key"]
        obj= Organization.objects.get(org_id=id)
        context={
         "obj_key":obj
        }
        return render(request,'lh_app/organization/org_edit_profile.html',context) 
     if request.method == "POST":
        nm=request.POST["name"]
        em=request.POST["email"]
        ph=request.POST["phone"] 
        ct=request.POST["city"]
        add=request.POST["address"] 
        id=request.session["session_key"]
        obj= Organization.objects.get(org_id=id)
        obj.name=nm
        obj.email=em
        obj.phone=ph
        obj.city=ct
        obj.address=add
        obj.save()
        context={
         "obj_key":obj
        }
        return render(request,'lh_app/organization/org_home.html',context) 
        
#function for home
def org_home(request):
      id=request.session["session_key"]
      obj= Organization.objects.get(org_id=id)
      context={
         "obj_key":obj
      }
      return render(request,'lh_app/organization/org_home.html',context)  

def login(request):
    if request.method == 'GET':
      return render(request,'lh_app/organization/org_login.html')
    
    if request.method == 'POST':
      user_id=request.POST["user_id"]
      user_pass=request.POST["user_pass"]
      organization_list=Organization.objects.filter(org_id=user_id,password=user_pass)
      size=len(organization_list)
      if size>0:
        print("user exists")
        #Binding id in session
        request.session["session_key"] =user_id
        obj= Organization.objects.get(org_id=user_id)
        context={
           "obj_key":obj
        }
        return render(request,'lh_app/organization/org_home.html',context)  
      else:
        messages.error(request,"Invalid Credentials")
        return render(request,'lh_app/organization/org_login.html')  
    
def registration(request):
  if request.method == 'GET':
    return render(request,'lh_app/organization/org_registration.html')
  if request.method == 'POST':
    #fetching data from html controls
    user_ID= request.POST["id"]
    user_password= request.POST["password"]
    org_name= request.POST["org_name"]
    user_email= request.POST["email"]
    user_phone= request.POST["phone"]
    user_city= request.POST["city"]
    user_address= request.POST["address"]
    owner_name= request.POST["owner_name"]
    about_org= request.POST["about_org"]
  
    print(user_ID, user_password, org_name, user_email, user_phone, user_city,  user_address, owner_name, about_org)
    #creating object of feedback model
    organization_object=Organization(org_id=user_ID,password=user_password, org_name=org_name,email=user_email,phone=user_phone,city=user_city,address=user_address,owner_name=owner_name, about_org=about_org)
    #save the object
    organization_object.save()
    messages.success(request,"Your registration form is successfully summitted!!!!")
    return render(request,'lh_app/organization/org_registration.html')
  
def add_activity(request):
  if request.method =="GET":
    id=request.session["session_key"]
    obj= Organization.objects.get(org_id=id)
    context={
      "obj_key":obj
        }
    return render(request,'lh_app/organization/add_activity.html',context) 
  if request.method == "POST":
      org_id=request.POST["org_id"]
      activity_name=request.POST["activity_name"]
      charge=request.POST["charge"] 
      duration=request.POST["duration"]
      contact=request.POST["contact"] 
      id=request.session["session_key"]
      obj= Organization.objects.get(org_id=id)
      obj.org_id=org_id
      obj.activity_name=activity_name
      obj.charge=charge
      obj.duration=duration
      obj.contact=contact
      obj.save()
      context={
         "obj_key":obj
        }
      return render(request,'lh_app/organization/add_activity.html',context)

def logout(request):
   if "session_key" not in request.session.keys():
      return redirect("org_login")
   request.session.flush()#clearing all the values bind in that session
   return redirect("org_login")#name of the view  

def compose(request):
    if request.method == 'GET':
     return render(request,'lh_app/organization/org_compose.html')
    if request.method == 'POST':
      #fetching data from html controls
      sender_id=  request.session["session_key"] 
      receiver_id= request.POST["receiver_id"]
      subject= request.POST["subject"]
      message= request.POST["message"]

      print(receiver_id, subject, message,)
    #creating object of feedback model
    message=Message(sender_id=sender_id,receiver_id=receiver_id,subject=subject, message=message)
    #save the object
    message.save()
    return render(request,'lh_app/organization/org_compose.html')

def org_inbox(request):
    o_id=  request.session["session_key"] 
    msg_list=Message.objects.filter(receiver_id=o_id)
    
    context={"message_key":msg_list}
    
    return render(request,'lh_app/organization/org_inbox.html',context)

def showmsg(request):
    id=request.GET["msg_id"]
    print("id here is",id)
    m_id=int(id)
    msg_obj=Message.objects.get(id=m_id)
    message_data=msg_obj.message
    context={"m1_key":message_data,
            }
    return JsonResponse(context)

def upload_qr(request):
    if request.method == 'GET':
     return render(request,'lh_app/organization/upload_qr.html')
    if request.method == 'POST':
     org_id=request.session["session_key"] 
     qr_pic= request.FILES.get("qrPic")
     org_object=Organization.objects.get(org_id=org_id)
     org_qr_obj=OrgQr(org=org_object,qr_pic=qr_pic)
     org_qr_obj.save()
     return render(request,'lh_app/organization/upload_qr.html')

   





        

        
  


  

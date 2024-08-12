from django.shortcuts import render,redirect
from.models import Parent,Message, Organization,Activity,Admission,OrgQr
from django.contrib import messages
from django.http import JsonResponse


#edit profile code

def parent_edit_profile(request):
     if request.method =="GET":
        id=request.session["session_key"]
        obj= Parent.objects.get(user_id=id)
        context={
         "obj_key":obj
        }
        return render(request,'lh_app/parent/parent_edit_profile.html',context) 
     if request.method == "POST":
        nm=request.POST["name"]
        em=request.POST["email"]
        ph=request.POST["phone"] 
        ct=request.POST["city"]
        add=request.POST["address"] 
        id=request.session["session_key"]
        obj= Parent.objects.get(user_id=id)
        obj.name=nm
        obj.email=em
        obj.phone=ph
        obj.city=ct
        obj.address=add
        obj.save()
        context={
         "obj_key":obj
        }
        return render(request,'lh_app/parent/parent_home.html',context) 
        

#function for home
def parent_home(request):
      id=request.session["session_key"]
      obj= Parent.objects.get(user_id=id)
      context={
         "obj_key":obj
      }
      return render(request,'lh_app/parent/parent_home.html',context)  

def login(request):
    if request.method == 'GET':
      return render(request,'lh_app/parent/parent_login.html')
    
    if request.method == 'POST':
      user_id=request.POST["user_id"]
      user_pass=request.POST["user_pass"]
      parent_list=Parent.objects.filter(user_id=user_id,password=user_pass)
      size=len(parent_list)
      if size>0:
        print("user exists")
        #Binding id in session
        request.session["session_key"] =user_id
        obj= Parent.objects.get(user_id=user_id)
        context={
           "obj_key":obj
        }
        return render(request,'lh_app/parent/parent_home.html',context)  
      else:
        messages.error(request,"Invalid Credentials")
        return render(request,'lh_app/parent/parent_login.html')  
    
def registration(request):
  if request.method == 'GET':
    return render(request,'lh_app/parent/parent_registration.html')
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
    parent_object=Parent(user_id=user_ID,password=user_password, org_name=org_name,email=user_email,phone=user_phone,city=user_city,address=user_address,owner_name=owner_name, about_org=about_org)
    #save the object
    parent_object.save()
    messages.success(request,"Your registration form is successfully summitted!!!!")
    return render(request,'lh_app/parent/parent_registration.html')
  
def logout(request):
  if "session_key" not in request.session.keys():
    return redirect("parent_login")
  request.session.flush()#clearing all the values bind in that session
  return redirect("org_login")#name of the view  

def compose(request):
    if request.method == 'GET':
     return render(request,'lh_app/parent/parent_compose.html')
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
    return render(request,'lh_app/parent/parent_compose.html')

def parent_inbox(request):
    
    p_id=  request.session["session_key"] 
    msg_list=Message.objects.filter(receiver_id=p_id)
    
    context={"message_key":msg_list}
    return render(request,'lh_app/parent/parent_inbox.html',context)
def showmsg(request):
    id=request.GET["msg_id"]
    print("id here is",id)
    m_id=int(id)
    msg_obj=Message.objects.get(id=m_id)
    message_data=msg_obj.message
    context={"m1_key":message_data,
            }
    return JsonResponse(context)




def all_organizers(request):
    parent_list=Parent.objects.all()
    org_list=Organization.objects.all()
    context={"parent_list":parent_list,"org_list":org_list }
    return render(request,'lh_app/parent/all_organizers.html',context)

def view_activity(request,id):
    organizer_obj=Organization.objects.get(org_id=id)
    qrobj=OrgQr.objects.get(org=organizer_obj)
    activity_list=Activity.objects.filter(org_id=id)
    context={
         "activity_list":activity_list,
         "org_key":qrobj
         }
    return render(request,'lh_app/parent/view_activity.html',context)


def take_admission(request,id,org_id):
    
    if request.method=="GET":
        
      context={"id":id,"org_id":org_id}
      return render(request,'lh_app/parent/admission.html',context)

def take_admission_final(request):
    if request.method == 'POST':
        activity_id=request.POST["activity_id"]
        org_id=request.POST["org_id"]
        student_name = request.POST.get('student_name')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        phone = request.POST.get('phone')
        alternative_phone = request.POST.get('alternative_phone')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        school_name = request.POST.get('school_name')
        admission_mode = request.POST.get('admission_mode')
        if admission_mode=='online':
           payment_screenshot = request.FILES.get('payment_screenshot')
        else:
           payment_screenshot=None
           
        fees= request.POST.get('fees')
        student_photo = request.FILES.get('student_photo')

        # print(student_name,mother_name,father_name,phone,alternative_phone,email,dob,age,gender,school_name,fees,admission_mode,payment_screenshot, qr_code,student_photo )
        activity_obj=Activity.objects.get(id=activity_id)
        org_obj=Organization.objects.get(org_id=org_id)

        admission_object=Admission(activity=activity_obj,org=org_obj,student_name=student_name,mother_name=mother_name,father_name=father_name,phone=phone,alternative_phone=alternative_phone, email= email,dob=dob,age=age,gender=gender,school_name=school_name,admission_mode=admission_mode,fees=fees,payment_screenshot=payment_screenshot,photo=student_photo)
        admission_object.save()
        messages.success(request,"Thank You for Admission! and payment is successfully done.")
        return render(request,'lh_app/parent/admission.html')
    
def checkId(request):
    id = request.GET['user_id']
    print(id)
    context = {'status' : Parent.objects.filter(user_id__iexact = id).exists()}
    return JsonResponse(context)


   





        

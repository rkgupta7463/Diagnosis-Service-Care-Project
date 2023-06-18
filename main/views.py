from django.shortcuts import render,HttpResponse,redirect
import pandas as pd
import pickle as plk
from django.conf import settings
from django.core.mail import send_mail
import socket


hdmodel=plk.load(open('models/Heart Disease.pkl','rb'))
kdc=plk.load(open('models/kidney_model_upgrade.pkl','rb'))
model_ddc=plk.load(open('models/model_gbc.pkl','rb'))

# Create your views here.

def index(request):
    sms=""
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone_no')
        problem=request.POST.get('problems')
        problemsms=request.POST.get('problemsms')
        
        #mail sending system
        try:
            subject = "Diagnosis Service Care Report"
            message = f"Hello {name}, \nThanks to contact with us. \nOur team will contact with soon regarding your problems!\nYour Details\nName :-{name}\nEmail :-{email}\nPhone :-{phone}\nYour Problem is {problem} \nDetails of Company\nCompany name is Diagnosis Service Care \nFeel Free to contact with us by below email\nemail id:-rishukumargupta.offical.com\nHave Good Day Dear🤞"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)  
            sms="Thanks for contacting with us! Our team will contact with you soon."
            # return redirect('index')
        except socket.gaierror:
             print("accuring error while sending mail!")   
             return redirect("index")
    context={
        'sms':sms,
    }
    return render(request,"index.html",context)

##heart disease function
def heart_disease(request):
    rs=None
    fname=""
    lname=""
    fullname=None
    address=None
    mail=None

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        age=request.POST.get('age')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        mail=request.POST.get('mail')
        phone=request.POST.get('phone_no')
        cpt=request.POST.get('cpt')
        bp=request.POST.get('bp')
        fbs=request.POST.get('fbs')
        chol=request.POST.get('Chol')
        ecg=request.POST.get('ecg')
        mhr=request.POST.get('mhr')
        exang=request.POST.get('exang')
        std=request.POST.get('std')
        sst=request.POST.get('sst')
        novf=request.POST.get('novf')
        thal=request.POST.get('thal')

        BP=int(bp)
        CHOL=int(chol)
        FBS=int(fbs)
        ECG=int(ecg)
        MHR=int(mhr)
        EXANG=int(exang)
        
        if hdmodel.predict(pd.DataFrame([[age,gender,cpt,BP,CHOL,FBS,ECG,MHR,EXANG,std,sst,novf,thal]],columns=['Age','Sex','Chest pain type','BP','Cholesterol','FBS over 120','EKG results','Max HR','Exercise angina','ST depression','Slope of ST','Number of vessels fluro','Thallium']))==1:
            rs="Heart Disease Presence"
        else:
            rs="Heart Disease Absecnce"

        ########### Fullname ###################
        fullname=fname+" "+lname   
        ########### End fullname ###############

    context={
        "fullname":fullname,
        "rs":rs,
        "address":address,
        "email":mail, 
    }    
    return render(request,"Heart_Disease.html" ,context)

##kidney function
def kidney(request):
    prediction=None
    fname=""
    lname=""
    fullname=None
    address=None
    email=None
    rs=None
    
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        email=request.POST.get('email')
        bp=request.POST.get('bp')
        sg=request.POST.get('sg')
        al=request.POST.get('Aluminum')
        su=request.POST.get('su')
        Rbc=request.POST.get('Rbc')
        bu=request.POST.get('bu')
        Sc=request.POST.get('Sc')
        Sod=request.POST.get('Sod')
        Pot=request.POST.get('Pot')
        Hemo=request.POST.get('Hemo')
        Wbcc=request.POST.get('Wbcc')
        Rbcc=request.POST.get('Rbcc')
        Htn=request.POST.get('Htn')

        print(gender)

        ##converting integer into float dtype  
        BPF=float(bp)
        SGF=float(sg)
        ALF=float(al)
        SUF=float(su)
        RBCF=float(Rbc)
        BUF=float(bu)
        SCF=float(Sc)
        SODF=float(Sod)
        POTF=float(Pot)
        HEMOF=float(Hemo)
        WBCCF=float(Wbcc)
        RBCCF=float(Rbcc)
        HTNF=float(Htn)

        prediction=kdc.predict(pd.DataFrame([[BPF,SGF,ALF,SUF,RBCF,BUF,SCF,SODF,POTF,HEMOF,WBCCF,RBCCF,HTNF]],columns=['Bp','Sg','Al','Su','Rbc','Bu','Sc','Sod','Pot','Hemo','Wbcc','Rbcc','Htn']))
        
        ########### Fullname ###################
        fullname=fname+" "+lname   
        ########### End fullname ###############
        
        if prediction == 1:
            rs='Patients has no kidney Problem'

        else:
            rs='Patients has kidney Problem'

        #mail sending system
        # try:
        #     subject = "Kidney Disease Testing Application"
        #     message = f"Hello {fullname}, \n Your report is {rs}.\nEmail id : rishukumargupta.offical.com"
        #     email_from = settings.EMAIL_HOST_USER
        #     recipient_list = [email, ]
        #     send_mail(subject, message, email_from, recipient_list)  
        # except socket.gaierror:
        #      print("accuring error while sending mail!")   
        #      return redirect("main")
    
    context={
        "fullname":fullname,
        "rs":rs,
        "address":address,
        "email":email, 
    }    
    return render(request,"kidney_Disease.html",context)


##debates function
def debates(request):
    prediction=None
    fname=""
    lname=""
    fullname=None
    address=None
    mail=None
    rs=None

    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        age=request.POST.get('age')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        mail=request.POST.get('mail')
        phone=request.POST.get('phone_no')
        hyperten=request.POST.get('htn')
        heart_d=request.POST.get('htd')
        sh=request.POST.get('sh')
        bmi=request.POST.get('bmi')
        hbl=request.POST.get('hbl')
        bgl=request.POST.get('bmi')
        AGE=float(age)
        HTN=int(hyperten)
        HTD=int(heart_d)
        BMI=float(bmi)
        HBL=float(hbl)
        BGL=int(bgl)
        

        if model_ddc.predict(pd.DataFrame([[gender,AGE,HTN,HTD,sh,BMI,HBL,BGL]],columns=['gender','age','hypertension','heart_disease','smoking_history','bmi','HbA1c_level','blood_glucose_level']))==1:
            rs="Diabetes Possitive"
        else:
            rs="Diabetes Negative"

        ########### Fullname ###################
        fullname=fname+" "+lname   
        ########### End fullname ###############

    context={
        "fullname":fullname,
        "rs":rs,
        "address":address,
        "email":mail, 
    }          

    return render(request, "debates_Disease.html",context)
##super user username:dell password:None



from email.mime import image
from urllib import response
from urllib.request import Request
from django.conf import Settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer
from zaigo import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from .models import Response_pdf
import PyPDF2
import slate3k as slate
import io
import fitz
from PIL import Image
from PyPDF2 import PdfFileReader,PdfFileWriter
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


# Create your views here.
def home(request):
    return render(request,'inside.html')

def signup(request):



    #myuser.is_active=False                  #user only activates after acceptin confirmation email,set to true to actiate instantly
    #send confirmation email process start
    #subject='this is subject'
    #body='this is body'
    #from_mail=Settings.EMAIL_HOST_USER
    #to_list=[myuser.email]                          #myuser is the object instnce after loin
    #send_mail(subject,body,from_mail,to_list,fail_silently=True)
    pass

def signin(request):
    pass

def signout(request):
    pass

def fileu(request):
    request_file=request.FILES.get('myfile1')
    print('request_file.name is',request_file.name)
    #print('pdffileobj is ',pdffileobj)
    #res_pdf=Response_pdf.objects.create(image_content=request_file)
    #res_pdf.save()
    if request_file:
        fs=FileSystemStorage()
        file=fs.save(request_file.name,request_file)
        fileurl=fs.url(file)
    stri='media/'+request_file.name
    #pdf_file=fitz.open(stri)
    #for page_index in range(len(pdf_file)):
    #    page=pdf_file[page_index]
    #    image_list=page.get_images()
    ##    if image_list:
     #       print('found imes')
     #   else:
     #       print('no ime in current pae')
     #   for image_index,img in enumerate(page.get_images(),start=1):
     #       xref=img[0]
     #       base_image=pdf_file.extract_image(xref)
     #       image_bytes=base_image["image"]
     #       image_ext=base_image["ext"]

    #print('type of base_image is',type(base_image))
    #print('base_image is',base_image)
    #print('image_bytes is',image_bytes)
    #print('image_ext is',image_ext)
    #res_pdf=Response_pdf.objects.create(image_content=image_bytes)
    #res_pdf.save()
    pdffileobj=open(stri,'rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    pageobj=pdfreader.getPage(0)
    print('pageobj is',pageobj)
    print('lettrs is',pageobj.extractText())
    print('pdfreader.numPages is',pdfreader.numPages)
    pdffileobj.close()
    #with open(stri,'rb') as f:
    #    extrctedtext=slate.PDF(f)
    #print('extrctedtext is',extrctedtext)
    #remote_file=urlopen(stri).read()
    #memory_file=io.BytesIO(remote_file)
    #pdf=pdftotext.PDF(memory_file)
    #for p in pdf:
    #    print('p is',p)
    return render(request,'index.html')

class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj ,_ =Token.objects.get_or_create(user=user)
        
        return Response({'status':200,'payload':serializer.data,'message':'success','token':str(token_obj)})
        from rest_framework.authtoken.models import Token
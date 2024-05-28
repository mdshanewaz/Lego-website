from logging.config import valid_ident
from multiprocessing import context
from operator import length_hint
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.contrib import messages
from .forms import ContactForm, DocumentfileForm
#from h11 import Data
from .models import Contact, Documentfile
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# def index(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Thank you for getting in touch!")
#             return redirect("home")
#     return render(request, 'index.html',{"form": form})



class HomeView(CreateView):
    model = Contact
    form_class = ContactForm
    msg_succ = 'Thank you for getting in touch!'
    template_name = "index.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        
        self.object      =      form.save(commit = False)
        self.object.name =      form.cleaned_data["name"]
        self.object.email =     form.cleaned_data["email"]
        self.object.subject =   form.cleaned_data["subject"]
        self.object.message =   form.cleaned_data["message"]
        self.object.save()
        self.form_submitted = True

        context={
            'name': self.object.name, 
            'email': self.object.email,
            'subject': self.object.subject,
            'message': self.object.message,
            # 'form_submitted' : self.object.form_submitted
        }

        #messages.success(self.request, self.msg_succ)

        user_input = "{} {} {} {}".format(context['name'], context['email'], context['subject'], context['message'])

        # send_mail(
        #         subject = "Contact Us Message",
        #         message = user_input, 
        #         from_email = "contact1@resumenalyzer.com", 
        #         recipient_list = [self.object.email, "def274753@gmail.com"]
        #     )
        
        return super(HomeView, self).form_valid(form)
        

        # Resume analysis
        # elif isinstance(form, DocumentfileForm):
        
        #     self.object      =      form.save(commit = False)
        #     self.object.doc_file = form.cleaned_data["doc_file"]
        #     self.object.email =     form.cleaned_data["email"]
            
        #     print(self.object.doc_file, self.object.email)

        #     self.object.save()

        #     context={
        #         'doc_file' : self.object.doc_file,
        #         'email': self.object.email,
        #     }

        #     messages.success(self.request, self.msg_succ)

        #     user_input = "{} {}".format(context['doc_file'],context['email'])

        #     send_mail(
        #             subject = "Upload your most up-to-date resume for a quick analysis free of cost !!!",
        #             message = user_input, 
        #             from_email = "contact@legoio.com", 
        #             recipient_list = [self.object.email, "def274753@gmail.com"]
        #         )
            

        #     return super(HomeView, self).form_valid(form)
    
   

class Press_releaseView(TemplateView):
    template_name = "press_release.html"
    success_url = reverse_lazy('home')





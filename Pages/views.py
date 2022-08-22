from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from Cars.models import Car, Category
from Pages.forms import CarSearchForm,ContactForm
from django .views.generic import ListView,CreateView,FormView
from django.contrib.postgres.search import SearchVector
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class HomeView(ListView):
    model =Car
    template_name ='pages/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
       
        recent_cars = Car.objects.select_related('user','category').filter(status='NOT SOLD',published=True).order_by('-created_date')[:4]
        most_viewed = Car.objects.select_related('user','category').filter(status='NOT SOLD',published=True).order_by('hit_count_generic')[:4]
        categories =Category.objects.all()
        context["recent_cars"] = recent_cars
        context["most_viewed"] = most_viewed
        context['categories']=categories
       
        return context
class ContactView(SuccessMessageMixin, CreateView):
    # model =Contact 
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_message='Your message has been sent. Thank you!'

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

def find(request):
    form = CarSearchForm
    results =[]
    
    # if form.is_valid('self'):
        # form = JobSearchForm(request.GET)
    if request.method =='GET':            
            q=request.GET.get('q')           
            results = Car.objects.select_related('user','category').annotate(search=SearchVector('stock_id','car_make','vendor_county','car_name','body_type','engine_size','year_of_make','mileage','price' ,'vendor_location','vendor_address','drive','transmission'),).filter(published=True,search=q).order_by('-created_date')
            page=request.GET.get('page',1)
            paginator = Paginator(results,20)
            try:
                results =paginator.page(page)
            except PageNotAnInteger:
                results=paginator.page(1)
            except EmptyPage:
                results=paginator.page(paginator.num_pages)
            
    return render(request,'pages/search.html',{'form':form,'results':results,'q':q })

def search(request):
    form = CarSearchForm
    results =[]
    
    if request.method == 'GET':
            
            category= request.GET.get('category',None)
            car_make=request.GET.get('car_make')
            # car_make = form.cleaned_data['car_make']
            
            body_type=request.GET.get('body_type')
            # body_type = form.cleaned_data['body_type']

            car_name=request.GET.get('car_name')
            # car_name = form.cleaned_data['car_name']

            year_of_make =request.GET.get('year_of_make ')
            # year_of_make  = form.cleaned_data['year_of_make ']

            location =request.GET.get('location ')
            # location  = form.cleaned_data['location ']

            results=Car.objects.select_related('user','category').filter(published=True)
            
            if category != '0':
                category=get_object_or_404(Category,pk=category)            
                results = results.filter(category__name__icontains=category.name,published=True ).order_by('-created_date')
                
                if car_make:
                   results = Car.objects.select_related('user','category').annotate(search=SearchVector('car_make'),).filter(published=True,search=car_make).order_by('-created_date')
                if location:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('vendor_county','vendor_location','vendor_address'),).filter(published=True,search=location).order_by('-created_date')
                if year_of_make:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('year_of_make'),).filter(published=True,search=year_of_make).order_by('-created_date')

                if body_type:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('body_type'),).filter(published=True,search=body_type).order_by('-created_date')

                if car_name:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('car_name'),).filter(published=True,search=car_name).order_by('-created_date')
                        
            else:
                if car_make:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('car_make'),).filter(published=True,search=car_make).order_by('-created_date')
                if location:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('vendor_county','vendor_location','vendor_address'),).filter(published=True,search=location).order_by('-created_date')
                if year_of_make:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('year_of_make'),).filter(published=True,search=year_of_make).order_by('-created_date')

                if body_type:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('body_type'),).filter(published=True,search=body_type).order_by('-created_date')

                if car_name:
                    results = Car.objects.select_related('user','category').annotate(search=SearchVector('car_name'),).filter(published=True,search=car_name).order_by('-created_date')
                        
            # results = Job.objects.annotate(search=SearchVector('title','county','location','address','category'),).filter(search=q).order_by('-created_date')
            page=request.GET.get('page',1)
            paginator = Paginator(results,30)
            try:
                results =paginator.page(page)
            except PageNotAnInteger:
                results=paginator.page(1)
            except EmptyPage:
                results=paginator.page(paginator.num_pages)
            
    return render(request,'pages/search.html',{'form':form,'results':results,'car_make':car_make,
    'car_name':car_name,'body_type':body_type,'year_of_make':year_of_make,'location':location })

def error_404(request,exception):
    return render(request,'errors/404.html')

def error_500(request):
    return render(request,'errors/500.html')
 
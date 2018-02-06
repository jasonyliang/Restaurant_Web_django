from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import RestaurantLocation

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
@login_required(login_url='/login/')
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    # if request.method == 'GET':
    #     print('get data')
    # if request.method == 'POST': #PUT
    #     # title = request.POST.get('title')
    #     # location = request.POST.get('location')
    #     # category = request.POST.get('category')
    #     form = RestaurantCreateForm(request.POST)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            form.save()
        # obj = RestaurantLocation.objects.create(
        #     name = form.cleaned_data.get('name'),
        #     location = form.cleaned_data.get('location'),                
        #     category = form.cleaned_data.get('category'),
        #     )
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors
    template_name = 'restaurants/form.html'
    context = { "form": form, "errors": errors}
    return render(request, template_name, context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset,

    }
    return render(request, template_name, context)

def restaurant_detailview(request, slug):
    template_name = 'restaurants/restaurantslocation_detail.html'
    obj = RestaurantLocation.objects.get(slug = slug)
    context = {
        'object': obj,

    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    # template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
                )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()



class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    #login_url = "/login/" can override the setting url
    template_name = 'restaurants/form.html'
    # success_url = "/restaurants/"
    def form_valid(self, form):
        instance = form.save(commit=False)
        #customize
        #like a pre_save
        instance.owner = self.request.user
        #form.save()
        return super(RestaurantCreateView, self).form_valid(form)
    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context







    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) #pk = rest_id
    #     return obj
# class SearchRestaurantListView(ListView):
#     template_name = 'restaurants/restaurants_list.html'
    
#     def get_queryset(self):
#         print(self.kwargs)
#         slug = self.kwargs.get("slug")
#         if slug:
#             queryset = RestaurantLocation.objects.filter(
#                 Q(category__iexact=slug) |
                
#                 Q(category__icontains=slug)
#                 )
#         else:
#             queryset = RestaurantLocation.objects.none()

#         return queryset















# Create your views here.
#function based view

# def home(request):
#     html_var = "fstrings, testing..."
#     html_ = f'''
#     <!DOCTYPE html>
#     <html lang=en>

#     <head>
#     </head>
#     <body>
#     <h1>Hellow World</h1>
#     <p> This is {html_var} from Django<p>

#     </body>
#     </html>

#     '''
#     #f strings

#     return HttpResponse(html_)
#     #return render(request, "home.html", {})#response


# def home(request):
#     randnum = None
#     some_list = [random.randint(1, 20000), random.randint(1, 20000), random.randint(1, 20000)]

#     condition_bool_item = True
#     if condition_bool_item:
#         randnum = random.randint(1, 20000)
#     context = {
#         'html_var': "context", 
#         'number': randnum, 
#         'some_list': some_list
#     }
#     return render(request, "home.html", context)#response

# def about(request):
#     context = {
#     }
#     return render(request, "about.html", context)#response



# def contact(request):
#     context = {
#     }
#     return render(request, "contact.html", context)#response

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)

# class HomeView(TemplateView):
#     template_name = 'home.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     randnum = None
    #     some_list = [random.randint(1, 20000), random.randint(1, 20000), random.randint(1, 20000)]

    #     condition_bool_item = True
    #     if condition_bool_item:
    #         randnum = random.randint(1, 20000)
    #     context = {
    #         'html_var': "context", 
    #         'number': randnum, 
    #         'some_list': some_list
    #     }
    #     return context
# class AboutView(TemplateView):
#     template_name = 'about.html'


# class ContactView(TemplateView):
#     template_name = 'contact.html'
    # def post(self, request, *args, **kwargs):
    #     context = {}
    #     return render(request, "contact.html", context)

    # def put(self, request, *args, **kwargs):
    #     context = {}
    #     return render(request, "contact.html", context)
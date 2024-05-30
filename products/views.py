from .forms import  ContactForm, ProductForm
from products.models import  Product,Order,Contact
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import LoginView
from django.contrib import messages

@login_required(login_url='Hd2')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")

        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('Hd2')

    return render (request,'products/signup.html')

def LogoutPage(request):
    logout(request)
    return redirect('Hd2')

def home(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        products = Product.objects.filter(name__icontains=item_name)
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        products = paginator.get_page(page)
    return render(request, 'products/home.html', {'products': products})

def hd(request):
    return render(request, 'products/Hd2.html')
    
class CustomLoginView(LoginView):
    template_name = 'products/Hd2.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Incorrect username or password.')
        return super().form_invalid(form)

@login_required

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    
    return render(request, 'products/create_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

    
@login_required
def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products:home')
    return render(request, 'products/delete_product.html', {'product': product})


def detail(request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': products})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        ord = Order(items=items,name=name, email=email,
                    city=city, state=state, zipcode=zipcode, total=total)
        ord.save()
        return redirect("confirm")
    return render(request, 'products/checkout.html')

def confirm(request):
    info= Order.objects.all()[:1]
    for item in info:
        name=item.name
    return render(request, 'products/confirm.html',{'name': name})


def about(request):
    return render(request,'products/about.html')

@csrf_protect

def contact(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Créer une instance du modèle Contact
        contact = Contact(name=name, email=email, subject=subject, message=message)

        # Enregistrer l'instance dans la base de données
        contact.save()

        # Afficher un message de succès ou effectuer d'autres actions

    return render(request, 'products/contact.html')



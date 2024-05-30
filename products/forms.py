from django import forms
from .models import  Product, Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'date_creation', 'date_modification', 'image')
        widgets = {
            'date_creation': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'date_modification': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select category'


class ContactForm(forms.Form):
    name = forms.CharField(label='Full Name')
    email = forms.EmailField(label='Email Address')
    subject = forms.CharField(label='Subject')
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)


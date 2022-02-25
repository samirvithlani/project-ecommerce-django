from django import forms

from .models import Brand, Category, Product

class ProductAddForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('is_deleted',)
        # widgets = {'name': forms.CharField(attrs = {'class': 'form-group',
        #                                             'id' : 'name',
        #                                             'name': 'product_name',})}
    # def clean_
class ProductBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name',)
    
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

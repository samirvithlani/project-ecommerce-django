from django.views.generic import  ListView

from .forms import *
from generic.views import *
# from ecommerce.adminportal.product.models import ProductImage
from django.db.models.query_utils import Q

# Create your views here.

#------------------------------Product-Brand------------------------------------#

class BrandCreateView(BaseCreateView, BaseAdminMixin):

    form_class = ProductBrandForm
    model = Brand
    template_name = "adminportal/brand.html"
    # success_url = '/admin_customized/'
    context_object_name = 'brand'

class UpdateBrandView(BaseAdminMixin, BaseUpdateView):

    model = Brand
    form_class = ProductBrandForm

class DeleteBrandView(BaseAdminMixin, BaseDeleteView):

    model = Brand


#------------------------------Product-Category------------------------------------#

class CategoryCreateView(BaseCreateView, BaseAdminMixin):

    form_class = ProductCategoryForm
    model = Category
    template_name = "adminportal/category.html"
    context_object_name = 'category'

class UpdateCategoryView(BaseAdminMixin, BaseUpdateView):

    model = Category
    form_class = ProductCategoryForm

class DeleteCategoryView(BaseAdminMixin,BaseDeleteView):

    model = Category

#------------------------------Product-Filter/Search/Single-Product------------------------------------#

class CategoryBrandFilterView(ListView):

    model = Product
    template_name = 'userportal/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        context["category"] = Category.objects.all()
        return context 

    def get_queryset(self):
        category = self.request.GET.get('category', None)
        brand = self.request.GET.get('brand', None)
        # category = get_object_or_404(Category, pk=self.kwargs['pk'])
        products = Product.objects.all()

        if category and not brand:
            products = products.filter(Q(category__name = category) )
        elif not category and brand:
            products = products.filter(Q(brand__name = brand))        
        elif category and brand:
            products = products.filter(Q(category__name = category) & Q(brand__name = brand))

        return products  

class SearchView(BaseListView):

    model = Product
    template_name = 'userportal/search.html'
    context_object_name = 'products'
    # context_object_name = 'q'

    def get_queryset(self):
        search = self.request.GET.get('q')
        print("search", search)
        if search:
            products = Product.objects.filter(Q(name__icontains=search ) | Q(price__icontains=search) |
                                             Q(brand__name__icontains=search) | Q(category__name__icontains=search)).order_by('created_at')
        else:
            products = Product.objects.none()
        return products

class SingleProductView(BaseDetailView):
    model = Product
    template_name = 'userportal/single_product.html'





 # def form_valid(self, form):
    #     product = form.save()
    #     if 'image' in request.FILES:
    #         ProductImage(
    #             product = product,
    #             image= image
    #         )
    #         product.image = request.FILES['image']
    #         ProductImage.save()
    #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         product = form.save()
    #         if 'image' in request.FILES:
    #             product.image = request.FILES['image']
    #         product.save()
    #         registered = True
    #         messages.success(request, 'Product was created successfully!')

    #         return redirect('user_urls:admin_customized')
from django.urls import path
from .views import * 
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user_urls'


urlpatterns = [
    path('', HomeView.as_view(),name='index'),
    path('admin_customized/', AdminHomeView.as_view(),name='admin_customized'),

    path('cart/',views.CartListView.as_view(),name='cart'),
    path('add_to_cart/',views.AddToCartView.as_view(),name='add_to_cart'),
    path('checkout/',views.CheckoutView.as_view(),name='checkout'),
    path('checkout-1/',AddressView.as_view(), name='address'),
    path('confirm/',EmailSendView.as_view(), name='email'),

    path('user_data/',AdminUserView.as_view(),name='user_data'),
    path('user_update/<int:pk>', UpdateUser.as_view(), name='user_update'),
    path('user_delete/<int:pk>', DeleteUser.as_view(), name='user_delete'),
    path('single_user/<pk>', UserDetailView.as_view(),name='single_user'),

    path('user-registration/',BaseRegisterView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(template_name='userportal/login.html', success_url = '/admin_customized/'), name='login'),
    path('logout/', LogoutView.as_view(template_name='userportal/login.html'), name='logout'),

    path('registration/',RegisterAdminUserView.as_view(), name='registration'),
    path('login-1/', AdminLoginView.as_view(), name='login_1'),
    path('logout-1/', LogoutView.as_view(template_name='adminportal/login.html'), name='logout_1'),

]

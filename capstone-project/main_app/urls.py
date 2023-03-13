from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm

urlpatterns = [
    path('', views.home),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('category-name/<val>', views.CategoryName.as_view(), name='category-name'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),

    # login auth
    path('signup', views.CustomerRegistrationView.as_view(), name='signup'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='main_app/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='main_app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='main_app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='main_app/passwordchangedone.html'), name='passwordchangedone'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
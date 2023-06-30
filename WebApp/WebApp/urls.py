# Here I define the major paths (URLs) of the project 

"""
First, import all the views necessary. Remember, in a MVT architecture the views are
 the codes that handle request and responses.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from tracker import views as tracker_views
from blog import views as blog_views
from . import views as app_views

"""
Note that some views were created by me and others were imported from django framework.

Since the register, profile, login, logout and password reset views are relevent for the entire application,
I let it here, instead of letting it on the Users app.
"""

urlpatterns = [
      
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'
         ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'
         ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'
         ), name='password_reset_confirm'), 
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'
         ), name='password_reset_complete'),
    path('blog/', include('blog.urls')),
    path('tracker/', include('tracker.urls')),
    path('about', app_views.about, name='about'),
    path('', app_views.landing, name='realHome')
]
## The path /password_reset_confirm/<uidb64>/<token>/ didn't make much sense for me at beggining, 
## but it is in fact a convention that Django requires in its auth views.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
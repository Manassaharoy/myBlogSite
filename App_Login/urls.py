from django.urls import path
from . import views



app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.profile, name='profile'),
    path('changeProfile/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('addPicture/', views.add_pro_pic, name='add_pro_pic'),
    path('changePicture/', views.change_pro_pic, name='change_pro_pic'),
]


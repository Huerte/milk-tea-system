from django.urls import path
from . import views

urlpatterns = [
    # Main flow following the flowchart exactly
    path('', views.enter_system, name='enter_system'),
    path('menu/', views.browse_menu, name='browse_menu'),
    path('decide/', views.decide_order, name='decide_order'),
    path('choose-specifics/', views.choose_specifics, name='choose_specifics'),
    path('payment-method/', views.choose_payment_method, name='choose_payment_method'),
    path('counter/', views.proceed_to_counter, name='proceed_to_counter'),
    path('place-order/', views.place_order, name='place_order'),
    path('wait/<str:order_number>/', views.wait_for_drink, name='wait_for_drink'),
    path('receive/<str:order_number>/', views.receive_drink, name='receive_drink'),
    path('enjoy/<str:order_number>/', views.enjoy_drink, name='enjoy_drink'),
    path('exit/', views.exit_website, name='exit_website'),
    
    # Legacy redirect
    path('payment/', views.process_payment, name='process_payment'),
    
    # AJAX endpoints
    path('api/order-status/<str:order_number>/', views.get_order_status, name='get_order_status'),
    path('api/update-status/<str:order_number>/', views.update_order_status, name='update_order_status'),
]

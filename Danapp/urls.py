from . import views
from django.urls import path
urlpatterns =[
    path('',views.index,name='index'),
    path('portfolio_details/',views.portfolio_details,name='portfolio_details'),
    path('contact/',views.contact,name='contact'),
    path('portfolio_view',views.portfolio_view,name='portfolio_view')
]
from . import views
from django.urls import path
urlpatterns =[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('portfolio_details/',views.portfolio_details,name='portfolio_details')
]
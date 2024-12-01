from django.urls import path
from .views import landing_view, detailsView, checkout,add_item

app_name = 'landing'
urlpatterns = [
    path('', landing_view, name='index'),
    path('<int:id>', detailsView, name='detail'),
    path('checkout', checkout, name='checkout'),
    path('add-item', add_item, name='add_item'),
]
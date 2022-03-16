from django.urls import path

from rent.api.views import RentAPIView, RentAPIDetailView

app_name = 'rent'

urlpatterns = [
    # Paths Rent
    path('rent/', RentAPIView.as_view()),
    path('rent/<int:pk>/', RentAPIDetailView.as_view(), name='rent-list'),
]

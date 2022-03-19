from django.urls import path

from rent.api.views import RentAPIView, RentAPIDetailView

app_name = 'rent'

urlpatterns = [
    # Paths Rent
    path('rents/', RentAPIView.as_view()),
    path('rents/<int:pk>/', RentAPIDetailView.as_view(), name='rent-list'),
]

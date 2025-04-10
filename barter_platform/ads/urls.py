from django.urls import path
from .views import (
    AdListView, AdCreateView, AdUpdateView, AdDeleteView,
    ExchangeProposalCreateView,
)

urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
    path('ads/create/', AdCreateView.as_view(), name='ad_create'),
    path('ads/<int:pk>/edit/', AdUpdateView.as_view(), name='ad_edit'),
    path('ads/<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('proposals/create/', ExchangeProposalCreateView.as_view(), name='proposal_create'),
]
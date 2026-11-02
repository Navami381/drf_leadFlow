from django.urls import path
from lead.views import LeadListCreateView,LeadRetriveUpdateDeleteView

urlpatterns=[
    path("leads/",LeadListCreateView.as_view()),
    path("leads/<int:pk>/",LeadRetriveUpdateDeleteView.as_view())
]
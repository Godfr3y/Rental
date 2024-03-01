from django.urls import path
from carrental.views import TemplateView

urlpatterns = {
    path('', TemplateView.as_view(), name='list-view-post')
}
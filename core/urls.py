from django.urls import path
from .views import DocumentCreateView, DeleteView

urlpatterns = [
    path('', DocumentCreateView.as_view()),
    path('/delete/<int:pk>', DeleteView.as_view(), name='document_delete'),
]

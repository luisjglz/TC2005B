from django.urls import path
from . import views
from django.views.generic import TemplateView

# Also, add namespace in project urls.py
app_name = 'gviews'

# Note use of plural for list view and singular for detail view
urlpatterns = [
    path('', TemplateView.as_view(template_name='gviews/main.html')),
    path('cats', views.CatListView.as_view(), name='cats'),
    path('cat/<int:cat_id>', views.CatDetailView.as_view(), name='cat'),
]


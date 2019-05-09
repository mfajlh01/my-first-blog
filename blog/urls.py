from django.urls import path
from . import views # import all views from the blog app

urlpatterns = [
    path('', views.post_list, name='post_list'), # match an empty string and the Django resolver will ignore domain name
    # we assign view call post_list to the root of URL. views.post_list is the right place to go if someone enters the website
]

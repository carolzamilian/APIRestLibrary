from django.contrib import admin
#from django.urls import path, include

from rest_framework.routers import DefaultRouter

from books.views import  BooksViewSet

route = DefaultRouter()

route.register(r'books', BooksViewSet, basename="Books")
urlpatterns = route.urls

"""urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
"""
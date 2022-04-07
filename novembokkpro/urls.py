"""novembokkpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from owner import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("owner/books/add",views.AddBook.as_view(),name="addbook"),
    path("books/all",views.BookListView.as_view(),name="allbooks"),
    path("books/<int:id>",views.BookDetailView.as_view(),name="bookdetails"),
    path("books/remove/<int:id>",views.BookDelete.as_view(),name="bookdelete"),
    path("books/change/<int:id>",views.BookChange.as_view(),name="bookchange"),
    path("customers/",include("customer.urls")),
    path("owner/dashboard",views.DashBoardView.as_view(),name="dashboard"),
    path("owner/order/<int:id>",views.OrderDetailView.as_view(),name="orderdetail"),
    path("owner/order/change/<int:id>",views.OrderChangeView.as_view(),name="updateorder"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

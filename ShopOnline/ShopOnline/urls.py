"""ShopOnline URL Configuration

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
from django.urls import path, include
from ShopApp import views as ShopAppViews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShopAppViews.home),
    path('register/', ShopAppViews.register, name="register"),
    path('home/', ShopAppViews.home, name='home'),
    path('all/', ShopAppViews.all_items, name='all'),
    path('category/<int:category_id>/', ShopAppViews.category, name='category'),
    path('item/<int:item_id>/', ShopAppViews.item, name='item'),
    path('cart/', ShopAppViews.cart, name='cart'),
    path('order_done', ShopAppViews.order_done, name="order_done"),
    path('profile/', ShopAppViews.profile, name="profile"),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

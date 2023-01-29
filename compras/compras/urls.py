
from django.contrib import admin
from django.urls import path, include
from carrito import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('carrito.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products-list/', views.ProductsListView.as_view()),
    path('products-list/<int:pk>', views.ProductsListDetailView.as_view()),
    path('products-list/<int:pk>/update', views.ProductsListUpdateView.as_view()),
    path('products-list/<int:pk>/delete', views.ProductsListDeleteView.as_view()),
    path('products-list/nuevo/', views.ProductsListCreateView.as_view()),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
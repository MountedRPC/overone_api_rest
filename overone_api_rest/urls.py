from django.urls import include, path
from rest_framework import routers
from user_info.views import UserViewSet
from product_info.views import ProductsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

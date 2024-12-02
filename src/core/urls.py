from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
app_name = 'core'

# router.register('color', ColorModelViewSet, basename='color')
# router.register('postal_code', PostalCodeModelViewSet, basename='postal_code')
# router.register('address', AddressModelViewSet, basename='address')
# router.register('state', StateModelViewSet, basename='state')
# router.register('city', CityModelViewSet, basename='city')
# router.register('district', DistrictModelViewSet, basename='district')
# router.register('measurement_unit', MeasurementUnitModelViewSet, basename='measurement_unit')
# router.register('bank', BankModelViewSet, basename='bank')


urlpatterns = [
    path('', include(router.urls)),
]

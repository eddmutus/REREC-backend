from rest_framework.routers import DefaultRouter

from .views import CustomersViewSet, ExistingHtLineViewSet, HtLineConstructedViewSet, HtPolesViewSet, LvPolesViewSet, ParcelsViewSet, SinglePhaseViewSet

router = DefaultRouter()

router.register(prefix="api/v1/customers", viewset=CustomersViewSet, basename="customers")
router.register(prefix="api/v1/existing_ht_line", viewset=ExistingHtLineViewSet, basename="existing_ht_line")
router.register(prefix="api/v1/ht_line_constructed", viewset=HtLineConstructedViewSet, basename="ht_line_constructed")
router.register(prefix="api/v1/ht_poles", viewset=HtPolesViewSet, basename="ht_poles")
router.register(prefix="api/v1/lv_poles", viewset=LvPolesViewSet, basename="lv_poles")
router.register(prefix="api/v1/parcels", viewset=ParcelsViewSet, basename="parcels")
router.register(prefix="api/v1/single_phase", viewset=SinglePhaseViewSet, basename="single_phase")


urlpatterns = router.urls
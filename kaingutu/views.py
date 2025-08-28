from rest_framework import viewsets

from .models import Customers, ExistingHtLine, HtLineConstructed, HtPoles, LvPoles, Parcels, SinglePhase
from .serializers import CustomersSerializer, ExistingHtLineSerializer, HtLineConstructedSerializer, HtPolesSerializer, LvPolesSerializer, ParcelsSerializer, SinglePhaseSerializer


# Create your views here.
class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class ExistingHtLineViewSet(viewsets.ModelViewSet):
    queryset = ExistingHtLine.objects.all()
    serializer_class = ExistingHtLineSerializer

class HtLineConstructedViewSet(viewsets.ModelViewSet):
    queryset = HtLineConstructed.objects.all()
    serializer_class = HtLineConstructedSerializer

class HtPolesViewSet(viewsets.ModelViewSet):
    queryset = HtPoles.objects.all()
    serializer_class = HtPolesSerializer

class LvPolesViewSet(viewsets.ModelViewSet):
    queryset = LvPoles.objects.all()
    serializer_class = LvPolesSerializer

class ParcelsViewSet(viewsets.ModelViewSet):
    queryset = Parcels.objects.all()
    serializer_class = ParcelsSerializer

class SinglePhaseViewSet(viewsets.ModelViewSet):
    queryset = SinglePhase.objects.all()
    serializer_class = SinglePhaseSerializer

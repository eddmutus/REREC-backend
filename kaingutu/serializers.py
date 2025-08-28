from rest_framework import serializers

from .models import Customers, ExistingHtLine, HtLineConstructed, HtPoles, LvPoles, Parcels, SinglePhase


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        geo_field = "geom"
        fields = "__all__"

class ExistingHtLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingHtLine
        geo_field = "geom"
        fields = "__all__"

class HtLineConstructedSerializer(serializers.ModelSerializer):
    class Meta:
        model = HtLineConstructed
        geo_field = "geom"
        fields = "__all__"

class HtPolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HtPoles
        geo_field = "geom"
        fields = "__all__"

class LvPolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LvPoles
        geo_field = "geom"
        fields = "__all__"

class ParcelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        geo_field = "geom"
        fields = "__all__"

class SinglePhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinglePhase
        geo_field = "geom"
        fields = "__all__"
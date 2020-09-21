from django.contrib.gis.geos import LineString
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_gis import serializers as geo_serializers


class RoutingSerializer(serializers.Serializer):
    geom = geo_serializers.GeometryField()
    callback_id = serializers.CharField(required=False)

    def validate_geom(self, value):
        if not isinstance(value, LineString):
            raise ValidationError(_("Geometry value should be a LineString object."))
        return value

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import  TreesData, Userdata

class TreesDataSerializer(GeoFeatureModelSerializer):
    
	class Meta:
		model = TreesData
		fields = ['str_schl',  'baumgruppe','watering','fruit', 'eichenprozessionsspinner', 'date_water']
		geo_field = 'geom'


class UserDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = Userdata
		fields = '__all__'
		#fields =  ('name', 'email', 'feedback')
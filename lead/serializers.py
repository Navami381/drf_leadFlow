from rest_framework import serializers
from lead.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields="__all__"
        read_only_fields=["id","created_by","created_at","updated_at"]
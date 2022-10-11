from rest_framework import serializers
from .models import ClientDetail, CommunicationDetail, BillingDetail, ShippingDetail, BankingDetail, DocumentAndProof, OtherDetail


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDetail
        fields = '__all__'
        read_only_fields = ['updated_at', 'is_active']


class CommunicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationDetail
        fields = '__all__'
        read_only_fields = ['updated_at', 'is_active']


class BillingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingDetail
        fields = '__all__'
        read_only_fields = ['updated_at', 'is_active']


class ShippingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetail
        fields = '__all__'
        read_only_fields = ['updated_at', 'is_active']


class BankingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankingDetail
        fields = '__all__'
        read_only_fields = ['updated_at', 'is_active']


class DocumentAndProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAndProof
        fields = '__all__'
        read_only_fields = ['updated_at', 'is_active']


class OtherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDetail
        fields = '__all__'
        read_only_fields = ['updated_at', 'is_active']
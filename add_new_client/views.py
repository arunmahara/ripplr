from .models import ClientDetail, CommunicationDetail, BillingDetail, ShippingDetail, BankingDetail, DocumentAndProof, OtherDetail
from .serializers import ClientDetailSerializer, CommunicationDetailSerializer, BankingDetailSerializer, ShippingDetailSerializer, BillingDetailSerializer
from .serializers import DocumentAndProofSerializer, OtherDetailSerializer, LoginCredentialSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


# client detail model viewset
class ClientDetailView(viewsets.ModelViewSet):
    queryset = ClientDetail.objects.all()
    serializer_class = ClientDetailSerializer


# communication detail model viewset
class CommunicationDetailView(viewsets.ModelViewSet):
    queryset = CommunicationDetail.objects.all()
    serializer_class = CommunicationDetailSerializer


# billing detail model viewset
class BillingDetailView(viewsets.ModelViewSet):
    queryset = BillingDetail.objects.all()
    serializer_class = BillingDetailSerializer


#  shipping detail model viewset
class ShippingDetailView(viewsets.ModelViewSet):
    queryset = ShippingDetail.objects.all()
    serializer_class = ShippingDetailSerializer


# banking detail model viewset
class BankingDetailView(viewsets.ModelViewSet):
    queryset = BankingDetail.objects.all()
    serializer_class = BankingDetailSerializer


# document_proof model viewset
class DocumentAndProofView(viewsets.ModelViewSet):
    queryset = DocumentAndProof.objects.all()
    serializer_class = DocumentAndProofSerializer


# other detail model viewset
class OtherDetailView(viewsets.ModelViewSet):
    queryset = OtherDetail.objects.all()
    serializer_class = OtherDetailSerializer

# other detail model viewset
class LoginCredentialView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginCredentialSerializer
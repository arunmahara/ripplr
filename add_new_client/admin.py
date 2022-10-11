from django.contrib import admin
from .models import ClientDetail, CommunicationDetail, BillingDetail, ShippingDetail, BankingDetail, DocumentAndProof, OtherDetail


@admin.register(ClientDetail)
class ClientDetailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client_name',
        'client_short_name',
        'legal_structure',
        'contact_person_first_name', 
        'contact_person_middle_name',
        'contact_person_last_name', 
        'gender',
        'primary_cost_center'
    )


@admin.register(CommunicationDetail)
class CommunicationDetailAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'email',
        'mobile_no', 
        'alternate_no',
        'address', 
        'pin_code',
        'zone',
        'state',
        'city'
    )


@admin.register(BillingDetail)
class BillingDetailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',  
        'address', 
        'pin_code',
        'zone',
        'state',
        'city'
    )


@admin.register(ShippingDetail)
class ShippingDetailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',  
        'address', 
        'pin_code',
        'zone',
        'state',
        'city'
    )


@admin.register(BankingDetail)
class BankingDetailAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'account_code', 
        'account_no',
        'ifsc_code',
        'bank_name',
        'bank_city',
        'bank_branch',
        'bank_document'
    )


@admin.register(DocumentAndProof)
class DocumentAndProofAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'pan_number',
        'adhar_number',
        'gst_reg_type',
        'gst_number',
        'pan_document',
        'adhar_document',
        'gst_document',
    )


@admin.register(OtherDetail)
class OtherDetailAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'related_party',
        'black_listed',
        'same_as_billing_location',
        'document_currency',
        'credit_period',
        'credit_amount',
        'payment_terms_and_condition',
        'exempt_from_tax',
    )
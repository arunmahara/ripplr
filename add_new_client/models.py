from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# choices for legal structure
LEGAL_STRUCTURE_CHOICE=[
    ('Company', 'Company'),
    ('LLP', 'LLP'),
    ('Individual', 'Individual'),
]


#choices for gender
GENDER_CHOICE=[
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]


#choices for primary cost center 
PRIMARY_COST_CENTER_CHOICE=[
    ('Distribution', 'Distribution'),
    ('Logistics', 'Logistics'),
]


#choices for zone
ZONE_CHOICES=[
    ('Central Zone', 'Central Zone'),
    ('East Zone', 'East Zone'),
    ('East Zone1', 'East Zone1'),
    ('North East Zone', 'North East Zone'),
    ('North Zone', 'North Zone'),
    ('South Zone','South Zone'),
    ('Union Territory', 'Union Territory'),
    ('West Zone', 'West Zone'),
]


#choices for state
STATE_CHOICES=[
    ('Bihar', 'Bihar'),
    ('Jharkhand', 'Jharkhand'),
    ('Odisha', 'Odisha'),
    ('Test State', 'Test State'),
    ('West Bengal', 'West Bengal'),
]


#choices for city
CITY_CHOICES=[
    ('none', 'none'),
]


#choices for GST Reg type
GST_REG_TYPE_CHOICES=[
    ('Registered', 'Registered'),
    ('Unregistered', 'Unregistered'),
]


# abstract model timestamp
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


#model for client details
class ClientDetail(TimeStamp):
    client_name = models.CharField(max_length=255)
    client_short_name = models.CharField(max_length=50)
    legal_structure = models.CharField(max_length=15, choices=LEGAL_STRUCTURE_CHOICE)
    contact_person_first_name = models.CharField(max_length=255)
    contact_person_middle_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person_last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    primary_cost_center = models.CharField(max_length=15, choices=PRIMARY_COST_CENTER_CHOICE)

    def __str__(self):
        return self.client_name


# abstract model address
class AddressDetail(TimeStamp):
    address = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=6, validators = [RegexValidator('^[0-9]{6}$', _('Invalid pin code'))])
    zone = models.CharField(max_length=50, choices=ZONE_CHOICES)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)

    class Meta:
        abstract = True


#model for billing details
class CommunicationDetail(AddressDetail):
    client  = models.OneToOneField(ClientDetail, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    mobile_no = PhoneNumberField(unique=True)
    alternate_no = PhoneNumberField()

    def __str__(self):
        return self.client.client_name


#model for billing details
class BillingDetail(AddressDetail):
    client  = models.ForeignKey(ClientDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.client_name


#model for shipping details
class ShippingDetail(AddressDetail):
    client  = models.ForeignKey(ClientDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.client_name


#model for banking details
class BankingDetail(TimeStamp):
    client  = models.OneToOneField(ClientDetail, on_delete=models.CASCADE, primary_key=True)
    account_code = models.CharField(max_length=20)
    account_no = models.CharField(max_length=17)
    ifsc_code = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=200)
    bank_city = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    bank_document = models.FileField(upload_to='bankDocument/')

    def __str__(self):
        return self.client.client_name


#model for document and proof 
class DocumentAndProof(TimeStamp):
    client  = models.OneToOneField(ClientDetail, on_delete=models.CASCADE, primary_key=True)
    pan_number = models.CharField(max_length=10)
    adhar_number = models.CharField(max_length=12)
    gst_reg_type = models.CharField(max_length=15, choices=GST_REG_TYPE_CHOICES)
    gst_number = models.CharField(max_length=15)
    pan_document = models.FileField(upload_to='panDocument/')
    adhar_document = models.FileField(upload_to='adharDocument/')
    gst_document = models.FileField(upload_to='gstDocument/')

    def __str__(self):
        return self.client.client_name


#model for other details
class OtherDetail(TimeStamp):
    client  = models.OneToOneField(ClientDetail, on_delete=models.CASCADE, primary_key=True)
    related_party = models.BooleanField(blank=True, null=True)
    black_listed = models.BooleanField(blank=True, null=True)
    same_as_billing_location = models.BooleanField(blank=True, null=True)
    document_currency = models.CharField(max_length=255)
    credit_period = models.CharField(max_length=255)
    credit_amount = models.FloatField()
    payment_terms_and_condition = models.TextField()
    exempt_from_tax = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.client.client_name

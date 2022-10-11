from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


# # Creating Router Object
router = DefaultRouter()


# # Register ViewSets with Router
router.register('client_detail', views.ClientDetailView, basename='client_detail')
router.register('communication_detail', views.CommunicationDetailView, basename='communication_detail')
router.register('billing_detail', views.BillingDetailView, basename='billing_detail')
router.register('shipping_detail', views.ShippingDetailView, basename='shipping_detail')
router.register('banking_detail', views.BankingDetailView, basename='banking_detail')
router.register('document_proof', views.DocumentAndProofView, basename='document_proof')
router.register('other_detail', views.OtherDetailView, basename='other_detail')


urlpatterns = [
    path('', include(router.urls)),

    # for login logout url
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    #for session authentication
    path('gettoken/', obtain_auth_token),

    #for jwt authentication
    path('getjwtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
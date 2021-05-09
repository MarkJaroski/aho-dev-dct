from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import (generics,permissions,renderers,)

from commoninfo.permissions import IsOwnerOrReadOnly,CustomDjangoModelPermissions
from .models import (StgFacilityType,StgFacilityOwnership,StgHealthFacility,
    StgServiceDomain,StgLocationCodes,FacilityServiceAvailability,
    FacilityServiceProvision,FacilityServiceReadiness,)

from .serializers import (StgFacilityTypeSerializer,StgFacilityOwnershipSerializer,
    StgServiceDomainSerializer,StgHealthFacilitySerializer,
    FacilityServiceAvailabilitySerializer,FacilityServiceProvisionSerializer,
    FacilityServiceReadinessSerializer,)

class StgFacilityTypeViewSet(viewsets.ModelViewSet):
    serializer_class = StgFacilityTypeSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,)

    def get_queryset(self):
        language = self.request.LANGUAGE_CODE # get the en, fr or pt from the request
        return StgFacilityType.objects.filter(
            translations__language_code=language).order_by(
            'translations__name').distinct()


class StgFacilityOwnershipViewSet(viewsets.ModelViewSet):
    serializer_class = StgFacilityOwnershipSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,)

    def get_queryset(self):
        language = self.request.LANGUAGE_CODE # get the en, fr or pt from the request
        return StgFacilityOwnership.objects.filter(
            translations__language_code=language).order_by(
            'translations__name').distinct()


class StgServiceDomainViewSet(viewsets.ModelViewSet):
    serializer_class = StgServiceDomainSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,IsOwnerOrReadOnly)

    def get_queryset(self):
        language = self.request.LANGUAGE_CODE # get the en, fr or pt from the request
        return StgServiceDomain.objects.filter(
            translations__language_code=language).order_by(
            'translations__name').distinct()


class StgHealthFacilityViewSet(viewsets.ModelViewSet):
    serializer_class = StgHealthFacilitySerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,IsOwnerOrReadOnly)

    def get_queryset(self):
        return StgHealthFacility.objects.all().order_by(
            'name').distinct()


class  FacilityServiceAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = FacilityServiceAvailabilitySerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,IsOwnerOrReadOnly)

    def get_queryset(self):
        return FacilityServiceAvailability.objects.all().order_by(
            'facility').distinct()



class  FacilityServiceCapacityViewSet(viewsets.ModelViewSet):
    serializer_class = FacilityServiceProvisionSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,IsOwnerOrReadOnly)

    def get_queryset(self):
        return FacilityServiceProvision.objects.all().order_by(
            'facility').distinct()



class  FacilityServiceReadinessViewSet(viewsets.ModelViewSet):
    serializer_class = FacilityServiceReadinessSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,IsOwnerOrReadOnly)

    def get_queryset(self):
        return FacilityServiceReadiness.objects.all().order_by(
            'facility').distinct()

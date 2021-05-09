from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import (generics,permissions,
    renderers,)

from commoninfo.permissions import IsOwnerOrReadOnly,CustomDjangoModelPermissions
from indicators.models import (StgIndicatorReference, StgIndicator,
    StgIndicatorDomain, FactDataIndicator,aho_factsindicator_archive,)
from indicators.serializers import (StgIndicatorReferenceSerializer,
    StgIndicatorSerializer,StgIndicatorDomainSerializer,
    FactDataIndicatorSerializer,FactIndicatorArchiveSerializer)

class StgIndicatorReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = StgIndicatorReferenceSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,)

    def get_queryset(self):
        language = self.request.LANGUAGE_CODE # get the en, fr or pt from the request
        return StgIndicatorReference.objects.filter(
            translations__language_code=language).order_by(
            'translations__name').distinct()



class StgIndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = StgIndicatorSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,)

    def get_queryset(self):
        language = self.request.LANGUAGE_CODE # get the en, fr or pt from the request
        return StgIndicator.objects.filter(
            translations__language_code=language).order_by(
            'translations__name').distinct()


class StgIndicatorDomainViewSet(viewsets.ModelViewSet):
    queryset = StgIndicatorDomain.objects.all()
    serializer_class = StgIndicatorDomainSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,)

    def get_queryset(self):
        language = self.request.LANGUAGE_CODE # get the en, fr or pt from the request
        return StgIndicatorDomain.objects.filter(
            translations__language_code=language).order_by(
            'translations__name').distinct()


class FactDataIndicatorViewSet(viewsets.ModelViewSet):
    queryset = FactDataIndicator.objects.all()
    serializer_class = FactDataIndicatorSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,IsOwnerOrReadOnly)

    # def get_queryset(self):
    #     location = self.request.location # get the en, fr or pt from the request
    #     return FactDataIndicator.objects.filter(
    #         location=location).order_by(
    #         'translations__name').distinct()


class FactIndicatorArchiveViewSet(viewsets.ModelViewSet):
    queryset = aho_factsindicator_archive.objects.all()
    serializer_class = FactIndicatorArchiveSerializer
    permission_classes = (permissions.IsAuthenticated,
        CustomDjangoModelPermissions,IsOwnerOrReadOnly)

    # def get_queryset(self):
    #     location = self.request.location # get the en, fr or pt from the request
    #     return aho_factsindicator_archive.objects.filter(
    #         location=location).order_by(
    #         'translations__name').distinct()

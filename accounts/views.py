from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from core.views import CompanySafeViewMixin
from accounts import serializers


User = get_user_model()


class AccountCreate(generics.CreateAPIView):
    name = 'account-create'
    serializer_class = serializers.AccountSerializer


class UserList(CompanySafeViewMixin, generics.ListCreateAPIView):
    name = 'user-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    # the abstract CompanySafeViewMixin replaces below methods
    '''def perform_create(self, serializer):
        company_id = self.request.user.company_id
        serializer.save(company_id=company_id)

    def get_queryset(self):
        # Ensure that the users belong to the company of the user that is making the request
        company_id = self.request.user.company_id
        return super().get_queryset().filter(company_id=company_id)'''


class UserDetail(CompanySafeViewMixin, generics.RetrieveUpdateDestroyAPIView):
    name = 'user-detail'
    permission_classes = (
       permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    '''def get_queryset(self):
        # Ensure that the user belongs to the company of the user that is making the request
        # Note that this method is identical to the one in `UserList`
        company_id = self.request.user.company_id
        return super().get_queryset().filter(company_id=company_id)'''


class CompanyDetail(generics.RetrieveUpdateAPIView):
    name = 'company-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.CompanySerializer

    def get_object(self):
        # Ensure that users can only see the company that they belong to
        return self.request.user.company
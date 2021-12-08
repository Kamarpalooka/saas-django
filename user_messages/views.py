from rest_framework import permissions
from rest_framework import generics

from user_messages import serializers
from user_messages.models import UserMessage


class UserMessageList(generics.ListCreateAPIView):
    name = 'usermessage-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        company_id = self.request.user.company_id
        serializer.save(company_id=company_id, from_user=user)

    def get_queryset(self):
        '''
            company_id = self.request.user.company_id
            return super().get_queryset().filter(company_id=company_id)
        '''

        # uses the UserMessageManager's method 'get_for_user'
        return UserMessage.objects.get_for_user(self.request.user)


class UserMessageDetail(generics.RetrieveAPIView):
    name = 'usermessage-detail'
    permission_classes = (
       permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def get_queryset(self):
        """
            company_id = self.request.user.company_id
            return super().get_queryset().filter(company_id=company_id)
        """

        # uses the UserMessageManager's method 'get_for_user'
        return UserMessage.objects.get_for_user(self.request.user)
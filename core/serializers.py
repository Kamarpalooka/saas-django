from rest_framework import serializers


class CompanySafeRelatedField(serializers.HyperlinkedRelatedField):
    """
    Ensures that the queryset only returns values related to the company of the user belongs /
    """
    def get_queryset(self):
        request = self.context['request']
        company_id = request.user.company_id
        return super().get_queryset().filter(company_id=company_id)


class CompanySafeSerializerMixin(object):
    """
    Mixin to be used with HyperlinkedModelSerializer to ensure that only company values are returned
    """
    serializer_related_field = CompanySafeRelatedField
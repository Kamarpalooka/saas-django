from django.core import exceptions


class CompanySafeViewMixin:
    """
    Mixin to be used with views that ensures that models are related to the company during creation and are querysets
    are filtered for read operations
    """
    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated()

        company_id = self.request.user.company_id
        return queryset.filter(company_id=company_id)

    def perform_create(self, serializer):
        company_id = self.request.user.company_id
        serializer.save(company_id=company_id)
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from auditlog.models import LogEntry


class UserAuditLog(LoginRequiredMixin, ListView):
    def get_queryset(self, *args, **kwargs):
        return LogEntry.objects.filter(actor=self.request.user)


class AuditLog(UserPassesTestMixin, ListView):
    model = LogEntry

    def test_func(self):
        return self.request.user.is_superuser

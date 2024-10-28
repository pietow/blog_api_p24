
from django.shortcuts import redirect
from allauth.account.views import ConfirmEmailView

class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.confirm(self.request)
        return redirect('rest_user_details')

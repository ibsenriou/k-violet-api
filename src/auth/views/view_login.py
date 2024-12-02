from dj_rest_auth.views import LoginView as BaseLoginView


class LoginView(BaseLoginView):
    def login(self):
        super().login()
        resolved_permissions, user_filters = "", ""
        self.request.session['resolved_permissions'] = list(resolved_permissions)
        self.request.session['user_filters'] = user_filters
        self.request.session.modified = True
        self.request.session.save()

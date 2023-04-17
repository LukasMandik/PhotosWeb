from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import generate_unique_username
import uuid


class CustomAccountAdapter(DefaultAccountAdapter):
    username_max_length = 40

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.email = data['email']
        user.username = data['email']  # Uložte email ako username
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        if commit:
            user.save()
        return user

    def populate_username(self, request, user):
        if not user.username:
            first_name = user.first_name or ''
            last_name = user.last_name or ''
            base_username = f"{first_name}.{last_name}".lower()
            user.username = self.generate_unique_username(base_username)

    def generate_unique_username(self, base_username):
        unique_string = uuid.uuid4().hex[:6]  # Generate a random unique string with 6 characters
        username = f"{base_username}.{unique_string}"
        return generate_unique_username([username], self.username_max_length)

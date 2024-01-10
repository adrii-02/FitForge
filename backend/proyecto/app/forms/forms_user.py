from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # Aquí puedes añadir los campos adicionales que necesitas
        fields = UserCreationForm.Meta.fields + ('email', 'password1', 'password2', 'username', 'first_name', 'last_name', 'age', 'gender', 'length', 'weight')


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm.Meta):
        pass

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
#유저 정보 변환 폼!
from django.contrib.auth import get_user_model


class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

class UserCustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


from django import forms
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8  # Optional: set a minimum length for the password
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'surname', 'nida_number', 'email', 'phone_number_1', 'phone_number_2', 'passport_image', 'gender', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'nida_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number 1'}),
            'phone_number_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number 2 (optional)'}),
            'passport_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_nida_number(self):
        nida_number = self.cleaned_data.get('nida_number')
        if nida_number and (len(nida_number) != 20 or not nida_number.isdigit()):
            raise forms.ValidationError('NIDA number must be exactly 20 digits.')
        return nida_number

    def clean_phone_number_1(self):
        phone_number = self.cleaned_data.get('phone_number_1')
        if phone_number:
            if len(phone_number) != 10 or not phone_number.startswith('0') or not phone_number.isdigit():
                raise forms.ValidationError('Phone Number 1 must start with 0 and be exactly 10 digits long.')
        return phone_number

    def clean_phone_number_2(self):
        phone_number = self.cleaned_data.get('phone_number_2')
        if phone_number:
            if len(phone_number) != 10 or not phone_number.startswith('0') or not phone_number.isdigit():
                raise forms.ValidationError('Phone Number 2, if provided, must start with 0 and be exactly 10 digits long.')
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match')

        return cleaned_data

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'surname', 'nida_number', 'email', 'phone_number_1', 'phone_number_2', 'passport_image', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'nida_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIDA Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number 1'}),
            'phone_number_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number 2 (optional)'}),
            'passport_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_phone_number_1(self):
        phone_number = self.cleaned_data.get('phone_number_1')
        if phone_number:
            if len(phone_number) != 10 or not phone_number.startswith('0') or not phone_number.isdigit():
                raise forms.ValidationError('Phone Number 1 must start with 0 and be exactly 10 digits long.')
        return phone_number

    def clean_phone_number_2(self):
        phone_number = self.cleaned_data.get('phone_number_2')
        if phone_number:
            if len(phone_number) != 10 or not phone_number.startswith('0') or not phone_number.isdigit():
                raise forms.ValidationError('Phone Number 2, if provided, must start with 0 and be exactly 10 digits long.')
        return phone_number



from django import forms
from django.contrib.auth import authenticate

class CustomLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password.")
        return cleaned_data




from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'surname', 'email', 'phone_number_1', 'phone_number_2', 'gender', 'user_type']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number_1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number_2': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }

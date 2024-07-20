from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Inmueble

class CrearUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    nombres = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rut = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono_personal = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Usuario.objects.create(
                user=user,
                nombres=self.cleaned_data['nombres'],
                apellidos=self.cleaned_data['apellidos'],
                rut=self.cleaned_data['rut'],
                direccion=self.cleaned_data['direccion'],
                telefono_personal=self.cleaned_data['telefono_personal'],
                correo_electronico=self.cleaned_data['correo_electronico'],
                tipo_usuario=self.cleaned_data['tipo_usuario']
            )
        return user


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'direccion', 'telefono_personal', 'correo_electronico']


class ActualizarUsuarioForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono_personal', 'email']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_personal': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        if commit:
            usuario.save()
            usuario.user.email = self.cleaned_data['email']
            usuario.user.save()
        return usuario

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'cantidad_estacionamientos',
                'cantidad_habitaciones', 'cantidad_banos', 'direccion', 'tipo_inmueble', 'precio_mensual', 
                'region', 'comuna', 'imagen_url']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
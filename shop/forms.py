from django import forms
#from django.conf import settings
from .models import User,Country,State,City,Address,Order
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
GENDER_CHOICE = (('M','Male'),('F','Female'))


    
	
class UserPasswordFixForm(UserCreationForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    address1 = forms.CharField(label=_('Address1'), max_length=80,validators = [RegexValidator(regex='^[a-zA-Z0-9_.:;,/\\-\s]+$',message = 'enter charecters,number,dash,hyphen,apostrophe',code='invalid_address')])

    """
    This field represents an address1 field.
    """

    address2 = forms.CharField(label=_('Address2'), max_length=80,required=False,validators = [RegexValidator(regex='^[a-zA-Z0-9_.:;,/\\-\s]+$',message = 'enter charecters,number,dash,hyphen,apostrophe',code='invalid_address')])

    """
    This field represents an address2 field.
    """

    country = forms.ModelChoiceField(label=_('Country'),queryset=Country.objects.all())

    """
    This field represents a country field.
    """

    state = forms.ModelChoiceField(label=_('State'),queryset=State.objects.all())

    """
    This field represents a state field.
    """

    city = forms.ModelChoiceField(label=_('City'), queryset=City.objects.all())

    """
    This field represents a location field.
    """

    class Meta:
        model = User
        exclude = ('password',)
    # def __init__(self,*args,**kwrgs):
        # super(UserPasswordFixForm,self).__init__(*args,**kwrgs)
        # if self.instance.pk:
            # add1=self.instance.address_set.get()
            # print(add1.address_line1)
            # tempadd1=add1.address_line1
            # self.fields['address1'].initial = tempadd1
            # print(add1.address_line2)
            # tempadd2=add1.address_line2
            # self.fields['address2'].initial = tempadd2
            # #self.fields['address2'].initial = self.instance.address_set.all().address_line2
            # print(add1.city.name)
            # print(add1.city.state.name)
            # print(add1.city.state.country.name)
            # self.fields['country'].initial = add1.city.state.country.name
            # self.fields['state'].initial = add1.city.state.name
            # self.fields['city'].initial = add1.city.name
    # def clean_password2(self):
        # cd = self.cleaned_data
        # if cd['password'] != cd['password2']:
            # raise forms.ValidationError('Passwords don\'t match.')
        # return cd['password2']


class CustomUserRegistrationForm(forms.Form):
    email = forms.EmailField(label=_('email address'),required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    first_name = forms.CharField(label=_('first name'), max_length=30,validators = [RegexValidator(regex='^[a-zA-z\s]+$',message = 'First name must have alphabets only',code= 'invalid_name'),])
    last_name = forms.CharField(label=_('last name'), max_length=30, validators = [RegexValidator(regex='^[a-zA-Z\'\s]*$',message = 'Last name must have charecters only',code= 'invalid_name'),])
    phone_number = forms.CharField(max_length=10,validators = [RegexValidator(regex='^[789]\d{9}$',message = 'Enter a valid Indian Phone Number',code= 'invalid_name'),])
    gender = forms.ChoiceField(choices = GENDER_CHOICE,widget=forms.Select(attrs={'class':'regDropDown'}))
    #need to add clean validation to date of birth i.e birthdate shouldnt be greater than today
    date_of_birth = forms.DateField(required = False)
    address1 = forms.CharField(label=_('Address1'), max_length=80,validators = [RegexValidator(regex='^[a-zA-Z0-9_.:;,/\\-\s]+$',message = 'enter charecters,number,dash,hyphen,apostrophe',code='invalid_address')])

    """
    This field represents an address1 field.
    """

    address2 = forms.CharField(label=_('Address2'), max_length=80,required=False,validators = [RegexValidator(regex='^[a-zA-Z0-9_.:;,/\\-\s]+$',message = 'enter charecters,number,dash,hyphen,apostrophe',code='invalid_address')])

    """
    This field represents an address2 field.
    """

    country = forms.ModelChoiceField(label=_('Country'),queryset=Country.objects.all())

    """
    This field represents a country field.
    """

    state = forms.ModelChoiceField(label=_('State'),queryset=State.objects.all())

    """
    This field represents a state field.
    """

    city = forms.ModelChoiceField(label=_('City'), queryset=City.objects.all())

    """
    This field represents a location field.
    """
    def clean_password2(self): 
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
	
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user','shipping_address']
		

class CouponApplyForm(forms.Form):
    code = forms.CharField()
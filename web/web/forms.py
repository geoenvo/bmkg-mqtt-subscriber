from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from .models import GeneralSetting


class MinLengthValidator(validators.MinLengthValidator):
    message = 'Ensure this value has at least %(limit_value)d elements (it has %(show_value)d).'

class MaxLengthValidator(validators.MaxLengthValidator):
    message = 'Ensure this value has at most %(limit_value)d elements (it has %(show_value)d).'


class CommaSeparatedCharField(forms.Field):
    def __init__(self, dedup=True, max_length=None, min_length=None, *args, **kwargs):
        self.dedup, self.max_length, self.min_length = dedup, max_length, min_length
        super(CommaSeparatedCharField, self).__init__(*args, **kwargs)
        if min_length is not None:
            self.validators.append(MinLengthValidator(min_length))
        if max_length is not None:
            self.validators.append(MaxLengthValidator(max_length))

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return ''
            #return []
        # prevent appending saved value continuously
        value = value.replace("[", "")
        value = value.replace("]", "")
        value = value.replace("'", "")
        value = value.replace("u", "")
        value = [item.strip() for item in value.split(',') if item.strip()]
        if self.dedup:
            value = list(set(value))

        return value

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value


class CommaSeparatedIntegerField(forms.Field):
    default_error_messages = {
        'invalid': 'Enter comma separated numbers only.',
    }

    def __init__(self, dedup=True, max_length=None, min_length=None, *args, **kwargs):
        self.dedup, self.max_length, self.min_length = dedup, max_length, min_length
        super(CommaSeparatedIntegerField, self).__init__(*args, **kwargs)
        if min_length is not None:
            self.validators.append(MinLengthValidator(min_length))
        if max_length is not None:
            self.validators.append(MaxLengthValidator(max_length))

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return []

        try:
            value = [int(item.strip()) for item in value.split(',') if item.strip()]
            if self.dedup:
                value = list(set(value))
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages['invalid'])

        return value

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value


class GeneralSettingAdminForm(forms.ModelForm):
    show_bps_id_kab_multiple = CommaSeparatedCharField(
        max_length=255,
        required=False,
        label="Filter Multiple Kabupaten IDs (separate IDs with comma)"
    )
    show_bps_id_kec_multiple = CommaSeparatedCharField(
        max_length=255,
        required=False,
        label="Filter Multiple Kecamatan IDs (separate IDs with comma)"
    )
    show_bps_id_des_multiple = CommaSeparatedCharField(
        max_length=255,
        required=False,
        label="Filter Multiple Desa IDs (separate IDs with comma)"
    )
    show_area_id_multiple = CommaSeparatedCharField(
        max_length=255,
        required=False,
        label="Filter Multiple Area ID (separate Area IDs with comma)"
    )
    
    class Meta:
        model = GeneralSetting
        fields = '__all__'

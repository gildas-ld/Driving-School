from django import forms

from .models import Lesson

# creating a form
# "Field",
# "CharField",
# "IntegerField",
# "DateField",
# "TimeField",
# "DateTimeField",
# "DurationField",
# "RegexField",
# "EmailField",
# "FileField",
# "ImageField",
# "URLField",
# "BooleanField",
# "NullBooleanField",
# "ChoiceField",
# "MultipleChoiceField",
# "ComboField",
# "MultiValueField",
# "FloatField",
# "DecimalField",
# "SplitDateTimeField",
# "GenericIPAddressField",
# "FilePathField",
# "JSONField",
# "SlugField",
# "TypedChoiceField",
# "TypedMultipleChoiceField",
# "UUIDField",
# class LessonsForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(
#                      help_text = "Enter 6 digit roll number"
#                      )
#     password = forms.CharField(widget = forms.PasswordInput())


#     multiple = forms.TypedMultipleChoiceField()
class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"

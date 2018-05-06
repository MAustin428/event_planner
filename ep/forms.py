from django import forms
from ep.models import Event

class DateInput(forms.DateInput):
	input_type = 'date'

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = '__all__'
		widgets = {
			'event_date': DateInput(),
			'entry_date': DateInput(),
			'pickup_date': DateInput(),
			'': forms.Textarea(attrs={'rows':10,'cols':80}),
		}
				  
from django.forms import ModelForm
from ep.models import Event

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['in_history', 'cust_name', 'cust_phone', 'event_date', 'pickup_date',
				  'assoc_name', 'entry_date', 'total_amt', 'total_cost', 'return_amt']
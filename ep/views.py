from .models import Event_Item, Event
from .forms import EventForm

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from datetime import datetime


#For testing purposes only
jz = ['Jerry Zhang', '880-090-5585', '2018-08-07', '2018-08-06', 'Mark D',
	  '2018-04-17', [ ['Kitchen Sink Moscato', 750, 8.99, 3], ['Cheval Quancard', 750, 12.99, 6], 
	  ['Jameson', 1750, 29.99, 1] ], 85, 420, 0]

pdl2 = [ ['Kitchen Sink Moscato', 750, 8.99, 3], ['Cheval Quancard', 750, 12.99, 6], ['Jameson', 1750, 29.99, 1] ]


# Create your views here.
e_list = list(Event.objects.all())

def summary(request):
	all_events = Event.objects.all()
	context = {'all_events': all_events,}
	return render(request, 'ep/summary.html', context)

def new(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.entry_date = datetime.today()
			post.save()
			return redirect('ep:summary')
	else:
		form = EventForm()
	return render(request, 'ep/InformationReader.html', {'form': form})


# Creates new entry when user presses the save button on the Create Event page
def create_entry(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('')



#	v = []
	
#	t = Event.objects.create()

#	for x in pdl2:
#		b = t.event_item_set.create(product_name = x[0], product_size = x[1], product_cost = x[2], product_qty = x[3])

#	i = 0
#	if e_list:
#		while datetime.strptime(t.event_date, '%Y-%m-%d').date() < e_list[i].event_date:
#			i += 1

#	e_list.insert(i, t)

# Updates existing entry when user presses the save button on the Edit Event page
def update_entry(e_list_entry, ___vals___):
	e_list_entry.data = ___vals___
	e_list_entry.save()

# Returns event information when user presses the View Event button
def view_entry(entry_index):
	the_event = e_list[entry_index]
	print(repr(the_event.cust_name))
	print(repr(the_event.cust_phone))
	print(repr(the_event.event_date))
	print(repr(the_event.pickup_date))
	print(repr(the_event.assoc_name))
	print(repr(the_event.entry_date))

	for i in the_event.product_list.all():
		print(repr(i.product_name), " ", repr(i.product_size), " ", repr(str(i.product_cost)), " ", repr(i.product_qty))
	# print(repr(the_event.product_list))

	print(repr(the_event.total_amt))
	print(repr(the_event.total_cost))
	print(repr(the_event.return_amt))

# Returns summary information for the Event List page
def event_list_summary(pull_from_history):
	if pull_from_history:
		tl = Event.objects.filter(in_history = True)
	else:
		tl = Event.objects.filter(in_history = False)

	for i in tl:
		print(repr(i.cust_name) + '\t' + repr(i.event_date.strftime('%m-%d-%Y')) + '\t' + repr(i.assoc_name))


def delete_entry(e_list_entry):
	e_list_entry.delete()
	if e_list:
		e_list.remove(e_list_entry)

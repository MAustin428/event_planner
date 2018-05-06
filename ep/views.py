from .models import Event_Item, Event
from .forms import EventForm

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from datetime import datetime

# Create your views here.
e_list = list(Event.objects.all())

def history(request, title): 

	if(title == 'List of Events'):
		all_events = Event.objects.all()
		context = {'all_events': all_events, 'title': 'History', 'history': 'Events'}
		return render(request, 'ep/summary.html', context)
	else:
		return summary(request)

def send_history(request):
	return summary(request)

def summary(request):
	all_events = Event.objects.all()
	context = {'all_events': all_events, 'title': 'List of Events', 'history': 'History'}
	return render(request, 'ep/summary.html', context)

def new(request):
	if request.method == 'POST':
		if 'cancel' in request.POST:
			return redirect('ep:summary')
		else:
			form = EventForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.entry_date = datetime.today()
				post.save()
				return redirect('ep:summary')
	else:
		form = EventForm()
	return render(request, 'ep/InformationReader.html', {'form': form, 'button_value': 'Enter'})

# Updates existing entry when user presses the save button on the Edit Event page
def update(request, pk):
	event = get_object_or_404(Event, pk=pk)
	if request.method == "POST":
		print(request.method)
		if 'cancel' in request.POST:
			return redirect('ep:summary')
		elif 'delete' in request.POST:
			event.delete()
			return redirect('ep:summary')
		else:
			form = EventForm(request.POST, instance=event)
			if form.is_valid():
				form.save()
				return redirect('ep:summary')
	else:
		form = EventForm(instance=event)
	return render(request, 'ep/InformationReader.html', {'form': form, 'button_value': 'Update'})


def view_event(request, pk):
	event = get_object_or_404(Event, pk=pk)
	return redirect('ep/view_event.html', pk=event.pk)

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

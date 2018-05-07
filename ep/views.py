from .models import Event_Item, Event
from .forms import EventForm

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from datetime import datetime

# Create your views here.
def history(request, title):
	if(title == 'List of Events'):
		all_events = Event.objects.filter(in_history=True)
		context = {'all_events': all_events, 'title': 'History', 'history': 'Events', 'send': 'Return to live'}
		return render(request, 'ep/summary.html', context)
	else:
		return summary(request)

def send_history(request, pk):
	event = get_object_or_404(Event, pk=pk)
	if(event.in_history):
		event.in_history=False
		event.save()
		return redirect('ep:summary')
	else:
		event.in_history=True
		event.save()
		return redirect('ep:summary')

def summary(request):
	all_events = Event.objects.filter(in_history=False)
	context = {'all_events': all_events, 'title': 'List of Events', 'history': 'History', 'send': 'Send to History'}
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
				return redirect('ep:summary')
	else:
		form = EventForm(instance=event)
	return render(request, 'ep/InformationViewer.html', {'form': form, 'button_value': '', 'return_func':'ep:view_event', 'param':event.pk})

from .models import Event_Item, Event
from .forms import EventForm

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from datetime import datetime

# Create your views here.
def history(request, title):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		if(title == 'List of Events'):
			all_events = Event.objects.filter(in_history=True).order_by('-event_date')
			context = {'all_events': all_events, 'title': 'History', 'history': 'Events', 'send': 'Return to live'}
			return render(request, 'ep/summary.html', context)
		else:
			return summary(request)

def send_history(request, pk):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		event = get_object_or_404(Event, pk=pk)
		event.in_history = not event.in_history
		event.save()
		return redirect('ep:summary')

def summary(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		all_events = Event.objects.filter(in_history=False).order_by('pickup_date')
		context = {'all_events': all_events, 'title': 'List of Events', 'history': 'History', 'send': 'Send to History'}
		return render(request, 'ep/summary.html', context)

def new(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		if request.method == 'POST':
			if 'cancel' in request.POST:
				print('Cancel')
				return redirect('ep:summary')
			else:
				form = EventForm(request.POST)
				if form.is_valid():
					post = form.save(commit=False)
					post.in_history = False
					post.entry_date = datetime.today()
					post.save()
					context = {'all_events': all_events, 'title': 'List of Events', 'history': 'History', 'send': 'Send to History'}
					return render(request, 'ep/summary.html', context)
		else:
			form = EventForm()
		return render(request, 'ep/InformationReader.html', {'form': form, 'button_value': 'Enter'})

	def items(request):
		item_form=EventForm(request.POST)



# Updates existing entry when user presses the save button on the Edit Event page
def update(request, pk):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		event = get_object_or_404(Event, pk=pk)
		if request.method == "POST":
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
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		event = get_object_or_404(Event, pk=pk)
		if request.method == "POST":
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

	def login(request):
#		context = {'text': 'You are not authorized to view this page. Please log in.'}
		render(request, 'login.html')
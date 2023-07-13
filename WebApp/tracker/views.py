from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserHabits
from django.http import JsonResponse


## In fact, when the /tracker URL is called, two things happen sequentialy.
# First, tracker() will render the trackerBase.html. But it will have no data.
@login_required
def tracker(request):
    return render(request, 'tracker/trackerBase.html')

## Then, javascript (tracker-actions.js) will fetch /load_tracker_data, triggering the 
# function below. It defines "user_habit" to represent the 
# UserHabit object associated with the User object that made the request.
@login_required
def load_tracker_data(request):
    
    user_habit = UserHabits.objects.filter(user=request.user).first()

    ## Then, the tracker_data variable is filled from the correct UserHabit's tracker_data (see the UserHabit model for more info).
    # If the user doesn't have tracker_data, then tracker_data variable will be just a empty dictionaire.
    if user_habit: 
        tracker_data = user_habit.tracker_data
    else:
        tracker_data = {} 

    ## In any case, it will return a Json object.
    # It is important to metion that this response will be received on front end by our tracker-actions.js. 
    # This js performs a final render on the page, to display the data for the user.
    return JsonResponse(tracker_data, safe=False) 


## When /tracker receives a POST, it will associate the user with it's tracker_data and
# update the tracker_data. 
# Then, it will save the new set (the updated set) of tracker_data into the db with the method save()
@login_required
def save_tracker_data(request):
    if request.method == 'POST':
        user = request.user
        tracker_data = request.POST.get('tracker_data') 

        user_habits, created = UserHabits.objects.get_or_create(user=user) 
        user_habits.tracker_data = tracker_data
        user_habits.save()

        return JsonResponse({'message': 'Tracker data saved successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.(?)'})


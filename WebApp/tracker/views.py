from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserHabits
from django.http import JsonResponse


@login_required
def tracker(request):
    return render(request, 'tracker/trackerBase.html')

@login_required
def load_tracker_data(request):
    # Busca os dados do tracker correspondentes ao usuário logado
    user_habit = UserHabits.objects.filter(user=request.user).first()

    if user_habit:
        tracker_data = user_habit.tracker_data
    else:
        tracker_data = {}  # Ou qualquer valor padrão que você desejar

    return JsonResponse(tracker_data, safe=False)

@login_required
def save_tracker_data(request):
    if request.method == 'POST':
        user = request.user
        tracker_data = request.POST.get('tracker_data') # assuming you're sending the data as form data

        user_habits, created = UserHabits.objects.get_or_create(user=user) 
        user_habits.tracker_data = tracker_data
        user_habits.save()

        return JsonResponse({'message': 'Tracker data saved successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.(?)'})


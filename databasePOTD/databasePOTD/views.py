from django.shortcuts import render, get_object_or_404, redirect
from .models import Friend
from .forms import FriendForm



def add_friend(request):
    friends = Friend.objects.all()
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_friend')  # Redirect to the friends list
    else:
        form = FriendForm()
    return render(request,'add_friend.html', {'form': form, 'friends': friends})



def update_friend(request, friend_id):
    friend = get_object_or_404(Friend, id=friend_id)

    if request.method == 'POST':
        form = FriendForm(request.POST, instance=friend)
        if form.is_valid():
            form.save()
            return redirect('add_friend')
    else:
        form = FriendForm(instance=friend)

    return render(request, 'update_friend.html', {'form': form})

def delete_friend(request, friend_id):
    friend = get_object_or_404(Friend, id=friend_id)
    friend.delete()
    return redirect('add_friend')

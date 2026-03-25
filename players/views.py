from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Player

class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players/player_list.html'

class PlayerDetailView(DetailView):
    model = Player
    context_object_name = 'player'
    template_name = 'players/player_detail.html'

class PlayerCreateView(CreateView):
    model = Player
    fields = '__all__'
    template_name = 'players/player_form.html'
    success_url = reverse_lazy('player_formation')

class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'players/player_form.html'
    success_url = reverse_lazy('player_formation')

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'players/player_confirm_delete.html'
    success_url = reverse_lazy('player_list')

class PlayerFormationView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players/player_formation.html'

from django.contrib import admin
from .models import PokemonCard

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "hp", "card_type", "attack","description","card_number", "release_date", "evolution_stage", "abilities")
    search_fields = ("name", "rarity", "hp", "card_type", "attack","description","card_number", "release_date", "evolution_stage", "abilities")

# Register your models here.

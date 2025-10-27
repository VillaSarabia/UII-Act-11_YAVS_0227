from django.apps import AppConfig


class AppPokemonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Nuevo nombre de la aplicación
    name = 'app_pokemon'
    # Nombre visible en el panel de administración
    verbose_name = 'Tienda de Cartas Pokémon' 

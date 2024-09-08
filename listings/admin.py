from django.contrib import admin
from listings.models import Band, Listing  # Importer vos modèles

# Configuration de l'affichage des groupes dans l'administration Django
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')  # Liste les champs à afficher dans la liste des objets

# Configuration de l'affichage des listings dans l'administration Django
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')  # Ajouter 'band' ici pour afficher le groupe associé

# Enregistrement des modèles dans l'admin avec leur configuration personnalisée
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)


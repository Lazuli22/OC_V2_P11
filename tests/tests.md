# Plan de tests unitaires pour l'application GUDLFT Registration Portal

1. Tests autour de l'authentification d'un utilisateur:
    * test_server.test_invalid_credentials: ce test doit démontrer qu'une connexion avec des identifiants erronées
    affiche la même page avec un message d'erreur
    
    * test_server.test_valid_credentials : ce test doit démontrer qu'une connexion avec des identifiants corrects
    affiche la page de reservation

    * test_server.test_empty-_credentials : ce test doit démontrer qu'une connexion avec des identifiants à vide 
    affiche la même page d'authentification avec un message d'erreur.

2. Tests autour de la gestion des points attribués à un club :
    * test_server.test_correct_points_allowed_per_clubs: ce test doit vérifier qu'un club 
    ne peut pas réserver plus de points qu'il lui est permis

    * test_server.test_update_points : ce test doit vérifier  la mise à jour des points d'un club
    après une reservation.

3. Tests autour de la gestion des réservations par compétitions : 
    * test_server.test_books_limited_12points : ce test doit vérifier que chaque club 
    peut au plus réserver 12 points par compétitions.

4. Tests autour de la gestion des competitions 
    * test_server.test_booking_past_competitions : ce test doit vérifier que la réservation de points ne doit pas être possible sur des compétitions anciennes.
    * test_server.test_booking_current_competitions : ce test doit vérifier que la réservation de points doit être possible sur des compétitions courantes.
    
5. Tests autour d'un tableau de bord

    * test_server.test_global_view_clubs : ce test doit vérifier l'affichage correct du tableau 
    récapitulatif des clubs avec leur points associés

# Plan de tests d'intégration pour l'application GUDLFT Registration Portal

1. Tests autour du login d'un utilisateur:

    * test_int_server.test_login_route: ce test doit démontrer qu'un utilisateur avec des crédentials valides peut bien
    s'authentifier et accéder à la réservation de clubs, peut se déconnecter et revenir sur le tableau de bord
    des clubs.
    
2. Tests de réservation de places par un utilisateur :
    * test_int_server.test_booking_route : ce test doit démontrer qu'un utilisateur authentifié peut réserver des places (10) d'une compétition courante (une compétition à venir). Il vérifie aussi que ce nombre de places est déduit du comptes des places de 
    de l'utilisateur et du nombre de places disponibles pour la compétition.

    * test_int_server.test_limite_booking_route : ce test doit démontrer qu'un utilisateur authentifié ne peut réserver au déla de 12 places d'une compétition courante.Il vérifie que le nombre de places de l'utilisateur et le nombre de places de la compétition restent inchangés.


    
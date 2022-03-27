# Plan de tests pour l'application GUDLFT Registration Portal

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

    * test_server.test_update_points : ce test doit vérifier que la mise des points d'un club
    après une reservation.

3. Tests autour de la gestion des réservations par compétitions : 
    * test_server.test_books_limited_12points : ce test doit vérifier que chaque club 
    peut au plus réserver 12 points par compétitions.

4. Tests autour de la gestion des competitions 
    * test_server.test_booking_current_competitions : ce test doit vérifier que la réservation de points doit être possible sur  une compétition en cours.

5. Tests autour d'un tableau de bord

    * test_server.test_global_view_clubs : ce test doit vérifier l'affichage correct du tableau 
    récapitulatif des clubs avec leur points associés

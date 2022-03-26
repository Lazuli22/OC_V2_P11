"""
A remplacer par un markdown :
-> test_server.test_invalid_credentials: ce test doit démontrer
qu'une connexion avec des identifiants erronnées
doit afficher la même page avec un message d'erreur

-> test_server.test_valid_credentials

-> test_server.test_empty-_credentials

->test_server.test_correct_points_allowed_per_clubs: ce test doit vérifier
qu'un club  ne peut pas réserver plus de points qu'il lui est permis

->test_server.test_books_limited_12points : ce test doit vérifier que chaque 
club peut au plus réserver 12 points par compétitions.

->test_server.test_booking_current_competitions : ce test doit vérifier que la
réservation de points se fait sur une compétitions en cours.

->test_server.test_update_points : ce test doit vérifier que la mise des points d'un club
après une reservation.

->test_server.test_global_view_clubs : ce test doit vérifier l'affichage correct du tableau 
récapitulatif des clubs avec leur points associés
"""
# À faire avant la remise

## 1. Publier les fichiers sur GitHub
1. Extraire cette archive ZIP.
2. Ouvrir le dossier `formation-developpeur` extrait.
3. Ouvrir PowerShell dans ce dossier.
4. Exécuter :
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\publier-sur-github.ps1
   ```
5. Suivre l'authentification GitHub si elle est demandée.
6. Vérifier le dépôt : https://github.com/ndouakacoupaulisrael-boop/formation-developpeur

Le dépôt est actuellement vide et ton compte y possède les droits administrateur. Le script initialise Git, configure `origin`, crée le commit et pousse la branche `main`.

## 2. Ajouter le professeur comme collaborateur
Dans le dépôt GitHub :
1. Ouvrir **Settings**.
2. Dans le menu latéral, ouvrir **Collaborators** ou **Collaborators and teams**.
3. Cliquer **Add people**.
4. Rechercher le pseudo exact **Sedrickgael**.
5. Sélectionner le compte de Sédrick Gaël Kouagni.
6. Pour lui permettre de consulter et contribuer au dépôt, choisir le rôle **Write** si cette option est proposée, puis envoyer l'invitation.
7. Vérifier que l'invitation apparaît comme en attente. Le professeur devra l'accepter.

## 3. Compléter les deux informations personnelles / d'équipe
- Dans `index.html` et `cv.html`, ajouter les coordonnées exactes : e-mail, téléphone et LinkedIn. Ne pas conserver une coordonnée fictive.
- Dans `application-console/TEAM.md`, remplacer les mentions « À compléter » par les vrais noms et contributions des membres de l'équipe.

## 4. Vérifications
- Portfolio : ouvrir `index.html`, tester le menu, puis réduire la largeur du navigateur pour démontrer le responsive.
- Console : dans `application-console`, lancer les commandes du README ; les 5 tests fournis passent déjà dans l'environnement de préparation.
- Django : installer les dépendances puis lancer `python manage.py check`, `python manage.py migrate` et `python manage.py runserver`.

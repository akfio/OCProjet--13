## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

-----------------------------------------------------------------------------------------------------------

## Déploiement


#### Comptes requis :

- Github
- CircleCi
- Dockerhub
- Heroku
- Sentry

#### Fonctionnement : 

##### Lorsqu'un commit est réalisé sur la branche master :

Le workflow 'master' du Pipeline du projet va se lancer, et il est composé de plusieurs jobs :

- le job 'build and test':
Il va lancer les test avec Pytest
Contrôler le linting PEP8 avec Flake8

- le job 'build-push-image-DockerHub':
Il va créer une image Docker 
Transmettre cette image vers le registre Dockerhub

- le job 'deploy-to-Heroku':
Il va déployer l'image docker vers Heroku


##### Lorsqu'un commit est réalisé sur une autre branche :

Le job 'build and test' est lancé.

#### Variables d'environnement :

Dans le projet CircleCI, accéde à `Project Settings`, accédedez à `Environment Variables` pui à `Add Environment Variables`:

Ccéation des variables suivantes :

 - DOCKER_USER : le user DockerHub
  
 - DOCKER_TOKEN : Token d'authentification recupérable dans GitHub via `Account settings`, `Security`, `New Access Token`
 
 -  HEROKU_API_TOKEN : Token Heroku récupéré avec la commande: ```python heroku authorizations:create```
 
 -  SENTRY_SDK_DNS : Url de Sentry 
 
 -  SECRET_KEY : Secret key Django
 
 -  HEROKU_APP_NAME : le nom de l'application (ici oc-lettings-8)



#### DockerHub : 

Le repository stockant en ligne l'image docker de l'application :

https://hub.docker.com/r/akfio/oc-lettings-8 

Récupérer l'application en local et lancer avec une seule commande : 

```python
docker run -it --publish 8000:8000 --name OCP13 akfio/oc-lettings-8:latest
```

#### Heroku : 

C'est l'hebergeur de l'application.

Si il faut recréer l'application voici la démarche à suivre : 

```python
heroku create oc-lettings-8
```
Lancer le pipline CircleCI, 
puis:
```python
git push heroku master

heroku run python3 manage.py migrate

heroku run python manage.py loaddata 'oc-lettings.json'
```


#### Sentry : 

https://sentry.io/organizations/akfio/projects/oc-lettings/?project=6034130

Sentry est utilisé pour faire du monitoring ou détecter les possibles bugs de l'application.
Pour l'utiliser, le package sentry_sdk est utilisé dans le settings.py et sa variable est enregistré dans CircleCi





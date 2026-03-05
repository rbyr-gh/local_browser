Projet Python S4 – Navigateur Local

Projet réalisé par trois étudiants de deuxième année de prépa intégrée de l’ESEO.

1. PRESENTATION DU PROJET

L’objectif de ce projet est de développer une application Python simulant un navigateur web fonctionnant entièrement hors ligne.

Cette application proposera une interface graphique centralisée permettant d’accéder à plusieurs outils et applications intégrées.

L’utilisateur pourra ouvrir différentes fonctionnalités sous forme d’onglets, à la manière d’un navigateur classique, et utiliser plusieurs modules simultanément.

Le projet vise à reproduire certaines fonctionnalités courantes d’un environnement numérique tout en restant indépendant d’une connexion Internet.

2. OBJECTIFS

Les principaux objectifs du projet sont les suivants :

Concevoir une interface graphique intuitive et esthétique

Mettre en place un système d’onglets permettant le multitâche

Développer plusieurs applications locales intégrées

Structurer le projet de manière modulaire et maintenable

Permettre un travail collaboratif via Git

3. INTERFACE UTILISATEUR

L’application devra proposer une interface graphique claire et simple d’utilisation.

Elle comprendra notamment :

    une barre de navigation

    un système d’onglets

    un menu d’accès aux différentes applications

    un système de gestion des fenêtres ou modules

L’interface devra être :

    stable

    ergonomique

    esthétique

    adaptée à une utilisation multitâche

Le développement de l’interface pourra être réalisé à l’aide de bibliothèques Python telles que :

    Tkinter

    PyQt

4. Fonctionnalités principales

Le navigateur local intégrera plusieurs modules accessibles depuis l’interface principale.

4.1 MINI ENCYCLOPEDIE (type Wikipédia)

Ce module permettra de consulter une base d’articles stockés localement.

Fonctionnalités :

    recherche d’articles

    affichage du contenu

    navigation entre différentes pages

    stockage des données en fichiers locaux

4.2 Messagerie locale

Une messagerie simulée permettant d’échanger des messages entre utilisateurs fictifs.

Fonctionnalités possibles :

    envoi de messages

    réception de messages

    historique des conversations

4.3 REPERTOIRE DE CONTACTS

Une application permettant de gérer un carnet d’adresses.

Fonctionnalités :

    ajout d’un contact

    modification d’un contact

    suppression d’un contact

    recherche de contacts

Informations stockées :

    nom

    prénom

    numéro de téléphone

    adresse e-mail (optionnelle)

4.4 APPLICATION DE PRISE DE NOTES

Un module simple permettant de rédiger et conserver des notes.

Fonctionnalités :

    création de notes

    modification

    suppression

    sauvegarde locale

4.5 CHRNOMETRE ET MINUTEUR

Un outil de gestion du temps.

Fonctionnalités :

    démarrer un chronomètre

    mettre en pause

    réinitialiser

    définir un minuteur avec alerte

4.6 JEUX INTEGRES

Le navigateur proposera également des jeux simples.

Morpion (Tic-Tac-Toe)

Fonctionnalités :

    mode deux joueurs

    détection automatique de victoire

    réinitialisation de la partie

Snake

Fonctionnalités :

    déplacement du serpent

    génération de nourriture

    gestion du score

    détection des collisions

5. ARCHITECTURE DU PROJET

Afin de faciliter la maintenance et le travail collaboratif, le projet devra être organisé de manière modulaire.

Exemple de structure :

projet-python-s4/
│
├── src/
│   ├── main.py
│   │
│   ├── interface/
│   │   └── navigateur.py
│   │
│   ├── applications/
│   │   ├── wikipedia.py
│   │   ├── messagerie.py
│   │   ├── notes.py
│   │   ├── contacts.py
│   │   └── chronometre.py
│   │
│   └── jeux/
│       ├── morpion.py
│       └── snake.py
│
├── data/
│   ├── articles/
│   ├── notes/
│   └── contacts/


profils utilisateurs

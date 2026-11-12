# Plan de construction de la boutique Shopify OMBRE

## Ce que je ferai dès que le connecteur Shopify répond (nouvelle session)
1. Lire la boutique : nom, devise, plan, thèmes, produits existants.
2. Créer les 4 produits de `produits.json` **en brouillon** (non visibles), avec SKU, poids et suivi de stock.
3. Créer les collections : « Matcha », « Coffrets & cadeaux ».
4. Créer les pages : Notre histoire, Livraison, Retours, FAQ. Les **mentions légales et les CGV restent en brouillon** tant que le SIRET n'existe pas.
5. Dupliquer le thème gratuit installé, puis appliquer l'identité OMBRE sur la **copie non publiée** : couleurs, polices, page d'accueil. Le connecteur bloque l'écriture sur le thème en ligne ; c'est voulu, la publication se fera avec ton accord.
6. Navigation : Boutique · Le Rituel · Notre histoire · FAQ.

## Page d'accueil (ordre des sections)
1. **Bannière** : « Le matcha né à l'ombre. » / « Jamais amer. Toujours tracé. » / bouton « Découvrir le Rituel »
2. **Bandeau de réassurance** : Livraison 48-72 h · Bio · Origine et récolte indiquées · Paiement sécurisé
3. **Produit vedette** : Le Rituel (54 €)
4. **« Pourquoi l'ombre »** : 3 colonnes (Ombre → Douceur → Vert intense)
5. **La gamme** : N°1, Duo, N°2
6. **Le rituel en 4 étapes** : 2 g · 70 ml · 75 °C · 20 s
7. **Avis clients** (après les premières ventes, jamais d'avis inventés)
8. **FAQ courte et inscription à la newsletter** (« -10 % sur votre première commande », à valider)

## Réglages du thème
- Couleurs : fond `#F4EFE6`, texte `#1F2A22`, bouton `#7FA33A` avec texte `#1F2A22`, accents `#C9B48A`
- Polices : titres **Fraunces** (si absente de la bibliothèque Shopify, une serif équivalente), texte **DM Sans**
- Rayons des boutons : 999 px (pilule), cartes : 12 px

## Ce qui nécessite ton intervention
- Photos réelles du produit : après réception du stock (le 26/11 au plus tôt).
- Activation des paiements, choix du forfait Shopify, nom de domaine : décisions et dépenses à valider.
- Publication du thème et ouverture de la boutique : uniquement avec ton accord.

## Avancement (12/11/2026)
- Le connecteur Shopify a demandé une nouvelle connexion : **aucune écriture dans la boutique pour l'instant**.
- Prêt à importer : `shopify/pages/*.html` + `shopify/pages/import.json`, générés par `python3 shopify/generer_pages.py` (dépendance : `pip install markdown`). Toutes les pages sont prévues **masquées** ; les notes internes et la garantie « Pas doux ? » (non validée) sont retirées du texte client.
- Reste à faire dès la reconnexion : étapes 1 à 6 ci-dessus.

# Audit des connecteurs, MCP et API

> Phase 0 — audit réalisé le **22/11/2026**.
> Règle appliquée : un connecteur n'est marqué « ✅ vérifié » que si un appel réel a répondu pendant cet audit.
> Les prix viennent des pages officielles quand elles étaient lisibles, sinon de sources tierces (signalé « à confirmer »).
> Aucune clé secrète n'a été lue ni affichée.

## 1. Synthèse en une page

| Statut | Signification |
|---|---|
| ✅ Vérifié | Connecté et testé par un appel réel pendant l'audit |
| 🟡 Disponible | Existe officiellement, connectable, pas encore branché |
| 🟠 Conditionnel | Demande un compte, une validation Google ou un abonnement |
| 🔴 Non retenu | Inutile, risqué ou contraire aux conditions d'utilisation |

| Outil | Statut | Coût | API officielle | MCP | Intérêt projet |
|---|---|---|---|---|---|
| **Shopify** (connecteur Claude) | ✅ Vérifié | Boutique en essai ; Basic ≈ 36 €/mois (à confirmer) | Oui (Admin GraphQL) | Oui, officiel, connecté | ⭐⭐⭐⭐⭐ |
| **Google Sheets** | ✅ Vérifié | Gratuit | Oui | Oui, connecté | ⭐⭐⭐⭐ |
| **Google Drive** | ✅ Vérifié | Gratuit (15 Go) | Oui | Oui, connecté | ⭐⭐⭐ |
| **Gmail** | ✅ Vérifié | Gratuit | Oui | Oui, connecté | ⭐⭐⭐⭐ (fournisseurs) |
| **Google Calendar** | ✅ Vérifié (listé connecté) | Gratuit | Oui | Oui, connecté | ⭐ |
| **GitHub** | ✅ Vérifié | Gratuit | Oui | Oui, connecté | ⭐⭐⭐⭐ (mémoire du projet) |
| **Claude Docs / Artifacts** | ✅ Disponible dans la session | Inclus | — | Oui | ⭐⭐⭐⭐ (tableaux de bord privés) |
| **TrendTrack** | 🟠 Conditionnel | 34 à 111 $/mois en annuel ; mensuel ≈ 49 à 159 $ (à confirmer) | Oui (API REST à crédits) | **Oui, officiel** (`https://api.trendtrack.io/v1/mcp`, OAuth) | ⭐⭐⭐⭐⭐ |
| **Google Ads** | 🟠 Conditionnel | API gratuite ; dépenses pub payantes | Oui | Oui, officiel (`googleads/google-ads-mcp`, lecture seule) | ⭐⭐⭐⭐⭐ (au lancement) |
| **Google Keyword Planner** | 🟠 Conditionnel | Gratuit avec un compte Google Ads | Via l'API Google Ads (accès Basic requis) | Via le MCP Google Ads | ⭐⭐⭐⭐⭐ |
| **Google Merchant Center** | 🟡 Disponible | Gratuit | Oui (Merchant API v1) | Non officiel | ⭐⭐⭐⭐ (via l'app Shopify) |
| **Google Analytics 4** | 🟡 Disponible | Gratuit | Oui (Data API) | Oui, officiel expérimental (`analytics-mcp`, lecture seule) | ⭐⭐⭐⭐ |
| **Google Search Console** | 🟡 Disponible | Gratuit | Oui | Pas de MCP officiel Google | ⭐⭐ (SEO plus tard) |
| **Google Trends** | 🟠 Conditionnel | Gratuit | API officielle **en alpha, sur candidature** | Non | ⭐⭐⭐⭐ (manuel + CSV) |
| **Microsoft Clarity** | 🟡 Disponible | Gratuit | API d'export de données | Non vérifié | ⭐⭐⭐ (après lancement, avec consentement) |
| **Brevo** | 🟡 Disponible | Gratuit 300 e-mails/jour | Oui | Non vérifié | ⭐⭐ (Shopify Email suffit au départ) |
| **Make** | 🟡 Disponible | Gratuit 1 000 crédits/mois, 2 scénarios | Oui | — | ⭐⭐ |
| **n8n** | 🟡 Disponible | Auto-hébergé gratuit mais serveur ≈ 4 à 7 $/mois ; cloud ≈ 20 €/mois | Oui | — | ⭐ (pas maintenant) |
| **Alibaba.com** | 🔴 API non accessible | Gratuit (site) | API réservée aux partenaires approuvés | Non | Process manuel structuré |
| **Fiverr** | Installé, **déconnecté** | Variable | — | Oui | ⭐ (visuels plus tard, si budget) |
| **ElevenLabs** | Clé injectée dans l'environnement | — | — | — | Aucun usage prévu |
| Stripe, Notion, Slack, Klaviyo | 🔴 Non retenu | — | — | — | Doublons (Shopify Payments, Drive, Gmail, Shopify Email) |

## 2. Ce que j'ai réellement trouvé dans l'environnement

### 2.1 Fichiers et configuration
- Dépôt `haydarnft-arch/E-commerce` : vide à part `README.md` (1 commit initial).
- **Aucun `.mcp.json`**, aucun dossier `.claude/` dans le projet, aucun MCP configuré au niveau utilisateur (`mcpServers` vide).
- Les MCP disponibles viennent des **connecteurs claude.ai** du compte, pas de fichiers locaux.
- Environnement cloud « Default » : **réseau non restreint**, pas de script d'installation. Un second environnement nommé « E-commerce OMBRE » existe (ancien projet).
- Une clé réseau est enregistrée pour `api.elevenlabs.io` (injectée par le proxy, valeur jamais visible). Elle ne sert pas au projet.
- Outils installés : Node 22, npm, pnpm, Python 3.13, Git, Docker, `gh`, `gcloud`, `jq`, Chromium et Playwright (captures d'écran et tests).
- Outils absents : Shopify CLI (installable gratuitement via npm), `sqlite3` en ligne de commande (Node 22 sait lire SQLite).

### 2.2 Connecteurs claude.ai (vérifiés par appel réel)

| Connecteur | Test effectué | Résultat |
|---|---|---|
| Shopify | `get-shop-info` + requête GraphQL en lecture | Boutique `dz9snc-bz.myshopify.com` (« Ma boutique »), EUR, France. **4 produits, 0 commande, 0 client.** Thème principal « OMBRE (brouillon) », thème Horizon non publié. |
| Gmail | Liste des libellés | Fonctionne. Des libellés « Fournisseurs/… » existent déjà (ancien projet). |
| Google Drive | 5 fichiers récents | Fonctionne. Deux feuilles d'un ancien projet (« OMBRE – Suivi fournisseurs », « HaydarMotion – Prospection »). |
| Google Sheets | Outils chargés | Fonctionne (même compte Google que Drive). |
| Google Calendar | Statut « connecté » | Non utilisé. |
| GitHub | Accès au dépôt | Fonctionne (lecture et écriture sur la branche de travail). |

> ⚠️ **Boutique Shopify existante.** Shopify indique exactement : *« Plan: trial — you'll need to upgrade before you can start selling and unlock full features »*.
> Cette boutique et ses 4 produits viennent du projet précédent. **Je n'y ai rien modifié.** Il faudra décider : la réutiliser plus tard (renommage, nettoyage) ou repartir de zéro. Voir `DECISION_LOG.md`.

### 2.3 Ce que le connecteur Shopify permet déjà
- Lecture et écriture GraphQL Admin (produits, collections, stocks, commandes, clients, remises, contenus).
- Édition de thème sur un thème **non publié** uniquement, avec captures d'écran.
- Requêtes analytics (ShopifyQL).
- Création de produits numériques, de collections, de remises.
- Outils hors boutique : génération de noms, vérification de domaines, aperçus de boutique.
- **Bloqué volontairement par Shopify** : remboursements, cartes cadeaux, gestion du personnel, publication et suppression de thème. Ces actions restent manuelles dans l'admin Shopify. C'est une bonne chose.

## 3. Fiches détaillées

Format de chaque fiche : utilité · coût · connexion · API · MCP · permissions · limites · risques · verdict.

### 3.1 TrendTrack — source prioritaire
- **Utilité** : découvrir des boutiques Shopify en croissance, des produits, des publicités Meta, Google et TikTok, et les e-mails des concurrents.
- **Coût** (page officielle, prix annuels ramenés au mois) : Starter **34 $/mois**, Pro **62 $/mois**, Business **111 $/mois**, Enterprise sur devis. Les prix mensuels n'étaient pas lisibles ; des sources tierces donnent **49 / 89 / 159 $** en mensuel. Une offre Black Friday affichait « jusqu'à −50 % sur l'annuel ». **À confirmer avant tout paiement.**
- **Connexion** : MCP distant officiel `https://api.trendtrack.io/v1/mcp`, authentification **OAuth 2.1** (pas de clé à copier). L'ajout se fait dans claude.ai → Paramètres → Connecteurs → connecteur personnalisé. **Seul l'utilisateur peut le faire.**
- **API** : oui, REST facturée en crédits. 10 000 crédits récurrents par mois sur chaque plan actif. Recharges : 1 $ = 1 000 crédits (minimum 10 $). Un résultat « boutique » ou « produit » coûte 4 crédits, une pub Meta 1,5, une requête échouée ou vide 0. Exemple : 20 boutiques = 80 crédits, donc environ 125 recherches de ce type par mois.
- **Outils MCP** cités : `search_shops`, `find_similar_shops`, `search_products`, `get_product`, `product_launch_radar`, `find_winning_products`, `search_ads`, `get_product_ads`, `search_google_ads_library`, `search_tiktok_library`, `brief_competitor`, `analyze_product`, `search_emails`, `analyze_shop_emails`, `daily_radar`, etc.
- **Permissions (scopes)** : `identity.read`, `discovery.read`, `brandtrackers.read/write`, `favorites.read/write`, `workspace_insights.read`. Les accès en lecture suffisent ; je n'utiliserai l'écriture que pour suivre des marques, avec votre accord.
- **Limites** : l'inclusion de l'API et du MCP par plan n'a pas pu être lue sur la page tarifs (la FAQ parle d'un accès gratuit limité aux outils `lookup`). Pas d'export CSV mentionné. Débits : Pro 120 requêtes/min, Business 250 requêtes/min.
- **Risques** : coût récurrent élevé pour un budget de 200 €. Les ventes et revenus affichés sont des **estimations**, jamais des chiffres comptables.
- **Verdict** : outil central de la phase 1, mais **uniquement pendant un sprint de recherche d'un mois** si vous n'êtes pas déjà abonné. Résiliation possible à tout moment selon la FAQ. Plan B légal si le MCP n'est pas inclus : saisie structurée ou export depuis l'interface vers `data/imports/trendtrack/*.csv`.

### 3.2 Shopify
- **Utilité** : la boutique, le catalogue, les commandes, les stocks, les clients et les analytics.
- **Coût** : boutique actuelle en **essai**. Basic ≈ **36 €/mois** en mensuel, ≈ 27 €/mois en annuel. Shopify Payments ≈ **1,5 % + 0,25 €** par vente sur Basic. Une passerelle externe ajoute 2 % de commission. Le plan Starter n'est plus ouvert aux nouveaux comptes. *Chiffres de sources tierces récentes, à confirmer sur shopify.com/fr/tarifs.*
- **Connexion** : connecteur officiel déjà actif. Pour l'application ECOMMERCE OS plus tard : une app « custom » dans l'admin Shopify, avec un jeton d'accès aux permissions minimales (`read_products`, `read_orders`, `read_inventory`, `read_customers`, `read_analytics`).
- **API** : Admin GraphQL (la REST est en fin de vie). Webhooks : commandes, stocks, remboursements.
- **Limites** : les webhooks exigent un serveur public, donc pas avant la phase 6. Shopify CLI n'est pas installé.
- **Apps officielles gratuites utiles** : Google & YouTube (flux Merchant Center + Google Ads), Shopify Email, Shopify Flow, Shopify Inbox, bandeau de consentement Customer Privacy. *Quotas gratuits à confirmer au moment de l'installation.*
- **Verdict** : indispensable, mais **pas de paiement avant la phase 5.**

### 3.3 Google Ads (dont Keyword Planner)
- **Utilité** : notre seul canal payant ; Keyword Planner donne les volumes et les CPC estimés.
- **Coût** : l'API est **gratuite** ; seules les dépenses publicitaires sont payantes. Le compte Google Ads est gratuit.
- **Accès à l'API** (documentation Google 2026) : depuis le **9/09/2026**, les niveaux d'accès sont rattachés au **projet Google Cloud**, et non plus au jeton développeur.
  - **Explorer** : 2 880 opérations/jour, mais **la planification de mots-clés n'est pas disponible.**
  - **Basic** : 15 000 opérations/jour, Keyword Planner disponible ; demande une **vérification de marque** du projet Cloud.
  - **Standard** : quasi illimité, exigences fonctionnelles minimales.
  - Un problème connu `AUTHORIZATION_ERROR` est signalé sur certains projets mis à niveau.
- **MCP** : officiel, `github.com/googleads/google-ads-mcp`, **en lecture seule** (rapports, diagnostic). Il se lance en local avec des identifiants OAuth et un ID de projet Cloud.
- **Permissions** : scope OAuth `adwords` sur le compte publicitaire uniquement.
- **Limites** : sans campagne active, Keyword Planner affiche des **fourchettes** de volume (ex. 1 k–10 k) et non des chiffres exacts.
- **Risques** : dépense incontrôlée. Règle absolue : **aucune campagne et aucune hausse de budget sans votre validation.**
- **Verdict** : en phase 1, Keyword Planner via l'**interface web** (gratuit, sans API). En phase 6, API et MCP en lecture pour les rapports. Les modifications de campagnes restent faites par vous ou après votre validation explicite.

### 3.4 Google Merchant Center
- **Utilité** : flux produits pour Google Shopping et les fiches gratuites ; diagnostic des refus (prix, livraison, disponibilité).
- **Coût** : gratuit.
- **API** : **Merchant API v1**. L'ancienne Content API for Shopping est **arrêtée depuis le 18/08/2026**.
- **Connexion recommandée** : l'app officielle Shopify **Google & YouTube** synchronise le catalogue, donc aucun code à écrire. L'API ne servira qu'au tableau de bord (état des produits, refus).
- **Verdict** : phase 6.

### 3.5 Google Analytics 4
- **Utilité** : sessions, sources, entonnoir e-commerce, revenus, conversion.
- **Coût** : gratuit.
- **MCP** : officiel mais **expérimental**, `analytics-mcp` (PyPI) / `googleanalytics/google-analytics-mcp`, **lecture seule**, via Application Default Credentials.
- **Connexion** : un compte de service ajouté en « Lecteur » sur la propriété GA4 est la piste la plus simple et la plus sûre.
- **Verdict** : phase 6. Le suivi se fait via l'intégration native Shopify, avec Consent Mode v2.

### 3.6 Google Search Console
- Gratuit, API officielle (Search Analytics : clics, impressions, CTR, positions). **Pas de MCP officiel Google** ; seuls des MCP communautaires existent, que je n'installerai pas sans revue. Utile après le lancement pour le SEO. **Priorité basse.**

### 3.7 Google Trends
- **API officielle** : existe **en alpha, sur candidature** (5 ans de données, échelle cohérente). Pas de garantie d'accès. → Je peux préparer la candidature avec vous (gratuit).
- **En attendant** : trends.google.fr en manuel. Le bouton d'export CSV de chaque graphique est autorisé ; les fichiers vont dans `data/imports/google-trends/`.
- **Non retenu** : les bibliothèques de scraping non officielles (`pytrends` et autres). Elles sont fragiles et contraires aux conditions de Google.

### 3.8 Alibaba / sourcing Chine
- Le programme API d'Alibaba.com est **réservé à des partenaires approuvés** ; aucune API acheteur publique n'est exploitable par nous.
- Les « scrapers » commerciaux (Apify et autres) violent les conditions du site, donc **non retenus**.
- **Process retenu** : recherche manuelle sur Alibaba, 1688 via agent et fournisseurs européens, puis fiche fournisseur standardisée importée en CSV. Les demandes de devis sont rédigées par moi comme **brouillons Gmail**, et c'est vous qui les envoyez. Les libellés Gmail « Fournisseurs/1-À contacter… 5-Retenus » existent déjà et peuvent servir.

### 3.9 Make
- Gratuit : 1 000 crédits/mois, **2 scénarios actifs**. Core ≈ 9 à 16 $/mois pour 10 000 crédits (sources divergentes).
- Connecteurs Shopify, Sheets, Gmail, Google Ads, Brevo et webhooks disponibles.
- Attention : un déclencheur qui interroge toutes les 5 minutes consomme environ 8 600 crédits/mois.
- **Verdict** : pas nécessaire au départ. Les tâches planifiées Claude et Shopify Flow couvrent les besoins.

### 3.10 n8n
- Community Edition auto-hébergée gratuite, mais elle demande **un serveur permanent** (≈ 4 à 7 $/mois). Notre conteneur Claude est éphémère. Cloud : pas d'offre gratuite (≈ 20 €/mois).
- **Verdict** : à reconsidérer en phase 8, si le volume le justifie.

### 3.11 Brevo
- Gratuit : **300 e-mails/jour** (marketing et transactionnels confondus), API disponible, mention « Sent with Brevo » imposée. Starter à partir d'environ 9 $/mois.
- **Verdict** : Shopify Email + Shopify Flow suffisent au lancement (bienvenue, panier abandonné, demande d'avis). On passe à Brevo seulement si une limite bloque.

### 3.12 Microsoft Clarity
- Gratuit : enregistrements de sessions, cartes de chaleur.
- **Depuis le 31/10/2025**, Clarity exige un **signal de consentement valide** pour les visiteurs de l'EEE, du Royaume-Uni et de la Suisse. Sans consentement, seules des données sans cookie sont collectées.
- **Verdict** : après le lancement, couplé au bandeau de consentement Shopify. À valider dans le Centre de conformité (CNIL).

### 3.13 Autres sources gratuites et officielles pour la recherche produit
| Source | Usage | Accès |
|---|---|---|
| Meta Ad Library | Pubs actives des concurrents ; portée des pubs dans l'UE (obligation DSA) | Gratuit, manuel |
| Google Ads Transparency Center | Pubs Google des concurrents | Gratuit, manuel |
| TikTok Creative Center | Tendances, produits et hashtags | Gratuit, manuel |
| Amazon.fr Meilleures ventes / Meilleures progressions | Signaux de demande par catégorie | Gratuit, consultation manuelle (pas de scraping) |
| Google Shopping (résultats) | Prix du marché, nombre de vendeurs | Gratuit, manuel |
| Forums, Reddit, avis clients 1 à 3 étoiles | Problèmes non résolus = différenciation | Gratuit, manuel |

### 3.14 Connecteurs non retenus
| Outil | Raison |
|---|---|
| Stripe | Shopify Payments est intégré et moins cher que l'ajout d'une passerelle externe (+2 %). |
| Notion | Doublon avec le dépôt Git + Google Drive/Sheets. |
| Slack | Doublon avec Gmail et les notifications Claude. |
| Klaviyo | Payant au-delà du gratuit ; Shopify Email suffit jusqu'à validation. |
| Outils de support client payants | Shopify Inbox (gratuit) + réponses préparées par Claude. |

## 4. Points de vigilance techniques

1. **Le conteneur Claude Code cloud est éphémère.** Tout ce qui doit durer va dans **Git** (documents, données CSV/JSON) ou dans **Google Sheets/Drive**. Une base SQLite locale est reconstructible à partir de ces fichiers, jamais la seule copie.
2. **Les API Google (Ads, GA4, Search Console) utilisent des jetons OAuth qui expirent chaque heure.** On ne peut donc pas simplement « coller une clé ». Trois options, à choisir en phase 6 :
   - un compte de service (GA4 et Search Console) ;
   - l'exécution des MCP sur votre ordinateur via Remote Control ;
   - des exports CSV manuels.
3. **Secrets** : jamais dans le code ni dans des variables d'environnement en clair. On utilise les « secrets réseau » de l'environnement cloud (injectés par le proxy) ou un gestionnaire dédié. `.env.example` ne contient que des noms.
4. **Permissions minimales** : lecture seule partout où c'est possible. Toute écriture (Shopify, Google Ads, e-mails) passe par votre validation.

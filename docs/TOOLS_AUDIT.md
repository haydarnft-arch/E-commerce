# Audit des outils, des coûts et des capacités d'automatisation

> Phase 0 — 22/11/2026. Complète `CONNECTORS_AUDIT.md`.

## 1. Claude Code Pro : ce dont nous disposons réellement

| Capacité | Disponible | Commentaire |
|---|---|---|
| Sessions cloud (claude.ai/code, appli mobile) | ✅ | Conteneur Linux éphémère, dépôt cloné à chaque session |
| Accès Internet | ✅ | Réseau « non restreint » sur l'environnement Default |
| Recherche web et lecture de pages | ✅ | Toutes les sources doivent être citées |
| Connecteurs MCP claude.ai | ✅ | Shopify, Gmail, Drive, Sheets, Calendar, GitHub ; TrendTrack ajoutable |
| Exécution de code (Node, Python, Docker) | ✅ | Construction et tests de l'application ECOMMERCE OS |
| Navigateur Chromium automatisé | ✅ | Tests du parcours d'achat et captures d'écran |
| **Tâches planifiées** | ✅ | Une session Claude peut être relancée à heure fixe (minimum horaire). Base des rapports quotidiens et hebdomadaires. |
| Artifacts (pages privées sur claude.ai) | ✅ | Tableaux de bord consultables sur téléphone, sans hébergement payant |
| Secrets réseau | ✅ | Clés API injectées par le proxy, jamais visibles dans le code |
| Accès à votre ordinateur (Remote Control) | Possible | Utile pour les outils Google en OAuth local |

### Limites de Claude Code Pro
- **Quota d'usage** : une fenêtre glissante de 5 heures plus un plafond hebdomadaire, partagés entre le chat, Claude Code et les tâches planifiées. Anthropic ne publie pas de nombre de jetons. Depuis le 14/09/2026, le plafond hebdomadaire est 25 % au-dessus de l'ancien niveau. Consultez votre usage avec `/usage`.
  → Conséquence : on regroupe le travail en sessions ciblées et on évite les tâches planifiées trop fréquentes.
- **Pas de mémoire entre sessions** en dehors du dépôt : `TASKS.md`, `DECISION_LOG.md` et `CHANGELOG.md` servent de mémoire. Ils sont mis à jour à chaque fin de session.
- **Pas de serveur permanent** : impossible de recevoir des webhooks Shopify ou d'héberger n8n dans le conteneur.
- **Actions irréversibles** : je ne peux ni payer, ni signer, ni créer un compte à votre nom, ni passer une vérification d'identité.

## 2. Coûts : outils gratuits et payants

| Outil | Gratuit | Payant | Quand payer |
|---|---|---|---|
| Claude Code Pro | — | Déjà payé | — |
| GitHub, Google Drive/Sheets/Gmail | ✅ | — | Jamais |
| Google Trends (web + CSV) | ✅ | — | Jamais |
| Keyword Planner (interface) | ✅ avec un compte Google Ads | — | Jamais (fourchettes sans campagne active) |
| Meta Ad Library, Google Ads Transparency, TikTok Creative Center | ✅ | — | Jamais |
| Merchant Center, GA4, Search Console, Clarity | ✅ | — | Jamais |
| Shopify Email, Flow, Inbox, app Google & YouTube | ✅ (quotas à confirmer) | Au-delà des quotas | Phase 7+ |
| Brevo | ✅ 300 e-mails/jour | ≈ 9 $/mois | Seulement si nécessaire |
| Make | ✅ 1 000 crédits/mois | ≈ 9 à 16 $/mois | Probablement jamais au départ |
| **TrendTrack** | Accès « lookup » limité | **34 à 49 $/mois (Starter)** à 62 à 89 $ (Pro) | Phase 1, **1 mois**, après votre validation |
| **Shopify Basic** | Essai en cours | ≈ 36 €/mois (+1,5 % + 0,25 €/vente) | Phase 5, juste avant d'ouvrir. Vérifier les offres d'appel du moment. |
| Nom de domaine | — | ≈ 10 à 15 €/an | Phase 5 |
| Échantillon produit | — | ≈ 15 à 50 € livré | Phase 3 |
| Google Ads | — | Budget de test | Phase 7, après votre validation |

## 3. Proposition de répartition des 200 € (à valider, rien n'est engagé)

| Poste | Montant indicatif | Phase | Commentaire |
|---|---|---|---|
| Outils de recherche (TrendTrack, 1 mois) | 0 à 45 € | 1 | **0 € si vous êtes déjà abonné** |
| Échantillon(s) | 30 à 40 € | 3 | Non négociable avant de vendre |
| Nom de domaine | 12 € | 5 | |
| Shopify (1er mois payant) | 1 à 36 € | 5 | Selon l'offre d'appel du moment |
| Test Google Ads | 70 à 100 € | 7 | Le minimum pour obtenir un signal |
| **Réserve de trésorerie** | **≥ 20 €** | — | Jamais dépensée sans décision explicite |

> ⚠️ **Constat honnête** : 200 € est un budget très serré. Un test Google Ads de 70 à 100 € donne un **premier signal**, pas une validation statistique.
> La sélection du produit doit donc viser un **panier moyen et une marge élevés** (marge contributive ≥ 15 à 20 € par commande). Sinon le CPA autorisé sera trop bas pour Google Ads.
> Tous les montants vont dans `BUDGET_LEDGER.md` au fur et à mesure.

## 4. Ce qui peut être automatisé

| Tâche | Comment | Quand |
|---|---|---|
| Collecte et normalisation des recherches produit | MCP TrendTrack + scripts d'import CSV | Phase 1 |
| Notation des produits sur 100 points | Module de scoring (code + tests) | Phase 2/4 |
| Calcul des marges, du CPA maximal et du ROAS de rentabilité | Profit Calculator | Phase 2/4 |
| Brouillons de demandes de devis fournisseurs | Gmail (brouillons uniquement) | Phase 3 |
| Fiches produit, textes, FAQ, CGV (brouillons) | Claude + connecteur Shopify | Phase 5 |
| Rapport quotidien (ventes, stocks, commandes en retard) | Tâche planifiée Claude + Shopify ShopifyQL | Phase 7 |
| Rapport hebdo Google Ads (CPC, CPA, ROAS, termes de recherche) | MCP Google Ads (lecture) | Phase 7 |
| E-mails clients (bienvenue, panier abandonné, avis) | Shopify Email + Flow | Phase 5/7 |
| Alertes (rupture, ROAS sous le seuil, commande bloquée) | Shopify Flow + tâche planifiée | Phase 7 |
| Réponses SAV préparées | Claude (brouillons à valider) | Phase 7 |
| Mise à jour du journal de décisions et des tâches | Claude, en fin de session | Toujours |

## 5. Ce qui ne peut pas (ou ne doit pas) être automatisé

| Élément | Raison |
|---|---|
| Paiements (abonnements, stock, échantillons, publicité) | Votre validation est obligatoire. Je n'ai pas de moyen de paiement et n'en veux pas. |
| Création des comptes (Google Ads, Merchant Center, Cloud, Shopify Payments) | Identité, KYC, vérification par téléphone ou pièce d'identité |
| Connexion OAuth de TrendTrack et des comptes Google | Clic d'autorisation de votre part |
| Immatriculation de l'entreprise, choix du statut | Démarche personnelle (URSSAF / guichet unique INPI) |
| Contrôle qualité de l'échantillon | Physique : vous devez avoir l'objet en main |
| Photos et vidéos du produit réel | En partie manuelles (photos de base) ; retouches assistées possibles |
| Envoi des e-mails aux fournisseurs et négociation finale | Je prépare ; vous envoyez et décidez |
| Lancement de campagne, hausse de budget | Validation humaine obligatoire |
| Remboursements, publication du thème | Bloqués par Shopify pour l'IA : action manuelle dans l'admin |

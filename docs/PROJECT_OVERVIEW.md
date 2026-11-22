# ECOMMERCE OS — Vue d'ensemble du projet

> Nom provisoire. Le nom commercial sera choisi **après** la validation du produit.

## Mission
Identifier, construire, lancer et développer une entreprise e-commerce rentable sur Shopify, avec Google Ads comme seul canal payant au lancement. Le marché se choisit **à partir des données**, sans idée préconçue.

## Contraintes
- Capital de départ : **200 €**, contrainte absolue. Aucune dépense sans validation (voir `BUDGET_LEDGER.md`).
- Aucune niche, aucun produit, aucune marque, aucun fournisseur choisi à ce jour.
- Le minimum d'abonnements ; les bénéfices sont réinvestis progressivement.
- Conformité France / UE vérifiée **avant** de choisir un produit.

## Statut actuel
- **Phase 0 (audit) : terminée.** Voir `CONNECTORS_AUDIT.md` et `TOOLS_AUDIT.md`.
- Prochaine étape : phase 1, étude de marché. Elle démarre dès que les questions ouvertes de `TASKS.md` ont une réponse.

## Architecture technique proposée

### Principe : un seul cerveau, des modules spécialisés
```
                      ┌────────────────────────────┐
                      │   Claude Code (cerveau)    │
                      │  sessions + tâches planif. │
                      └─────────────┬──────────────┘
          lit / écrit (avec validation pour toute action sensible)
   ┌───────────────┬────────────────┼────────────────┬────────────────┐
   ▼               ▼                ▼                ▼                ▼
TrendTrack     Shopify          Google Ads       GA4 / Merchant    Gmail / Sheets
 (MCP)        (MCP officiel)   (MCP lecture)     (API lecture)     (MCP)
   │               │                │                │                │
   └───────────────┴──── données normalisées ────────┴────────────────┘
                                    ▼
                  Dépôt Git = mémoire durable du projet
           docs/ (décisions)  ·  data/ (CSV/JSON versionnés)
                                    ▼
                    app/ — ECOMMERCE OS (Next.js + TS)
          Finder · Scoring · Calculateur · Fournisseurs · Budget · …
                                    ▼
          Tableaux de bord privés (Artifacts claude.ai) sur téléphone
```

### Choix techniques
| Couche | Choix | Pourquoi |
|---|---|---|
| Mémoire et données (phases 1 à 4) | Fichiers **CSV/JSON dans Git** + miroir Google Sheets | Le conteneur est éphémère ; Git est durable, versionné et gratuit. Sheets est lisible sur téléphone. |
| Base locale | **SQLite**, reconstruite depuis les fichiers | Rapide pour filtrer et comparer ; jamais la seule copie |
| Application | **Next.js + TypeScript + Tailwind CSS**, en français | Demandé ; un seul langage pour l'interface et la logique |
| Logique métier (scoring, rentabilité) | Fonctions TypeScript pures + **tests automatisés** | Calculs financiers vérifiables |
| Consultation | Artifacts claude.ai privés (gratuit), puis hébergement si besoin | Pas d'abonnement d'hébergement au départ |
| Données en direct (phase 6+) | **Supabase** (offre gratuite) ou fonction serverless gratuite | Seulement quand les webhooks Shopify deviennent utiles |
| Automatisations | Tâches planifiées Claude + Shopify Flow | Gratuit ; Make ou n8n seulement si nécessaire |

> Point à vérifier en phase 4 : l'offre gratuite Vercel « Hobby » est réservée à un usage **non commercial**. Si on héberge l'application, on comparera Cloudflare (offre gratuite, usage commercial autorisé) et Supabase.

### Règles de sécurité
- Permissions minimales, lecture seule par défaut.
- Aucun secret dans le dépôt ; `.env.example` ne contient que des noms.
- Toute écriture externe (Shopify, Google Ads, e-mail, paiement) se fait après votre validation, tracée dans `DECISION_LOG.md`.
- Jamais de données simulées présentées comme réelles. Les estimations (TrendTrack, Keyword Planner) sont étiquetées comme telles.

## Index des documents
| Document | Contenu | Phase |
|---|---|---|
| `CONNECTORS_AUDIT.md` | Connecteurs, MCP, API | 0 ✅ |
| `TOOLS_AUDIT.md` | Coûts, limites, automatisations | 0 ✅ |
| `ROADMAP.md` | Plan par phase | 0 ✅ |
| `DECISION_LOG.md` | Journal des décisions | continu |
| `BUDGET_LEDGER.md` | Registre des dépenses | continu |
| `NICHE_RESEARCH.md`, `TRENDTRACK_RESEARCH.md`, `KEYWORD_RESEARCH.md`, `COMPETITOR_ANALYSIS.md` | Étude de marché | 1 |
| `PRODUCT_DATABASE.md`, `PRODUCT_SCORING.md`, `LEGAL_COMPLIANCE.md` | Sélection | 2 |
| `SUPPLIER_RESEARCH.md`, `FINANCIAL_MODEL.md` | Sourcing et rentabilité | 3 |
| `SHOPIFY_ARCHITECTURE.md` | Boutique | 5 |
| `GOOGLE_ADS_STRATEGY.md`, `TRACKING_PLAN.md` | Acquisition | 6 |
| `AUTOMATION_PLAN.md` | Automatisations | 4 à 8 |
| `USER_GUIDE.md` | Guide utilisateur | 4 |

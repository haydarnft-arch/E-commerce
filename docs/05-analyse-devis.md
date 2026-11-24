# Analyse des devis fournisseurs — point du 17/11/2026

Sources : réponses e-mail des fournisseurs et grilles tarifaires officielles jointes (Matcha Matcha « Tarifs B2B 2026 », ASARUMI « Wholesale price list, édition novembre 2026 »). Tous les prix sont HT. Le suivi détaillé est dans la Google Sheet « OMBRE – Suivi fournisseurs ».

## 1. Réponses reçues

| Fournisseur | Pays | Matcha cérémonie bio | Commande min. | Points forts | Bloquants |
|---|---|---|---|---|---|
| **Matcha Matcha** (SKEYL SASU, Paris) | France | **199 €/kg** (1 kg), 189 € (5 kg), 179 € (10 kg) — Kagoshima, Yabukita, récolte 2026 | **1 kg** | Français, livraison 48 h à 1 sem., fouet 8 € et cuillère 2,50 €, devis possible avant l'immatriculation | Paiement à la commande. Vend aussi au détail (concurrent indirect). Analyses à demander |
| **ASARUMI** (Bucarest) | Roumanie (UE) | **275 €/kg** (bio Yame Kanayamidori, stock UE) | 1 kg / grade | Analyses du lot fournies d'office, certifiés bio UE + JAS, remplissage de boîtes 30 g à notre marque dès 1 kg | Plus cher. Port FedEx non chiffré. 100 % d'avance |
| **Kyosun** (+ plateforme MatchaB2B) | Tchéquie | Prix seulement après inscription | **5 kg / grade** | Gros importateur, documentation qualité | **N° de TVA intracommunautaire obligatoire** + minimum trop élevé pour le budget |
| **Moya Matcha** | Pologne | Pas encore de prix | — | — | A demandé l'origine souhaitée : réponse envoyée le 17/11 |
| **Thés Direct** | France | — | — | — | Pas de réponse : relance 1 envoyée le 17/11 |

## 2. Les vrais coûts sont plus élevés que dans l'étude

L'étude supposait **150 €/kg** [E]. Le marché réel pour du **bio japonais en petite quantité** est à **199-275 €/kg** [F]. Cela confirme la tension sur le matcha décrite dans l'étude.

Économie unitaire recalculée avec Matcha Matcha (fournisseur le moins cher en bio japonais) :

| Produit | Coût HT | Marge brute | Gain avant pub | Après cotisations micro |
|---|---|---|---|---|
| Le Rituel à **54 €** | 24,13 € | 48 % | 13,95 € | **7,65 €** ⚠️ |
| Le Rituel à **59 €** | 24,13 € | 52 % | 18,15 € | 11,27 € |
| N°1 Cérémonie à **27 €** | 8,83 € | 68 % | 13,46 € | 9,63 € |
| N°1 Cérémonie à **29 €** | 8,83 € | 70 % | 15,29 € | 11,20 € |
| Duo Cérémonie à 46 € | 17,66 € | 58 % | 18,26 € | 12,46 € |
| N°1 avec boîte remplie par ASARUMI, 27 € | 12,35 € | 56 % | 9,84 € | 6,00 € |

Hypothèses [E] : boîte vide et étiquette 2,50 €, support céramique 3 €, coffret 1,80 €, port client et frais de paiement comme dans `finance/modele.py`.

## 3. Recommandations (à valider)

1. **Fournisseur principal : Matcha Matcha** (France, 1 kg, le prix le plus bas en bio japonais, accessoires chez le même fournisseur, donc une seule livraison).
   **Fournisseur de secours : ASARUMI** (analyses fournies d'office, boîtes à notre marque possibles).
2. **Ajuster les prix** : Le Rituel à **59 €** (Nature & Découvertes vend un coffret équivalent 58,50 €) et N°1 à **29 €**. À 54 €, le coffret ne laisse pas assez de marge pour la publicité.
3. **Commander les échantillons avant le 26/11** : Matcha Matcha 10 g (5 € + 5 € de port) et ASARUMI 5 g (3,50 € + 9 € de port) → **~23 € au total**. C'est une dépense : **ton accord est nécessaire**.
4. **Exiger le certificat d'analyse du lot** de Matcha Matcha avant toute commande (il est disponible « sur simple demande »).
5. **Kyosun** : à revoir quand on aura un numéro de TVA intracommunautaire et des volumes de 5 kg.

## 4. Premier stock possible au 26/11 (Matcha Matcha, budget ~1 000 €)
- 1 kg de matcha cérémonie : 199 €
- 25 fouets + 25 cuillères à prix unitaire : 25 × 8 + 25 × 2,50 = 262,50 €
- Port : offert (franco de port à partir de 390 € HT)
- **Sous-total fournisseur : ~460 € HT** (TVA : 5,5 % sur le matcha, 20 % sur les accessoires)
- Il reste à trouver : boîtes vides 30 g, étiquettes, supports, coffrets.

---

## 5. Mise à jour du 24/11/2026

| Fournisseur | Nouvelle information |
|---|---|
| **Thés Direct** | A répondu le 17/11. Prix pros HT affichés sur leur site (non lisible depuis mon environnement). Aucun minimum, sacs de 1 kg, port 9,90 € (offert dès 300 €). **Préparation en 5 à 10 jours ouvrés** : trop lent pour un lancement début décembre. Pas d'échantillon à la demande. Origine et analyses non communiquées. |
| **Moya** (Varsovie) | Grille « marque blanche » de juillet 2026. Boîte 30 g bio cérémonie « Traditional » à notre marque : **10,30 €** l'unité, **minimum 250 boîtes** (≈ 2 575 €). Fouet 5,95 €, support porcelaine 4,45 €, cuillère 1,70 € (**minimum 100** chacun). **Échantillons offerts** (3 grades + hojicha), 15 € de port. Analyses fournies seulement après commande. |
| **Matcha Matcha** | Relance commerciale le 23/11 : propose une 1re commande sous 2 semaines et l'envoi de l'échantillon 10 g (5 €) sous 72 h. |
| **Kyosun** | Rappel : numéro de TVA intracommunautaire obligatoire. |

**Conclusion inchangée** : Matcha Matcha reste le meilleur fournisseur pour démarrer (1 kg, livraison rapide, prix au kilo le plus bas en bio japonais). **Moya devient intéressant en phase 2** : ses accessoires sont moins chers que ceux de Matcha Matcha, mais ses minimums (100 à 250 unités) dépassent le budget de lancement.

**Échantillons conseillés (décision fondateur)** : Matcha Matcha 10 g (5 € + 5 € de port) + Moya (gratuits, 15 € de port) = **25 €**. Ils remplaceraient ceux d'Asarumi, qui coûtent 12,50 € pour 5 g et sont plus chers à l'achat en vrac.

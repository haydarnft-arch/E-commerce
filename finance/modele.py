"""Modèle financier — phase étude. Toutes les valeurs marquées EST sont des estimations
à confirmer par devis fournisseurs. Exécution : python3 finance/modele.py"""

# ---------- 1. Économie unitaire par produit (matcha) ----------
PAY_PCT, PAY_FIX = 0.018, 0.25      # Shopify Payments ~1,5%+0,25€ (cartes UE) ; 1,8% blended pour PayPal/cartes hors UE (EST)
RETURNS = 0.02                       # provision retours/casse/remboursements (EST, alimentaire peu retourné)
INBOUND = 0.03                       # transport amont en % du coût d'achat (EST)
MICRO_SOCIAL = 0.123                 # URSSAF vente de marchandises 2026
VL_IR = 0.01                         # versement libératoire IR (si éligible)

produits = {
    # nom: (prix TTC, TVA, coût marchandise HT, frais de port payé par nous HT, port facturé client TTC)
    "Kit Rituel (30g cérémonie + chasen + cuillère + support)": (54.0, 0.14, 19.0, 5.80, 0.0),
    "Matcha Cérémonie 30g":                                       (27.0, 0.055, 6.5, 4.30, 3.90),
    "Duo Recharge 2x30g":                                         (46.0, 0.055, 13.0, 4.60, 0.0),
    "Matcha Latte 100g":                                          (24.0, 0.055, 7.8, 4.60, 3.90),
}

def unitaire(prix, tva, cogs, ship, ship_fact):
    enc_ttc = prix + ship_fact
    ht = prix / (1 + tva) + ship_fact / 1.2
    frais = enc_ttc * PAY_PCT + PAY_FIX
    marge_brute = ht - cogs * (1 + INBOUND)
    contrib = marge_brute - ship - 0.60 - frais - ht * RETURNS   # 0,60 € emballage expédition (EST)
    micro = ht * (MICRO_SOCIAL + VL_IR)
    return enc_ttc, ht, marge_brute, contrib, contrib - micro

print("=== ÉCONOMIE UNITAIRE (avant publicité) ===")
print(f"{'Produit':58} {'TTC':>6} {'HT':>6} {'MargeB':>7} {'%MB':>5} {'Contrib':>8} {'ApresMicro':>10}")
for n, p in produits.items():
    ttc, ht, mb, c, cm = unitaire(*p)
    print(f"{n:58} {ttc:6.2f} {ht:6.2f} {mb:7.2f} {mb/ht*100:4.0f}% {c:8.2f} {cm:10.2f}")

# ---------- 2. Comparaison des candidats (EST) ----------
print("\n=== COMPARAISON CANDIDATS — panier type, contribution avant pub (EST) ===")
cands = {  # panier TTC, TVA, coût HT, port HT, taux retours, réachat 12 mois (EST)
    "Matcha rituel (kit+recharges)":   (54, 0.14, 19.0, 5.8, 0.02, 0.40),
    "Mastications naturelles chien":   (32, 0.20, 11.0, 5.2, 0.02, 0.45),
    "Taie d'oreiller soie 22 momme":   (59, 0.20, 13.5, 4.6, 0.08, 0.10),
    "Bougie parfumée made in France":  (34, 0.20, 11.0, 6.9, 0.05, 0.20),
    "Chaussettes pilates (lot de 3)":  (29, 0.20, 5.5, 4.3, 0.06, 0.15),
}
for n, (p, t, c, s, r, rep) in cands.items():
    ht = p / (1 + t)
    contrib = ht - c * 1.03 - s - 0.6 - (p * PAY_PCT + PAY_FIX) - ht * r
    print(f"{n:34} panier {p:5.0f}€ TTC | HT {ht:5.2f} | contrib {contrib:6.2f}€ ({contrib/ht*100:3.0f}% HT) | CPA max 1re cde ≈ {contrib - ht*0.123:5.2f}€ | réachat EST {rep:.0%}")

# ---------- 3. Combien faut-il pour 5 000 € nets dans la poche ? ----------
def net_sasu(profit_annuel, pfu=0.314):
    is_ = min(profit_annuel, 42500) * 0.15 + max(profit_annuel - 42500, 0) * 0.25
    return (profit_annuel - is_) * (1 - pfu)

def profit_requis_sasu(net_mensuel=5000):
    lo, hi = 0, 1e6
    for _ in range(100):
        mid = (lo + hi) / 2
        if net_sasu(mid) / 12 < net_mensuel: lo = mid
        else: hi = mid
    return hi

P = profit_requis_sasu()
print(f"\n=== OBJECTIF 5 000 €/mois DISPONIBLES ===")
print(f"SASU (IS 15%/25% + flat tax 31,4% sur dividendes) : bénéfice avant IS requis ≈ {P:,.0f} €/an = {P/12:,.0f} €/mois")
FIXES = 450  # charges fixes mensuelles à ce stade (Shopify, apps, compta, assurance, banque, outils) EST
for nom, marge in [("Prudent", 0.15), ("Réaliste", 0.20), ("Ambitieux", 0.26)]:
    ca_ht = (P / 12 + FIXES) / marge
    ca_ttc = ca_ht * 1.10
    cmd = ca_ttc / 50
    print(f"{nom:9} marge après pub {marge:.0%} du CA HT -> CA ≈ {ca_ht:,.0f} € HT/mois ({ca_ttc:,.0f} € TTC), ≈ {cmd:,.0f} commandes/mois ({cmd/30:.0f}/jour) à 50 € TTC")
# Micro-entreprise : impossible d'atteindre l'objectif sous le plafond ?
for marge in (0.20, 0.26):
    ca = (5000 + FIXES) / (marge - MICRO_SOCIAL - VL_IR)
    print(f"Micro (marge {marge:.0%}) : CA requis ≈ {ca:,.0f} €/mois = {ca*12:,.0f} €/an vs plafond 203 100 € -> {'IMPOSSIBLE' if ca*12 > 203100 else 'possible'}")

# ---------- 4. Simulation mensuelle sur 24 mois ----------
# Hypothèses clés (EST) : le CPA se dégrade quand le budget augmente (audiences plus froides) ;
# la pub du mois suivant n'augmente que si le mois est rentable ; stock acheté à l'avance (BFR).
import math
SCEN = {
    #            CPA   panier1  panierRep  réachat/mois  orga départ  orga +/mois  croissance pub max
    "Prudent":   (30,   48,      40,        0.05,         8,           4,           0.25),
    "Réaliste":  (24,   52,      42,        0.08,         15,          8,           0.35),
    "Ambitieux": (19,   56,      45,        0.11,         25,          14,          0.45),
}
CMV, LOGI, FEES, RET, TVA_MIX = 0.37, 0.13, 0.035, 0.02, 0.10

def cpa_effectif(cpa, ads):
    return cpa * (1 + 0.15 * math.log2(1 + ads / 1000))

def simulate(nom, capital=750, mois=24):
    cpa, a1, a2, rr, o0, og, gmax = SCEN[nom]
    cash, base, ads, stock, statut, ca12 = capital, 0.0, 150.0, 0.0, "micro", []
    out = []
    for m in range(1, mois + 1):
        new = ads / cpa_effectif(cpa, ads) + o0 + og * (m - 1)
        rep = base * rr
        ca_ttc = new * a1 + rep * a2
        ca_ht = ca_ttc / (1 + TVA_MIX)
        ca12 = (ca12 + [ca_ht])[-12:]
        if statut == "micro" and sum(ca12) * 12 / len(ca12) > 150000:
            statut = "SASU"          # bascule avant le plafond micro (203 100 €) — décision à valider
        fixes = 120 if m <= 3 else (250 if m <= 9 else 450)
        if statut == "SASU": fixes += 150   # expert-comptable
        social = ca_ht * 0.133 if statut == "micro" else 0
        res = ca_ht * (1 - CMV - LOGI - FEES - RET) - ads - fixes - social
        net = res if statut == "micro" else net_sasu(max(res, 0) * 12) / 12
        achat = max(ca_ht * CMV * 1.3 - stock, 0)
        stock += achat - ca_ht * CMV
        cash += ca_ht * (1 - LOGI - FEES - RET) - ads - fixes - social - achat
        base = base * 0.93 + new
        out.append((m, round(ads), round(new + rep), round(ca_ttc), round(res), round(net), statut, round(cash)))
        # Règle d'accélération : on n'augmente la pub que si le mois est rentable ET que la pub
        # reste < 25 % du CA HT (MER > 4). Sinon on stabilise / on coupe.
        part_pub = ads / ca_ht if ca_ht else 1
        if res > 0 and part_pub < 0.25:
            ads = min(ads * (1 + gmax), max(cash, 0) * 0.6)
        elif part_pub > 0.30 or res < 0:
            ads = ads * 0.8
        ads = max(ads, 100)
    return out

for nom in SCEN:
    print(f"\n=== SIMULATION 24 MOIS — {nom} (capital 750 €) — EST ===")
    print(" Mois    Pub€   Cdes    CA TTC   Résultat  Net dispo  Statut   Tréso")
    first = None
    for m, ads, o, ca, r, n, st, c in simulate(nom):
        if n >= 5000 and first is None: first = m
        if m in (1, 2, 3, 6, 9, 12, 15, 18, 21, 24):
            print(f" {m:4} {ads:7} {o:6} {ca:9} {r:10} {n:10} {st:>6} {c:8}")
    print(f" -> 5 000 € nets/mois atteints : {'mois ' + str(first) if first else 'NON atteint en 24 mois'}")

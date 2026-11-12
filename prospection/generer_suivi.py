"""Génère prospection/suivi-fournisseurs.xlsx (CRM fournisseurs). python3 prospection/generer_suivi.py"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter

ENCRE, MATCHA, WASHI, BAMBOU = "1F2A22", "7FA33A", "F4EFE6", "C9B48A"
H = Font(bold=True, color="FFFFFF", name="Calibri", size=11)
HF = PatternFill("solid", fgColor=ENCRE)
thin = Side(style="thin", color="D9D2C3")
B = Border(left=thin, right=thin, top=thin, bottom=thin)
wb = Workbook()

def sheet(ws, headers, widths, rows=(), n_empty=30):
    ws.append(headers)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
        c = ws.cell(row=1, column=i); c.font = H; c.fill = HF
        c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[1].height = 34
    for r in rows: ws.append(r)
    last = len(rows) + 1 + n_empty
    for row in ws.iter_rows(min_row=2, max_row=last, max_col=len(headers)):
        for c in row:
            c.border = B; c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{last}"
    return last

# ---------- 1. Pipeline fournisseurs ----------
ws = wb.active; ws.title = "Fournisseurs"
STATUTS = ["1-À qualifier", "2-À contacter", "3-Devis demandé", "4-Relance 1", "5-Relance 2", "6-Devis reçu",
           "7-Échantillons", "8-Négociation", "9-Retenu", "X-Écarté", "Z-Sans réponse"]
hdr = ["ID", "Fournisseur", "Catégorie", "Pays / ville", "Site officiel", "E-mail pro", "Téléphone",
       "Source des coordonnées", "Coordonnées vérifiées ?", "Statut", "Priorité (1-3)", "Date 1er contact",
       "Date dernier échange", "Prochaine relance", "Jours sans réponse", "Lien fil Gmail",
       "Prix constaté public", "MOQ connu", "Modèle stock (achat ferme ?)", "Notes"]
w = [6, 24, 14, 16, 26, 26, 16, 26, 12, 16, 9, 12, 12, 12, 10, 22, 22, 14, 18, 40]
rows = [
 ["F01", "Thés Direct", "Matcha", "France – Aubagne (13)", "https://thesdirect.com", "info@thesdirect.com", "09 70 70 52 53",
  "Fiche Trustpilot de l'entreprise (12/11/2026)", "Non", "2-À contacter", 1, None, None, None, None, None,
  "Matcha cérémonie bio JP ~123,75 €/kg (sac 1 kg)", "1 kg ?", "À confirmer", "Certifié FR-BIO-01. Grossiste >600 réf. Vérifier compte pro et origine/récolte."],
 ["F02", "Grossiste-Thé / Grossiste-Boîte", "Matcha", "France", "https://grossiste-the.com", "À récupérer sur le site", "À récupérer",
  "—", "Non", "1-À qualifier", 1, None, None, None, None, None,
  "Cérémonie bio JP 199,90 € HT/kg ; JP bio 65,80 € HT/kg", "1 kg", "À confirmer", "Deux grades très différents : demander fiches techniques des deux."],
 ["F03", "matchamatcha.fr (Matcha Cérémonie Bio)", "Matcha", "France", "https://matchamatcha.fr", "À récupérer (page B2B)", "À récupérer",
  "—", "Non", "1-À qualifier", 1, None, None, None, None, None,
  "Non publié (paliers 5/10/20 kg)", "1 kg", "À confirmer", "Annonce revente + marque blanche."],
 ["F04", "Kyosun", "Matcha", "UE (société s.r.o. – pays à confirmer)", "https://www.kyosun.com/fr/", "À récupérer", "À récupérer",
  "—", "Non", "1-À qualifier", 2, None, None, None, None, None,
  "« dès 35 €/kg » (grade ?) ; ~80 €/kg cérémonie (annuaire)", "5 kg MB / 500 doypacks", "À confirmer", "Grade réel à vérifier : prix bas = risque qualité."],
 ["F05", "Moya Matcha", "Matcha", "Pologne", "https://b2b.moyamatcha.com", "wholesale@moyamatcha.com", "À récupérer",
  "Résultat de recherche (extrait usetorg.com) – à vérifier", "Non", "1-À qualifier", 2, None, None, None, None, None,
  "Non publié", "Non publié", "À confirmer", ""],
 ["F06", "MatchaB2B", "Matcha (marque blanche)", "À confirmer", "https://www.matchab2b.com", "À récupérer", "À récupérer",
  "—", "Non", "1-À qualifier", 3, None, None, None, None, None,
  "Non publié", "50 doypacks remplis", "À confirmer", "Délai annoncé 14-21 j. Localisation inconnue."],
 ["F07", "Matcha Passion GmbH (via Faire)", "Accessoires", "Allemagne", "https://www.faire.com/en-gb/product/p_bzpn92y39c", "Via Faire", "—",
  "Fiche Faire", "Non", "1-À qualifier", 2, None, None, None, None, None,
  "Chasen 100 brins PVC 12,64 £", "Minimum Faire", "Achat ferme", "Prix de gros visibles avec compte revendeur Faire."],
 ["F08", "Cupplement B.V. (via Faire)", "Accessoires", "Pays-Bas", "https://www.faire.com/en-gb/product/p_trsaqgf26d", "Via Faire", "—",
  "Fiche Faire", "Non", "1-À qualifier", 3, None, None, None, None, None,
  "Chasen PVC 12,98 £", "Minimum Faire", "Achat ferme", ""],
]
last = sheet(ws, hdr, w, rows)
dv = DataValidation(type="list", formula1='"' + ",".join(STATUTS) + '"', allow_blank=True)
ws.add_data_validation(dv); dv.add(f"J2:J{last}")
dv2 = DataValidation(type="list", formula1='"Oui,Non"'); ws.add_data_validation(dv2); dv2.add(f"I2:I{last}")
dv3 = DataValidation(type="list", formula1='"Achat ferme,Stock réservé à notre nom,À confirmer,REFUSÉ (dropshipping)"')
ws.add_data_validation(dv3); dv3.add(f"S2:S{last}")
for r in range(2, last + 1):
    ws[f"N{r}"] = f'=IF(M{r}="","",M{r}+5)'
    ws[f"O{r}"] = f'=IF(OR(M{r}="",LEFT(J{r},1)="6",LEFT(J{r},1)="9",LEFT(J{r},1)="X"),"",TODAY()-M{r})'
    for col in "LMN": ws[f"{col}{r}"].number_format = "DD/MM/YYYY"
ws.conditional_formatting.add(f"O2:O{last}", CellIsRule(operator="greaterThanOrEqual", formula=["5"], fill=PatternFill("solid", fgColor="F6C8B8")))
ws.conditional_formatting.add(f"A2:T{last}", FormulaRule(formula=['LEFT($J2,1)="9"'], fill=PatternFill("solid", fgColor="DCE9C8")))
ws.conditional_formatting.add(f"A2:T{last}", FormulaRule(formula=['LEFT($J2,1)="X"'], font=Font(color="9A9A9A", strike=True)))

# ---------- 2. Comparatif des devis ----------
wc = wb.create_sheet("Comparatif devis")
hdr = ["ID fournisseur", "Produit / grade", "Origine (préfecture)", "Récolte", "Bio (n° certif.)", "Analyses fournies ?",
       "Prix HT / kg", "Quantité devis (kg)", "Frais de port HT", "Remise %", "Coût rendu HT / kg",
       "Coût matière 30 g HT", "MOQ", "Délai (jours)", "Paiement", "Note goût /10 (échantillon)", "Note couleur /10",
       "Note fiabilité /10", "Score global /10", "Commentaire"]
w = [12, 24, 16, 10, 16, 12, 11, 11, 11, 9, 13, 12, 10, 10, 16, 12, 11, 11, 11, 36]
last = sheet(wc, hdr, w, n_empty=25)
for r in range(2, last + 1):
    wc[f"K{r}"] = f'=IF(OR(G{r}="",H{r}=""),"",(G{r}*H{r}*(1-N(J{r})/100)+N(I{r}))/H{r})'
    wc[f"L{r}"] = f'=IF(K{r}="","",K{r}*0.03)'
    wc[f"S{r}"] = f'=IF(COUNT(P{r}:R{r})<3,"",ROUND(P{r}*0.4+Q{r}*0.25+R{r}*0.35,1))'
    for col in "GIKL": wc[f"{col}{r}"].number_format = '#,##0.00 "€"'
dvb = DataValidation(type="list", formula1='"Oui,Non,Partiel"'); wc.add_data_validation(dvb); dvb.add(f"F2:F{last}")

# ---------- 3. Journal des échanges ----------
wj = wb.create_sheet("Journal échanges")
hdr = ["Date", "ID fournisseur", "Sens (envoyé/reçu)", "Canal", "Objet", "Résumé", "Engagements pris", "Action suivante", "Échéance", "Lien Gmail"]
sheet(wj, hdr, [12, 12, 14, 10, 28, 40, 30, 28, 12, 26], n_empty=60)

# ---------- 4. Négociation ----------
wn = wb.create_sheet("Négociation")
hdr = ["ID fournisseur", "Point négocié", "Offre initiale", "Notre demande", "Contre-offre", "Accord final", "Gain estimé €/an", "Statut", "Date"]
sheet(wn, hdr, [12, 26, 18, 18, 18, 18, 14, 14, 12], n_empty=25)

# ---------- 5. Mode d'emploi ----------
wm = wb.create_sheet("Mode d'emploi")
lignes = [
 "SUIVI FOURNISSEURS — mode d'emploi",
 "1. Fournisseurs : une ligne par fournisseur. Ne jamais saisir une coordonnée non sourcée ; renseigner 'Source' et 'Vérifiées ?'.",
 "2. Statuts : 1-À qualifier → 2-À contacter → 3-Devis demandé → 4/5-Relances → 6-Devis reçu → 7-Échantillons → 8-Négociation → 9-Retenu (ou X-Écarté / Z-Sans réponse).",
 "3. 'Prochaine relance' = dernier échange + 5 jours. 'Jours sans réponse' passe en rouge à partir de 5 jours.",
 "4. Modèle stock : seul 'Achat ferme' ou 'Stock réservé à notre nom' (facturé avant vente) est accepté. Tout fournisseur qui n'achète qu'après la commande client = REFUSÉ (dropshipping).",
 "5. Comparatif : saisir prix/kg, quantité, port, remise → coût rendu/kg et coût d'une portion 30 g calculés automatiquement. Notes d'échantillon : goût 40 %, couleur 25 %, fiabilité 35 %.",
 "6. Journal : chaque e-mail envoyé/reçu = une ligne, avec le lien du fil Gmail.",
 "7. Règle : aucun envoi d'e-mail, commande ou paiement sans validation explicite du fondateur.",
]
for l in lignes: wm.append([l])
wm.column_dimensions["A"].width = 140; wm["A1"].font = Font(bold=True, size=14, color=ENCRE)
wb.move_sheet("Mode d'emploi", offset=-4)
wb.save("prospection/suivi-fournisseurs.xlsx")
print("OK")

"""Convertit shopify/pages.md en HTML prêt à importer dans Shopify (pageCreate).

Usage : python3 shopify/generer_pages.py
Sortie : shopify/pages/<handle>.html et shopify/pages/import.json

Toutes les pages sont créées MASQUÉES (isPublished: false). La publication
se fait uniquement avec l'accord du fondateur.
Les notes internes (« Note interne », « à valider », « à activer seulement si
validée ») sont retirées du texte client et listées dans import.json.
"""
import json
import re
from pathlib import Path

import markdown

ICI = Path(__file__).parent
SORTIE = ICI / "pages"

# titre de section dans pages.md -> (titre Shopify, handle, bloquants avant publication)
PAGES = {
    "Notre histoire": ("Notre histoire", "notre-histoire", []),
    "Livraison": ("Livraison", "livraison", ["[E-MAIL CONTACT]", "seuil 45 € et délais à confirmer"]),
    "Retours & remboursements": ("Retours & remboursements", "retours", ["[E-MAIL CONTACT]", "[ADRESSE]"]),
    "Mentions légales": ("Mentions légales", "mentions-legales", ["SIRET", "adresse", "nom", "e-mail"]),
    "Conditions générales de vente": ("Conditions générales de vente", "cgv", ["texte complet à rédiger", "médiateur"]),
    "FAQ": ("FAQ", "faq", ["mention caféine à valider avec la fiche fournisseur"]),
}

NOTE_INTERNE = re.compile(
    r"\*\(?(Note interne|Formulation à valider|à activer seulement|à vérifier|tant que)[^*]*\)?\*",
    re.IGNORECASE,
)


def nettoyer(md: str) -> tuple[str, list[str]]:
    notes = [m.group(0).strip("*()") for m in NOTE_INTERNE.finditer(md)]
    lignes = []
    for ligne in md.splitlines():
        # garantie non validée : on retire le paragraphe entier
        if "Pas doux ?" in ligne:
            notes.append("Garantie « Pas doux ? » retirée en attendant validation")
            continue
        if ligne.strip().startswith("*Note interne"):
            continue
        lignes.append(NOTE_INTERNE.sub("", ligne).rstrip().replace(" .", "."))
    return "\n".join(lignes).strip(), notes


def main() -> None:
    source = (ICI / "pages.md").read_text(encoding="utf-8")
    sections = re.split(r"^## ", source, flags=re.MULTILINE)[1:]
    SORTIE.mkdir(exist_ok=True)
    manifeste = []
    for section in sections:
        entete, _, corps = section.partition("\n")
        cle = next((k for k in PAGES if entete.startswith(k)), None)
        if not cle:
            continue
        titre, handle, bloquants = PAGES[cle]
        corps = corps.replace("\n---", "").strip()
        md, notes = nettoyer(corps)
        html = markdown.markdown(md)
        (SORTIE / f"{handle}.html").write_text(html + "\n", encoding="utf-8")
        manifeste.append({
            "title": titre,
            "handle": handle,
            "isPublished": False,
            "bodyFile": f"{handle}.html",
            "bloquants_avant_publication": bloquants,
            "notes_retirees": notes,
        })
    (SORTIE / "import.json").write_text(
        json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{len(manifeste)} pages générées dans {SORTIE}")


if __name__ == "__main__":
    main()

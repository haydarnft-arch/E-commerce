"""Génère les fichiers du thème OMBRE (copie non publiée de Horizon).
Sortie : settings_data.json et index.json, à pousser via themeFilesUpsert."""
import json

S = {
  "logo_height": 36, "logo_height_mobile": 28,
  "page_background_color": "{{ settings.color_palette.background }}", "page_width": "narrow",
  "page_text_color": "{{ settings.color_palette.foreground }}",
  "type_body_font": "dm_sans_n4", "type_subheading_font": "dm_sans_n5",
  "type_heading_font": "fraunces_n6", "type_accent_font": "fraunces_n6",
  "type_size_paragraph": "16", "type_line_height_paragraph": "body-loose",
  "type_font_h1": "heading", "type_size_h1": "56", "type_line_height_h1": "display-tight", "type_letter_spacing_h1": "heading-normal", "type_case_h1": "none",
  "type_font_h2": "heading", "type_size_h2": "40", "type_line_height_h2": "display-tight", "type_letter_spacing_h2": "heading-normal", "type_case_h2": "none",
  "type_font_h3": "heading", "type_size_h3": "28", "type_line_height_h3": "display-normal", "type_letter_spacing_h3": "heading-normal", "type_case_h3": "none",
  "type_font_h4": "heading", "type_size_h4": "22", "type_line_height_h4": "display-tight",
  "type_font_h5": "subheading", "type_size_h5": "14", "type_line_height_h5": "display-loose",
  "type_font_h6": "subheading", "type_size_h6": "12", "type_line_height_h6": "display-loose",
  "page_transition_enabled": False, "transition_to_main_product": False, "card_hover_effect": "none",
  "badge_position": "top-right", "badge_corner_radius": 100,
  "badge_sale_background_color": "#C9B48A", "badge_sale_text_color": "{{ settings.color_palette.foreground }}",
  "badge_sold_out_background_color": "#E8E0D2", "badge_sold_out_text_color": "{{ settings.color_palette.foreground }}",
  "badge_text_transform": "none",
  "palette_primary_button_background": "#7FA33A", "palette_primary_button_text": "#1F2A22", "palette_primary_button_border": "#7FA33A",
  "primary_button_border_width": 0, "button_border_radius_primary": 100,
  "palette_secondary_button_background": "rgba(0,0,0,0)", "palette_secondary_button_text": "{{ settings.color_palette.foreground }}",
  "palette_secondary_button_border": "{{ settings.color_palette.foreground }}", "secondary_button_border_width": 1, "button_border_radius_secondary": 100,
  "cart_type": "drawer", "cart_price_font": "subheading", "show_cart_note": False, "show_add_discount_code": True,
  "drawer_background_color": "{{ settings.color_palette.background }}", "drawer_text_color": "{{ settings.color_palette.foreground }}",
  "drawer_border_color": "{{ settings.color_palette.color2 }}", "icon_stroke": "default",
  "palette_input_background": "#FFFFFF", "palette_input_text": "{{ settings.color_palette.color1 }}", "palette_input_border": "{{ settings.color_palette.color2 }}",
  "input_border_width": 1, "inputs_border_radius": 12,
  "popover_background_color": "{{ settings.color_palette.background }}", "popover_text_color": "{{ settings.color_palette.foreground }}",
  "popover_border_radius": 12, "popover_border_color": "{{ settings.color_palette.color2 }}", "popover_border_width": 1,
  "currency_code_enabled_product_pages": False, "currency_code_enabled_product_cards": False, "currency_code_enabled_cart_items": False,
  "quick_add_background": "{{ settings.color_palette.background }}", "quick_add_text": "{{ settings.color_palette.foreground }}",
  "product_corner_radius": 12, "card_corner_radius": 12, "show_variant_image": False,
  "variant_swatch_width": 34, "variant_swatch_height": 34, "variant_swatch_radius": 32,
  "palette_variant_background": "{{ settings.color_palette.background }}", "palette_variant_text": "{{ settings.color_palette.foreground }}",
  "palette_variant_border": "{{ settings.color_palette.color2 }}",
  "palette_selected_variant_background": "{{ settings.color_palette.foreground }}", "palette_selected_variant_text": "{{ settings.color_palette.background }}",
  "palette_selected_variant_border": "{{ settings.color_palette.foreground }}",
  "variant_button_border_width": 1, "variant_button_radius": 100, "variant_button_width": "equal-width-buttons",
  "color_palette": {"background": "#F4EFE6", "foreground": "#1F2A22", "color1": "#1F2A22", "color2": "#C9B48A"},
}
json.dump({"current": S, "presets": {"Horizon": S}}, open("settings_data.json", "w"), ensure_ascii=False, indent=2)

def text(html, preset="rte", align="left", color=None):
    s = {"text": html, "width": "100%", "max_width": "normal", "alignment": align, "type_preset": preset}
    if color: s["text_color"] = color
    return {"type": "text", "settings": s, "blocks": {}}

def section(blocks, bg="{{ settings.color_palette.background }}", direction="column", align="center"):
    order = list(blocks)
    return {"type": "section", "blocks": blocks, "block_order": order,
            "settings": {"content_direction": direction, "horizontal_alignment_flex_direction_column": align,
                         "gap": 24, "section_width": "page-width", "background_color": bg,
                         "padding-block-start": 56, "padding-block-end": 56}}

INK = "{{ settings.color_palette.foreground }}"
hero = {
  "type": "hero",
  "blocks": {
    "titre": text("<h1>Le matcha né à l'ombre.</h1>", "h1", "center", INK),
    "soustitre": text("<p>Jamais amer. Toujours tracé.</p>", "h4", "center", INK),
    "bouton": {"type": "button", "settings": {"label": "Découvrir le Rituel", "link": "shopify://products/le-rituel-coffret-matcha",
               "open_in_new_tab": False, "style_class": "button", "width": "fit-content", "width_mobile": "fit-content"}, "blocks": {}},
  },
  "block_order": ["titre", "soustitre", "bouton"],
  "settings": {"media_type_1": "image", "media_type_2": "image", "content_direction": "column", "vertical_on_mobile": True,
               "horizontal_alignment_flex_direction_column": "center", "vertical_alignment_flex_direction_column": "center",
               "gap": 24, "section_width": "page-width", "section_height": "medium", "background_color": "#E8E0D2",
               "toggle_overlay": False, "padding-block-start": 100, "padding-block-end": 100},
}
reassurance = section({
  "r1": text("<p><strong>Livraison 48-72 h</strong></p>", align="center"),
  "r2": text("<p><strong>Bio</strong></p>", align="center"),
  "r3": text("<p><strong>Origine et récolte indiquées</strong></p>", align="center"),
  "r4": text("<p><strong>Paiement sécurisé</strong></p>", align="center"),
}, bg="#C9B48A", direction="row")
reassurance["settings"].update({"padding-block-start": 16, "padding-block-end": 16, "horizontal_alignment": "space-around"})

def product_list(handle, titre, n):
    return {"type": "product-list", "blocks": {}, "settings": {
        "collection": handle, "layout_type": "grid", "max_products": n, "columns": min(n, 3), "mobile_columns": "1",
        "section_width": "page-width", "gap": 28, "background_color": "{{ settings.color_palette.background }}",
        "padding-block-start": 48, "padding-block-end": 48}, "_titre": titre}

vedette = product_list("coffrets-cadeaux", "Le Rituel", 1)
pourquoi = section({
  "t": text("<h2>Pourquoi l'ombre</h2>", "h2", "center"),
  "c1": text("<h4>Ombre</h4><p>Trois semaines avant la récolte, les théiers sont couverts.</p>", align="center"),
  "c2": text("<h4>Douceur</h4><p>Privée de soleil, la feuille perd son amertume.</p>", align="center"),
  "c3": text("<h4>Vert intense</h4><p>Un matcha vif, une mousse fine, un goût doux.</p>", align="center"),
})
gamme = product_list("matcha", "La gamme", 3)
rituel = section({
  "t": text("<h2>Le rituel en 4 étapes</h2>", "h2", "center"),
  "e": text("<p><strong>2 g</strong> de matcha · <strong>70 ml</strong> d'eau · <strong>75 °C</strong> · <strong>20 s</strong> de fouet en W</p>", "h4", "center"),
}, bg="#E8E0D2")
faq = section({
  "t": text("<h2>Questions fréquentes</h2>", "h2", "center"),
  "q1": text("<p><strong>Pourquoi n'est-il pas amer ?</strong><br>Cultivé à l'ombre et préparé à 75 °C, jamais à l'eau bouillante.</p>", align="center"),
  "q2": text("<p><strong>Combien de bols dans 30 g ?</strong><br>Environ 15, à 2 g par bol.</p>", align="center"),
  "lien": {"type": "button", "settings": {"label": "Toutes les questions", "link": "shopify://pages/faq", "style_class": "button-secondary",
           "width": "fit-content", "width_mobile": "fit-content"}, "blocks": {}},
})
SECTIONS = {"hero": hero, "reassurance": reassurance, "vedette": vedette, "pourquoi": pourquoi, "gamme": gamme, "rituel": rituel, "faq": faq}
for s in SECTIONS.values(): s.pop("_titre", None)
json.dump({"sections": SECTIONS, "order": list(SECTIONS)}, open("index.json", "w"), ensure_ascii=False, indent=2)
print("ok")

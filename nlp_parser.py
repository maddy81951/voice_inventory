import re
import spacy
nlp = spacy.load("en_core_web_sm")

UNITS = {"packs", "boxes", "cartons", "kgs", "liters", "bottles", "units", "pieces", "items", "grams", "ml", "cans", "bags"}

def parse_inventory_command(text):
    doc = nlp(text)
    
    quantity = None
    quantity_with_unit = None
    item = None
    location = None

    for i, token in enumerate(doc):
        if token.like_num:
            quantity = token.text
            unit = ""
            item_candidate = ""

            j = i + 1
            while j < len(doc):
                word = doc[j].text.lower()
                if word in UNITS and not unit:
                    unit = word
                elif doc[j].pos_ == "NOUN":
                    item_candidate = doc[j].text
                    break
                j += 1

            quantity_with_unit = f"{quantity} {unit}" if unit else quantity
            item = item_candidate
            break

    match = re.search(r'(shelf|rack|bin|section)\s*\w+', text, re.IGNORECASE)
    if match:
        location = match.group()

    return {
        "item": item,
        "quantity": quantity_with_unit,  
        "location": location
    }
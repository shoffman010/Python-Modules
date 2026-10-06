from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    normalized = ingredients.casefold()
    allowed = dark_spell_allowed_ingredients()

    is_valid = any(item in normalized for item in allowed)
    status = "VALID" if is_valid else "INVALID"

    return f"({ingredients} - {status})"
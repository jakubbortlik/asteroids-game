def get_text_widths(texts: list[str], font) -> list[int]:
    text_widths = [font.get_rect(line)[2] for line in texts]
    return text_widths

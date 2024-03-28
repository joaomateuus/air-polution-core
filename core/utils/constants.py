STATUS_DICT: dict = {
    "P": "Pobre",
    "MP": "Muito Pobre",
    "B": "Bom",
    "M": "Moderado",
    "R": "Razoável"
}

def convert_choices(status: str):
    return STATUS_DICT.get(status)
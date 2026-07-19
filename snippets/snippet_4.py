messages = [
    {"role": "system", "content": INSTRUCTION},  # quién eres, qué restricciones tienes
    {"role": "user", "content": (
        "Usa la siguiente información fiable para responder.\n\n"
        f"{contexto_formateado}\n\n"
        f"Pregunta: {query}"
    )},
]
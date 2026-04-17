import anthropic

# Pega tu clave real dentro de las comillas
client = anthropic.Anthropic(api_key="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")

message = client.messages.create(
    # Por esto:
    model="claude-3-5-sonnet-latest",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Responde solo con: Conexión exitosa"}
    ]
)

print(message.content[0].text)

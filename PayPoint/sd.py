import treepoem

# Código EAN-13 COMPLETO (con 13 dígitos)
codigo_completo = "1234567890128"  # Incluye el dígito de control

# Generar código de barras en formato PNG
imagen = treepoem.generate_barcode(
    barcode_type="ean13", 
    data=codigo_completo
)

# Guardar la imagen
imagen.convert("RGB").save("codigo_completo_ean13.png")

print("Código de barras generado y guardado como 'codigo_completo_ean13.png'")

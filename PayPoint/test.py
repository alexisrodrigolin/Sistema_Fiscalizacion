from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.graphics.barcode import code128
from reportlab.lib.colors import black, red
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import os
import subprocess

def generar_etiquetas(productos, disposicion, nombre_archivo="ofertas.pdf"):
    # Configurar disposición y orientación
    if disposicion == "1x1" or disposicion == "4x1":
        ancho, alto = landscape(A4)  # Apaisado
    else:
        ancho, alto = A4  # Vertical

    margen = 1 * cm
    estilos = {
        'titulo': ParagraphStyle(name='Titulo', fontSize=20, textColor=black, leading=10),
        'precio': ParagraphStyle(name='Precio', fontSize=20, textColor=black, leading=22),
        'normal': ParagraphStyle(name='Normal', fontSize=10, textColor=black, leading=12)
    }

    # Configurar disposición
    if disposicion == "1x1":
        columnas, filas = 1, 1
    elif disposicion == "2x1":
        columnas, filas = 1, 2  # Una columna, dos filas (una debajo de la otra)
    elif disposicion == "4x1":
        columnas, filas = 2, 2  # Dos columnas, dos filas (apaisado)
    else:
        raise ValueError("Disposición no válida: usar 1x1, 2x1 o 4x1")

    ancho_etiqueta = (ancho - 2 * margen) / columnas
    alto_etiqueta = (alto - 2 * margen) / filas

    c = canvas.Canvas(nombre_archivo, pagesize=(ancho, alto))

    for i, producto in enumerate(productos):
        col = i % columnas
        fila = (i // columnas) % filas

        if i % (columnas * filas) == 0 and i != 0:
            c.showPage()

        x = margen + col * ancho_etiqueta
        y = alto - margen - (fila + 1) * alto_etiqueta

        # Marco de la etiqueta
        c.rect(x, y, ancho_etiqueta, alto_etiqueta)

        # Contenido
        elementos = [
            (Paragraph(f"<b>~Oferta~</b> ", estilos['titulo']), 0.5 * cm),
            (Paragraph(producto['descripcion'], estilos['precio']), 1 * cm),
            (Paragraph(f"<b>Ahora:</b> $ {producto['precio']} ", estilos['precio']), 2 * cm),
            (Paragraph(f"<b>Antes:</b> <strike>$ {producto['precio_anterior']} </strike>", estilos['normal']), 2.5 * cm),
            (Paragraph(f"Precio por litro: $ {producto['precio_litro']} /L", estilos['normal']), 10 * cm),
        ]

        current_y = y + alto_etiqueta - 0.5 * cm
        for elemento, espacio in elementos:
            elemento.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
            elemento.drawOn(c, x + 0.5 * cm, current_y - elemento.height)
            current_y -= espacio + elemento.height

        # Código de barras


    c.save()


# Ejemplo de uso
productos = [
    {
        'titulo': '',
        'descripcion': 'Extra virgen 1L botella vidrio',
        'precio': '6.99',
        'precio_anterior': '8.99',
        'precio_litro': '6.99',
        'codigo_barras': '123456789012'
    },
    {
        'titulo': '',
        'descripcion': 'Leche Entera Pack Pack de 6 botellas de 1L',
        'precio': '4.50',
        'precio_anterior': '5.99',
        'precio_litro': '0.75',
        'codigo_barras': '987654321098'
    },
    {
        'titulo': 'Leche Entera',
        'descripcion': 'Pack de 6 botellas de 1L',
        'precio': '4.50',
        'precio_anterior': '5.99',
        'precio_litro': '0.75',
        'codigo_barras': '987654321098'
    },
    {
        'titulo': 'Leche Entera',
        'descripcion': 'Pack de 6 botellas de 1L',
        'precio': '4.50',
        'precio_anterior': '5.99',
        'precio_litro': '0.75',
        'codigo_barras': '987654321098'
    },
    # Agrega más productos según necesites
]

# disposicion = input("Elige disposición (1x1, 2x1, 4x1): ").strip().lower()
disposicion= "4x1"
generar_etiquetas(productos, disposicion)
print("PDF generado correctamente!") 
def abrir_pdf(ruta_archivo):
    # Para Windows
            if os.name == 'nt':
                os.startfile(ruta_archivo)
            # Para Linux o macOS
            else:
                opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
                subprocess.run([opener, ruta_archivo])

        # Ejemplo de uso
abrir_pdf("ofertas.pdf")
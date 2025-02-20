from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.graphics.barcode import code128
from reportlab.lib.colors import black, red
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

from reportlab.lib.enums import TA_CENTER, TA_RIGHT
import os
import subprocess

def generar_etiquetas(productos, disposicion, nombre_archivo=
                      "ofertas.pdf"):
    # Configurar disposición y orientación
    if disposicion == "1x1" :
        ancho, alto = landscape(A4)
        state=1.5  # Apaisado
    elif  disposicion == "4x1":
         ancho, alto = landscape(A4) 
         state=1
    else:
        state=1.2
        ancho, alto = A4  # Vertical
    tamanio_fuente = {
        '1x1': {'titulo': 38, 'precio': 48, 'normal': 15},
        '2x1': {'titulo': 30, 'precio': 38, 'normal': 14},
        '4x1': {'titulo': 22, 'precio': 30, 'normal': 8}
    }[disposicion]
    margen = 1 * cm                                     
    estilos = {
        'titulo': ParagraphStyle(
            name='Titulo', 
            fontSize=tamanio_fuente["titulo"], 
            textColor=black, 
            leading=29,  # Aumentar leading para evitar solapamiento
            alignment=TA_CENTER  # Alineación centrada
        ),
        'precio': ParagraphStyle(
            name='Precio',
            fontSize=tamanio_fuente["precio"],
            textColor=black,
            leading=22,
            alignment=TA_CENTER  # Alineación centrada
        ),
        'normal': ParagraphStyle(
            name='Normal',
            fontSize=tamanio_fuente['normal'],
            textColor=black,
            leading=20,
            alignment=TA_CENTER  # Alineación centrada
        ),
        'other': ParagraphStyle(
            name='other',
            fontSize=tamanio_fuente['normal'],
            textColor=black,
            leading=10,
              # Alineación centrada
        ),
        'other1': ParagraphStyle(
            name='other1',
            fontSize=tamanio_fuente['normal'],
            textColor=black,
            leading=12,
            alignment=TA_RIGHT
              # Alineación centrada
        )
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
       

        current_y = y + alto_etiqueta - 0.5 * cm
        oferta = Paragraph(f"<b><u>OFERTA</u></b>", estilos['precio'])
        oferta.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
        x_pos = x + (ancho_etiqueta - oferta.width) / 2  # Centrado horizontal
        oferta.drawOn(c, x_pos, y + alto_etiqueta - (0.5 * cm*state) - oferta.height)

        # 2. Descripción del producto
        descripcion = Paragraph(producto['descripcion'], estilos['titulo'])
        descripcion.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
        x_pos = x + (ancho_etiqueta - descripcion.width) / 2
        descripcion.drawOn(c, x_pos, y + alto_etiqueta - (1.9 * cm*state) - descripcion.height)

        # 3. Precio actual
        precio_actual = Paragraph(f"Ahora: <b>3x ${producto['precio']}</b>", estilos['precio'])
        precio_actual.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
        x_pos = x + (ancho_etiqueta - precio_actual.width) / 2
        precio_actual.drawOn(c, x_pos, y + alto_etiqueta - (4.5 * cm*state) - precio_actual.height)

        # 4. Precio anterior tachado
        precio_anterior = Paragraph(f"<b>Antes:</b> $ {producto['precio_anterior']}", estilos['other'])
        precio_anterior.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
        x_pos = x + 5*cm+(ancho_etiqueta - precio_anterior.width) / 2
        precio_anterior.drawOn(c, x_pos, y + alto_etiqueta - (6.5 * cm*state) - precio_anterior.height)

        # 5. Precio por litro
        precio_litro = Paragraph(f"Precio por litro: $ {producto['precio_litro']}/L", estilos['other'])
        precio_litro.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
        x_pos = x + 0.5 * cm  # Alineado a la izquierda
        precio_litro.drawOn(c, x_pos, y + 1 * cm)

        # 6. Código de barras numérico (alineado a la derecha)
        codigo = Paragraph(f"Art: {producto['codigo_barras']}", estilos['other1'])
        codigo.wrapOn(c, ancho_etiqueta - 1 * cm, alto_etiqueta)
        x_pos = x + ancho_etiqueta - codigo.width - 0.5 * cm  # Alineado a la derecha
        codigo.drawOn(c, x_pos, y + 1 * cm)
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
        'descripcion': 'Leche Entera Pack Pack de 6 boewewtellas de 1L',
        'precio': '11,999.99',
        'precio_anterior': '5.99',
        'precio_litro': '0.75',
        'codigo_barras': '987654321098'
    },
    {
        'titulo': 'Leche Entera',
        'descripcion': 'Pack de 6 botellas de 1L',
        'precio': '4499.99',
        'precio_anterior': '5.99',
        'precio_litro': '0.75',
        'codigo_barras': '987654321098'
    },
    {
        'titulo': 'Leche Entera',
        'descripcion': 'Pack de 6 botellas de 1L',
        'precio': '3999.99',
        'precio_anterior': '299925.99',
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
# abrir_pdf("ofertas.pdf")
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.utils import simpleSplit
import barcode

from barcode.ean import EuropeanArticleNumber13
from barcode.writer import ImageWriter
import os

# Configuración de la página
PAGE_WIDTH, PAGE_HEIGHT = A4
LABEL_WIDTH = 5.8 * cm
LABEL_HEIGHT = 2.8 * cm
MARGIN_LEFT = (PAGE_WIDTH - (3 * LABEL_WIDTH)) / 2
ROWS_PER_PAGE = 10

# Estilo del texto
NOMBRE_FUENTE = "Helvetica"
TAMANO_PRECIO = 20  # Reducido para mejor ajuste
TAMANO_TEXTO = 12
TAMANO_CODIGO = 6
ESPACIADO = 0.1 * cm

# Zonas verticales de la etiqueta (en cm desde el borde superior)
ZONA_NOMBRE = 0.4* cm
ZONA_PRECIO = 1.55 * cm
ZONA_CODIGO = 3.0 * cm

productos = [
    {"nombre": "1234567890123456789456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "123456789012345673456", "precio": "$59999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456783456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456789456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456789456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "123456789012345673456", "precio": "$59999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456783456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456789456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456789456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "123456789012345673456", "precio": "$59999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456783456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456783456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
    {"nombre": "Mermelada Arcor frutilla 450ml", "precio": "$499.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456789456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
    {"nombre": "1234567890123456789456", "precio": "$5999.99", "codigo": "1234567890123"},
    {"nombre": "mermelada\n Arcor frutilla 450ml", "precio": "$4999.99", "codigo": "1234567890123"},
]
# def generar_codigo_barras(codigo):
#     """Genera código de barras EAN-13 válido"""
#     try:
#         # Asegurar 13 dígitos (rellenar con ceros si es necesario)
#         codigo = codigo.zfill(13)[:13]
        
#         # Validar checksum y corregirlo si es necesario
#         ean = EuropeanArticleNumber13(codigo)
#         codigo_valido = ean.get_fullcode()  # Incluye el checksum correcto
        
#         # Configuración para EAN-13
#         writer = ImageWriter()
#         writer.set_options({
#             "module_width": 0.33,  # Ancho de barras (estándar EAN-13)
#             "module_height": 15,    # Altura en mm
#             "quiet_zone": 3.0,      # Márgenes laterales (3mm mínimo)
#             "font_size": 0          # Ocultar texto debajo
#         })
        
#         # Generar imagen
#         imagen = ean.render(writer)
#         nombre_archivo = f"temp_{codigo_valido}"
#         imagen.save(nombre_archivo)
#         return f"{nombre_archivo}.png"
    
#     except Exception as e:
#         print(f"Error en código {codigo}: {str(e)}")
#         return None
def generar_codigo_barras(codigo):
    codigo_barras = barcode.get_barcode_class("code128")
    imagen = codigo_barras(codigo, writer=ImageWriter())
    nombre_archivo = f"temp_{codigo}"
    imagen.save(nombre_archivo, options={"write_text": False})
    return f"{nombre_archivo}.png"

def crear_etiquetas():
    c = canvas.Canvas("etiquetas_precios.pdf", pagesize=A4)
    
    for i, producto in enumerate(productos):
        if i % (ROWS_PER_PAGE * 3) == 0 and i != 0:
            c.showPage()
        
        columna = i % 3
        fila = (i // 3) % ROWS_PER_PAGE
        
        x = MARGIN_LEFT + (columna * LABEL_WIDTH)
        y = PAGE_HEIGHT - LABEL_HEIGHT - (fila * LABEL_HEIGHT)-1*cm
        
        # Dibujar borde
        c.rect(x, y, LABEL_WIDTH, LABEL_HEIGHT)
        
        # Nombre del producto (parte superior)
        c.setFont(NOMBRE_FUENTE, TAMANO_TEXTO)
        nombre = simpleSplit(producto["nombre"], NOMBRE_FUENTE, TAMANO_TEXTO, LABEL_WIDTH - 2*ESPACIADO)
        text_y = y + LABEL_HEIGHT - ZONA_NOMBRE
        for line in nombre:
            c.drawString(x + ESPACIADO, text_y, line)
            text_y -= TAMANO_TEXTO * 1.2
 # Precio (centro destacado)
        c.setFont(NOMBRE_FUENTE , 8)
        c.drawCentredString(
            x + LABEL_WIDTH-0.7*cm,
            y +ESPACIADO ,
            "22/05/24"
        )
        c.setFont(NOMBRE_FUENTE, 8)
        c.drawCentredString(
            x + LABEL_WIDTH/2+0.2*cm,
            y +ESPACIADO ,
            "$49888.98 xLt"
        )
        # Precio (centro destacado)
        c.setFont(NOMBRE_FUENTE + "-Bold", TAMANO_PRECIO)
        c.drawCentredString(
            x + LABEL_WIDTH/2,
            y + LABEL_HEIGHT - ZONA_PRECIO,
            producto["precio"]
        )

        # Código de barras (parte inferior)
        codigo_img = generar_codigo_barras(producto["codigo"])
        c.drawImage(codigo_img, 
                   x +ESPACIADO-0.05*cm, 
                   y + ESPACIADO+0.25*cm, 
                   width=2.8*cm,  # Ancho reducido
                   height=0.6*cm,  # Altura reducida
                  )
        
        # Texto del código
        c.setFont(NOMBRE_FUENTE, TAMANO_CODIGO)
        c.drawCentredString(
            x +ESPACIADO+ 0.85*cm,
            y + ESPACIADO ,
            producto["codigo"]
        )
        
        os.remove(codigo_img)
    
    c.save()
    print("PDF generado correctamente")

if __name__ == "__main__":
    crear_etiquetas()
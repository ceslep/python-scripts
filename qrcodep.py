import qrcode

# URL a codificar
url = "https://iedeoccidente.edu.co/documentos/manual_de_convivencia_ieo.pdf"

# Crear el objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada "caja" del QR
    border=4,     # Grosor del borde (en cajas)
)

# Agregar la URL al objeto QR
qr.add_data(url)
qr.make(fit=True)

# Crear la imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en un archivo
img.save("manual_convivencia_qr.png")
print("El código QR se ha generado y guardado como 'manual_convivencia_qr.png'")

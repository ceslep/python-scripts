import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# -------------------------------
# CONFIGURACIÓN DEL CORREO
# -------------------------------
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "inasistenciasinstitutoguatica@gmail.com"
SENDER_PASSWORD = "deim efwu aavv pblf"  # ¡No uses tu contraseña real!

# -------------------------------
# CONFIGURACIÓN DEL ARCHIVO EXCEL
# -------------------------------
EXCEL_FILE = "inasistencias.xlsx"
EMAIL_COLUMN = "Dirección de correo electrónico"

# Leemos todas las hojas del Excel en un diccionario: {nombre_hoja: DataFrame}
sheets_dict = pd.read_excel(EXCEL_FILE, sheet_name=None)

# Conectamos al servidor SMTP
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

# -------------------------------
# RECORRER CADA HOJA Y ENVIAR CORREO
# -------------------------------
for sheet_name, df in sheets_dict.items():
    print(f"Procesando hoja: {sheet_name}")
    
    # Verificar que la columna de email exista
    if EMAIL_COLUMN not in df.columns:
        print(f"  La hoja '{sheet_name}' no contiene la columna '{EMAIL_COLUMN}'. Se omite.")
        continue

    # Obtener direcciones de correo únicas (descartando valores nulos)
    emails = df[EMAIL_COLUMN].dropna().unique()
    
    # Convertir el contenido de la hoja en una tabla HTML
    contenido_html = df.to_html(index=False)
    
    # Generar el cuerpo del mensaje (puedes personalizarlo)
    cuerpo = f"""
    <html>
      <body>
        <h2>Reporte de inasistencias para {sheet_name}</h2>
        <p>Adjunto se encuentra el reporte de inasistencias correspondiente a tu hoja de cálculo:</p>
        {contenido_html}
      </body>
    </html>
    """
    
    # Enviar correo a cada dirección encontrada en la hoja
    for recipient in emails:
        # Crear el objeto de mensaje
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = f"Reporte de inasistencias - {sheet_name}"
        
        # Adjuntar el cuerpo en formato HTML
        msg.attach(MIMEText(cuerpo, 'html'))
        
        try:
            server.send_message(msg)
            print(f"  Email enviado a {recipient} para la hoja '{sheet_name}'.")
        except Exception as e:
            print(f"  Error al enviar email a {recipient}: {e}")

# Cerrar la conexión con el servidor SMTP
server.quit()

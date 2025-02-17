import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# -------------------------------
# CONFIGURACIÓN DEL CORREO (desde el archivo .env)
# -------------------------------
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# -------------------------------
# CONFIGURACIÓN DEL ARCHIVO EXCEL
# -------------------------------
EXCEL_FILE = "inasistencias.xlsx"
EMAIL_COLUMN = "Dirección de correo electrónico"

# Columnas requeridas para el reporte
REQUIRED_COLUMNS = ["Estudiante", "Grupo", "Asignatura", "Horas de Inasistencia"]

# Leemos todas las hojas del Excel en un diccionario: {nombre_hoja: DataFrame}
sheets_dict = pd.read_excel(EXCEL_FILE, sheet_name=None)

# Conectamos al servidor SMTP
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

# Definir estilos CSS para la tabla (striped, encabezados centrados y columna "Horas de Inasistencia" centrada)
css_style = """
<style>
table {
    width: 100%;
    border-collapse: collapse;
    font-family: Arial, sans-serif;
    margin-bottom: 20px;
}
th, td {
    border: 1px solid #dee2e6;
    padding: 8px;
}
/* Encabezados centrados */
th {
    background-color: #007bff;
    color: white;
    text-align: center;
}
/* Por defecto, celdas alineadas a la izquierda */
td {
    text-align: left;
}
tr:nth-child(odd) {
    background-color: #f9f9f9;
}
tr:nth-child(even) {
    background-color: #e9e9e9;
}
/* Centrar la columna "Horas de Inasistencia" (suponiendo que es la cuarta columna) */
td:nth-child(4) {
    text-align: center;
}
</style>
"""

# -------------------------------
# RECORRER HOJAS Y ENVIAR CORREO A CADA DOCENTE
# -------------------------------
for sheet_name, df in sheets_dict.items():
    sheet_name_lower = sheet_name.lower()

    # Omitir la hoja "consolidado" o aquella que contenga "inasistencias" en su nombre
    if sheet_name_lower == "consolidado" or "inasistencias" in sheet_name_lower:
        print(f"Omitiendo hoja: {sheet_name}")
        continue

    # Verificar que la columna de correo exista
    if EMAIL_COLUMN not in df.columns:
        print(f"La hoja '{sheet_name}' no contiene la columna '{EMAIL_COLUMN}'. Se omite.")
        continue

    # Extraer correos válidos (no nulos) y únicos
    correos_validos = df[EMAIL_COLUMN].dropna().unique()

    # Si no se encuentra ningún correo, se omite la hoja
    if len(correos_validos) == 0:
        print(f"La hoja '{sheet_name}' no tiene correos válidos. Se omite.")
        continue

    # Tomar el primer correo como el destinatario del docente
    teacher_email = correos_validos[0]
    print(f"Procesando hoja: {sheet_name} para enviar a {teacher_email}")

    # Verificar que existan las columnas requeridas para el reporte
    if not all(col in df.columns for col in REQUIRED_COLUMNS):
        print(f"La hoja '{sheet_name}' no contiene todas las columnas requeridas: {REQUIRED_COLUMNS}. Se omite.")
        continue

    # Filtrar las columnas requeridas
    df_reporte = df[REQUIRED_COLUMNS].copy()

    # Asegurarse de que "Horas de Inasistencia" sea numérico (para sumar)
    df_reporte["Horas de Inasistencia"] = pd.to_numeric(df_reporte["Horas de Inasistencia"], errors="coerce").fillna(0)

    # Agrupar por Estudiante, Grupo y Asignatura, sumando las Horas de Inasistencia
    df_agrupado = df_reporte.groupby(["Estudiante", "Grupo", "Asignatura"], as_index=False)["Horas de Inasistencia"].sum()

    # Convertir el DataFrame agrupado en una tabla HTML sin índice y sin bordes predeterminados
    tabla_html = df_agrupado.to_html(index=False, border=0)

    # Generar el cuerpo del mensaje incluyendo el bloque de estilos CSS
    cuerpo = f"""
    <html>
      <head>
        {css_style}
      </head>
      <body>
        <h2>Reporte de inasistencias - {sheet_name}</h2>
        <p>Adjunto se encuentra el reporte de inasistencias acumuladas por Estudiante y Asignatura:</p>
        {tabla_html}
      </body>
    </html>
    """

    # Crear el objeto de mensaje
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = teacher_email
    msg['Subject'] = f"Reporte de inasistencias - {sheet_name}"

    # Adjuntar el cuerpo en formato HTML
    msg.attach(MIMEText(cuerpo, 'html'))

    try:
        server.send_message(msg)
        print(f"Email enviado para la hoja '{sheet_name}' a {teacher_email}.")
    except Exception as e:
        print(f"Error al enviar email para la hoja '{sheet_name}' a {teacher_email}: {e}")

# Cerrar la conexión con el servidor SMTP
server.quit()

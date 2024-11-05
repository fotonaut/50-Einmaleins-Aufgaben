import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

# Funktion, um eine Liste von zufälligen Einmaleins-Aufgaben zu generieren
def generate_tasks(count=50):
    tasks = []
    for _ in range(count):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        tasks.append(f"{a} x {b} = _____")
    return tasks

# Funktion, um die Aufgaben in ein PDF zu exportieren
def export_to_pdf(tasks, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Überschrift
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 40, "50 Einmaleins Aufgaben")

    # Zwei-Spalten Layout
    c.setFont("Helvetica", 12)
    col1_x = 100  # x-Position für die erste Spalte
    col2_x = width / 2 + 50  # x-Position für die zweite Spalte
    y_start = height - 80  # Startposition für die Aufgaben
    y_offset = 30  # Abstand zwischen den Aufgaben

    # 25 Aufgaben pro Spalte
    for i, task in enumerate(tasks[:25]):
        y_position = y_start - i * y_offset
        c.drawString(col1_x, y_position, f"{i + 1}) {task}")
        
    for i, task in enumerate(tasks[25:]):
        y_position = y_start - i * y_offset
        c.drawString(col2_x, y_position, f"{i + 26}) {task}")

    c.save()

# Hauptprogramm
tasks = generate_tasks(50)
now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d_%H%M%S")+"_einmaleins_aufgaben.pdf"
export_to_pdf(tasks, filename)
print("Die PDF-Datei mit den Einmaleins-Aufgaben wurde erstellt!")

import csv
import os

filename = 'C:\\Users\\bgale\\Downloads\\data.csv' # corrige
filename

if os.path.isfile(filename):
    print('El archivo ya existe, agregando datos...')
else:
    print('El archivo no existe, creando archivo...')
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Codigo', 'Lote', 'Pais', 'Caducidad', 'Descripcion'])

def add_to_csv(qr_code):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(qr_code)

while True:
    qr_code = input('Ingrese el codigo QR: ')
    if qr_code:  # Verificar si qr_code no es una cadena vacía
        qr_code = qr_code.split('Ñ')
        print(qr_code)
        add_to_csv(qr_code)
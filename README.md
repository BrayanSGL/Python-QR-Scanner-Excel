# CSV Data Management with QR Code Input

Este script de Python está diseñado para gestionar datos en un archivo CSV, centrándose específicamente en códigos QR. El script permite a los usuarios ingresar códigos QR, los cuales se procesan y se añaden a un archivo CSV. Si el archivo CSV ya existe, se añaden nuevos datos; si no existe, se crea un nuevo archivo.

## Uso

1. Ejecute el script en su entorno de Python preferido.
2. El script le solicitará que ingrese códigos QR.
3. Debe ingresar cada código QR, y el script dividirá la entrada por 'Ñ' para luego añadir los datos resultantes al archivo CSV.
4. Si el archivo CSV no existe, se creará y se añadirán datos subsiguientes.

## Información del Archivo

- **Nombre del Archivo:** data.csv
- **Campos:** 
  - Codigo
  - Lote
  - Pais
  - Caducidad
  - Descripcion

## Instrucciones

- Asegúrese de que el archivo CSV (data.csv) esté en la ubicación especificada (C:\\Users\\bgale\\Downloads\\).
- Si el archivo ya existe, el script añadirá nuevos datos. En caso contrario, se creará un nuevo archivo.

Siéntase libre de modificar el script según sus necesidades específicas.

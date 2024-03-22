import os
import glob
import docx
import openpyxl
from PyPDF2 import PdfReader

def extraer_metadatos_docx(archivo):
    doc = docx.Document(archivo)
    metadatos = {}
    metadatos = {
        'Título': doc.core_properties.title,
        'Autor': doc.core_properties.author,
        'Asunto': doc.core_properties.subject,
        'Palabras clave': doc.core_properties.keywords,
        'Comentarios': doc.core_properties.comments,
        'Categoría': doc.core_properties.category,
        'Administrador': doc.core_properties.last_modified_by,
        'Fecha de creación': doc.core_properties.created,
        'Fecha de modificación': doc.core_properties.modified,
    }
    return metadatos

def extraer_metadatos_xlsx(archivo):
    wb = openpyxl.load_workbook(archivo)
    metadatos = wb.properties.__dict__
    print(metadatos)
    return metadatos

def extraer_metadatos_pdf(archivo):
    reader = PdfReader(archivo)
    meta = reader.metadata

    return meta

def buscar_archivos(ruta):
    print(f'Buscando archivos en {ruta}...')
    archivos = glob.glob(os.path.join(ruta, '*'))
    print(f'Se encontraron {len(archivos)} archivos.')
    documentos = [archivo for archivo in archivos if archivo.endswith(('.docx', '.xlsx', '.pdf'))]
    return documentos

def main():
    ruta_directorio = input("Ingrese la ruta del directorio: ")
    documentos = buscar_archivos(ruta_directorio)

    for documento in documentos:
        if documento.endswith('.docx'):
            metadatos = extraer_metadatos_docx(documento)
        elif documento.endswith('.xlsx'):
            metadatos = extraer_metadatos_xlsx(documento)
        elif documento.endswith('.pdf'):
            metadatos = extraer_metadatos_pdf(documento)
        else:
            continue

        print(f'Metadatos de {documento}:')
        for clave, valor in metadatos.items():
            print(f'{clave}: {valor}')
        print()

if __name__ == "__main__":
    main()

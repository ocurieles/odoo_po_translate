from googletrans import Translator

def translate_po(input_file, output_file, src_lang='en', dest_lang='es'):
    translator = Translator()

    # Leer el archivo .po
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Variables para procesar el archivo
    new_lines = []
    current_msgid = None

    for line in lines:
        if line.startswith("msgid "):
            current_msgid = line[7:].strip().strip('"')
            new_lines.append(line)  # Agregar la línea original
        elif line.startswith("msgstr ") and current_msgid:
            if line.strip() == 'msgstr ""':  # Si no hay traducción existente
                translation = translator.translate(current_msgid, src=src_lang, dest=dest_lang).text
                new_lines.append(f'msgstr "{translation}"\n')  # Añadir traducción
            else:
                new_lines.append(line)  # Copiar traducción existente
            current_msgid = None
        else:
            new_lines.append(line)  # Copiar otras líneas sin cambios

    # Guardar el archivo traducido
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Configura los nombres de los archivos
input_po = "es_VE.po"  # Cambia esto por la ruta de tu archivo original
output_po = "es_VE_translated.po"  # Archivo traducido

# Ejecutar la traducción
translate_po(input_po, output_po)

print(f"Archivo traducido guardado en: {output_po}")

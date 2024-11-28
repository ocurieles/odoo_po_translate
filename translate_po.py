from translate import Translator

def translate_po(input_file, output_file, src_lang='en', dest_lang='es'):
    """
    Translates a .po file from one language to another.

    :param input_file: Path to the input .po file.
    :param output_file: Path to save the translated .po file.
    :param src_lang: Source language (default is English).
    :param dest_lang: Target language (default is Spanish).
    """
    # Initialize the translator
    translator = Translator(from_lang=src_lang, to_lang=dest_lang)

    # Read the .po file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Variables for processing the file
    new_lines = []
    current_msgid = None

    for line in lines:
        if line.startswith("msgid "):
            # Store the msgid content for translation
            current_msgid = line[7:].strip().strip('"')
            new_lines.append(line)  # Keep the original msgid
        elif line.startswith("msgstr ") and current_msgid:
            if line.strip() == 'msgstr ""':  # If no translation exists
                try:
                    # Translate the msgid content
                    translation = translator.translate(current_msgid)
                    print(translation)
                    new_lines.append(f'msgstr "{translation}"\n')  # Add the translation
                except Exception as e:
                    # Handle translation errors
                    print(f"Error translating '{current_msgid}': {e}")
                    new_lines.append('msgstr ""\n')  # Leave empty if translation fails
            else:
                new_lines.append(line)  # Keep the existing translation
            current_msgid = None
        else:
            new_lines.append(line)  # Keep other lines unchanged

    # Save the translated .po file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    print(f"Translated file saved to: {output_file}")

# Set the input and output file names
input_po = "es_VE.po"  # Change this to the path of your original file
output_po = "es_VE_translated.po"  # Translated file name

# Run the translation
translate_po(input_po, output_po)


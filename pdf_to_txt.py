import os
import PyPDF2

# Spécifie le répertoire contenant les fichiers PDF
input_directory = '/Users/Thomas/Desktop/3. Projets divers/4. Programmation/nanoGPT/data/shakespeare_char/HP series fr'
output_directory = os.path.join(input_directory, 'txt_files')

# Crée le répertoire de sortie s'il n'existe pas
os.makedirs(output_directory, exist_ok=True)

# Parcourt tous les fichiers dans le répertoire
for filename in os.listdir(input_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(input_directory, filename)
        txt_filename = f"{os.path.splitext(filename)[0]}.txt"
        txt_path = os.path.join(output_directory, txt_filename)

        # Lit et extrait le texte du fichier PDF
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            all_text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                all_text += page.extract_text()

            # Sauvegarde le texte extrait dans un fichier .txt
            with open(txt_path, 'w', encoding='utf-8') as text_file:
                text_file.write(all_text)

        print(f"Converted {filename} to {txt_filename}")




# for some reason, tous les espaces ont été convertis en tab, le code qui suit rétablit cela


# Chemin vers le répertoire contenant les fichiers TXT
txt_directory = '/Users/Thomas/Desktop/3. Projets divers/4. Programmation/nanoGPT/data/shakespeare_char/HP series fr/txt_files'

# Parcourt tous les fichiers dans le répertoire
for filename in os.listdir(txt_directory):
    if filename.endswith('.txt'):
        txt_path = os.path.join(txt_directory, filename)

        # Lit le contenu du fichier texte
        with open(txt_path, 'r', encoding='utf-8') as text_file:
            content = text_file.read()

        # Remplace les tabulations par des espaces
        content = content.replace('\t', ' ')

        # Réécrit le contenu modifié dans le fichier texte
        with open(txt_path, 'w', encoding='utf-8') as text_file:
            text_file.write(content)

        print(f"Converted tabs to spaces in {filename}")

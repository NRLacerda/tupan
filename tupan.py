import os

def search_files(folder_path, extensions):
    matching_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                matching_files.append((file_path, file_size))
    return matching_files
folder_path = ''
extensions = ''
print('-------------------------------------------------')
print("Bem vindo ao Tupan, o caçador de arquivos.")
print('-------------------------------------------------')
print("OBS: LEMBRE-SE QUE PARA CADA '\\' DEVE EXISTIR UMA OUTRA")
print("Por exemplo > 'C:\\' se torna 'C:\\\\'")
print('-------------------------------------------------')
print("Insira a pasta da qual você deseja caçar")
folder_path = input () # caminho q tu quer verificar
print("Agora o formato")
extensions = ['.pst'] # aqui vai a extensão q vc quer procurar
print('-------------------------------------------------')
print("Caminho Selecionado: "+folder_path)
matching_files = search_files(folder_path, extensions)
print('-------------------------------------------------')


if matching_files:
    print("Após algum tempo caçando isto foi o que encontramos:")
    for file_path, file_size in matching_files:
        formated_file_size = "{:.2e}".format(file_size)
        print(f"Arquivo: {file_path}  Tamanho: {formated_file_size} gigabytes")
else:
    print("A caça não resultou em nada.")

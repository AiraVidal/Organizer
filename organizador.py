import os
import shutil

def organizar_arquivos():
    # Obtenha o diretório atual do script
    diretorio_atual = os.getcwd()

    # Pasta de origem é o diretório atual
    pasta_origem = diretorio_atual

    # Pasta de destino é uma subpasta chamada "Organizados"
    pasta_destino = os.path.join(diretorio_atual, "Organizados")

    # Certifique-se de que a pasta de destino exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(pasta_origem)

    for arquivo in arquivos:
        # Construa o caminho completo para o arquivo
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        # Verifique se é um arquivo
        if os.path.isfile(caminho_arquivo):
            # Obtenha a extensão do arquivo
            _, extensao = os.path.splitext(arquivo)

            # Remova o ponto da extensão (opcional)
            extensao = extensao[1:]

            # Crie uma pasta para a extensão se não existir
            pasta_extensao = os.path.join(pasta_destino, extensao)
            if not os.path.exists(pasta_extensao):
                os.makedirs(pasta_extensao)

            # Construa o caminho de destino para o arquivo
            caminho_destino = os.path.join(pasta_extensao, arquivo)

            # Mova o arquivo para a pasta de destino
            shutil.move(caminho_arquivo, caminho_destino)

if __name__ == "__main__":
    organizar_arquivos()

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da API do Spotify
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Verifica se as credenciais foram carregadas corretamente
if not client_id or not client_secret:
    raise ValueError("Credenciais do Spotify não encontradas. Verifique o arquivo .env")

print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")

# Autenticação na API do Spotify
try:
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    # Verifica se o token foi obtido corretamente
    token_info = client_credentials_manager.get_access_token()
    if not token_info:
        raise ValueError("Falha ao obter o token de acesso. Verifique suas credenciais.")
    print("Autenticação bem-sucedida!")
except spotipy.exceptions.SpotifyException as e:
    raise ValueError(f"Erro ao autenticar na API do Spotify: {e}")

# Função para buscar artistas similares
def buscar_artistas_similares(nome_artista):
    try:
        # Busca o artista no Spotify
        resultados = sp.search(q=f"artist:{nome_artista}", type="artist", limit=1)
        if not resultados["artists"]["items"]:
            print(f"Artista '{nome_artista}' não encontrado no Spotify.")
            return None

        artista_id = resultados["artists"]["items"][0]["id"]
        artista_nome = resultados["artists"]["items"][0]["name"]

        try:
            # Busca artistas relacionados
            artistas_similares = sp.artist_related_artists(artista_id)
            if not artistas_similares["artists"]:
                print(f"Nenhum artista similar encontrado para '{artista_nome}'.")
                return None
            return artistas_similares["artists"]
        except spotipy.exceptions.SpotifyException as e:
            print(f"Erro ao buscar artistas similares: {e}")
            return None
    except spotipy.exceptions.SpotifyException as e:
        print(f"Erro ao buscar o artista '{nome_artista}': {e}")
        return None

# Função para recomendar gêneros similares
def recomendar_generos_similares(genero):
    try:
        recomendacoes = sp.recommendations(seed_genres=[genero], limit=5)
        if recomendacoes["tracks"]:
            print(f"\nRecomendações para o gênero '{genero}':")
            for track in recomendacoes["tracks"]:
                print(f"- {track['name']} by {track['artists'][0]['name']}")
        else:
            print("Nenhuma recomendação encontrada.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Erro ao buscar recomendações: {e}")

# Função principal para interação com o usuário
def main():
    print("Bem-vindo ao Recomendador de Música do Spotify!")
    while True:
        print("\nEscolha uma opção:")
        print("1. Buscar artistas similares")
        print("2. Recomendar gêneros similares")
        print("3. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            artista = input("Digite o nome de um artista: ")
            artistas_similares = buscar_artistas_similares(artista)
            if artistas_similares:
                print(f"\nArtistas similares a {artista}:")
                for artista in artistas_similares[:5]:  # Mostra os 5 primeiros artistas similares
                    print(f"- {artista['name']}")
        elif opcao == "2":
            genero = input("Digite um gênero musical: ")
            recomendar_generos_similares(genero)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
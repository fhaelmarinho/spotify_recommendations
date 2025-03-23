# Spotify Recommendations

Este projeto é um recomendador de músicas do Spotify que permite buscar artistas similares e recomendar gêneros musicais. Ele utiliza a API do Spotify para obter informações sobre artistas e gêneros.

## Funcionalidades

- Buscar artistas similares: Dado o nome de um artista, o programa retorna uma lista de artistas similares.
- Recomendar gêneros musicais: Dado um gênero musical, o programa retorna uma lista de recomendações de músicas desse gênero.

## Pré-requisitos

- Python 3.6 ou superior
- Conta de desenvolvedor no Spotify para obter as credenciais da API
- Biblioteca `spotipy` para interagir com a API do Spotify
- Biblioteca `python-dotenv` para carregar variáveis de ambiente a partir de um arquivo `.env`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/fhaelmarinho/spotify_recommendations.git
   cd spotify_recommendations
   ```

2. Crie um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais do Spotify:

   ```plaintext
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   ```

## Uso

1. Ative o ambiente virtual:

   ```bash
   source .venv/bin/activate
   ```

2. Execute o script:

   ```bash
   python recommendations.py
   ```

3. Siga as instruções no terminal para buscar artistas similares ou recomendar gêneros musicais.

## Estrutura do Projeto

```
Spotify_Recommendations/
├── .venv/
│   └── ... (arquivos do ambiente virtual)
├── .env
├── recommendations.py
├── requirements.txt
└── README.md
```

## Exemplo de Uso

Ao executar o script, você verá o seguinte menu no terminal:

```
Bem-vindo ao Recomendador de Música do Spotify!

Escolha uma opção:
1. Buscar artistas similares
2. Recomendar gêneros similares
3. Sair
Opção:
```

### Buscar Artistas Similares

Digite `1` e, em seguida, o nome de um artista. O programa retornará uma lista de artistas similares.

```
Opção: 1
Digite o nome de um artista: laura pausini

Artistas similares a laura pausini:
- Artista 1
- Artista 2
- Artista 3
- Artista 4
- Artista 5
```

### Recomendar Gêneros Similares

Digite `2` e, em seguida, o nome de um gênero musical. O programa retornará uma lista de recomendações de músicas desse gênero.

```
Opção: 2
Digite um gênero musical: pop

Recomendações para o gênero 'pop':
- Música 1 by Artista 1
- Música 2 by Artista 2
- Música 3 by Artista 3
- Música 4 by Artista 4
- Música 5 by Artista 5
```

### Sair

Digite `3` para sair do programa.

```
Opção: 3
Saindo...
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


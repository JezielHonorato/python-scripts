# Python Scripts

Scripts simples desenvolvidos em Python para executar tarefas genéricas, específicas ou apenas testar minhas habilidades.

## [`delete_repositories`](delete_repositories/delete_repositories.py)

Script criado para deletar todos os repositórios do GitHub de forma automatizada.

Meu GitHub estava ficando bagunçado após anos adicionando projetos sem me preocupar com comentários, README's ou organização. Decidi que a melhor forma era jogar tudo para o alto e começar de novo.

### Requisitos:

- [`requests`](https://pypi.org/project/requests/): para fazer requisições HTTP à API do GitHub.
- [`python-dotenv`](https://pypi.org/project/python-dotenv/): para carregar variáveis de ambiente do arquivo `.env`.

Instale com:

```bash
pip install -r requirements.txt
```

## [`web_scrapping`](web_scrapping/web_scrapping.py)

Script criado em 2021 para visualizar automaticamente as notas do SUAP.

Criei esse codigo em 2021 para por em pratica o que aprendi em python nas aulas de algoritimo do IFRN. Nos primeiros commits, ainda não sabia utilizar o .env e acabei salvando no github as minhas credênciais do SUAP. O codigo oje no repositorio esta foi adaptado para melhoress praticas porem sem perder sua ideia original.

### Requisitos:

- [`bs4`](https://pypi.org/project/beautifulsoup4/): para retirar informações de uma pagina web.
- [`selenium`](https://selenium-python.readthedocs.io/): para automatizar a interação com sites dinamicos.
- [`pandas`](https://pandas.pydata.org/getting_started.html): para automatizar a interação com sites dinamicos.

Instale com:

```bash
pip install -r requirements.txt
```

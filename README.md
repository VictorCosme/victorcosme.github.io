# Como escrever um post:
1. Abra o arquivo scripts/post.py.
2. Preencha as variáveis como se pede
3. Execute o script (será gerado um arquivo HTML no diretorio de posts)


# Hierarquia de diretórios
- index.html: é a pagina inicial do blog, contendo um feed cronologico das postagens do blog
- archive.html: é o arquivo do blog, contendo todos os posts organizados por data e por tags
- about.html: é a pagina "Sobre mim", contendo meu perfil na internet
- feed.xml: é o arquivo para sindicancia via RSS
- sitemap.xml: é um arquivo que eu ainda não sei pra que serve
- TEMPLATES/: diretório contendo arquivos base para geração de paginas HTML/CSS
- scripts/: diretório de arquivos python auxiliares na criação do blog
- posts: diretório onde ficam armazenados todas as postagens do blog
- posts/tags: diretório por enquanto inutil, mas vai servir de feed filtrado por tag (arquivos serão gerados automaticamente)
- media: diretório contendo fotos/videos/audios/icones/assets que serao linkados ao blog
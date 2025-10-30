import os

# === CONFIGURAÇÕES ===
SITE_URL = "https://victorcosme.github.io"
SITE_TITLE = "Victor Cosme"
AUTHOR_MAIL = "victorcosmemelo@gmail.com"

# === CAMINHOS ===
MD_DIR = "md_posts"
HTML_DIR = "posts"

os.makedirs(HTML_DIR, exist_ok=True)
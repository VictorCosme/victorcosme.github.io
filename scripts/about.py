from config import SITE_TITLE, AUTHOR_MAIL, SITE_URL
import utils

about_html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>{SITE_TITLE}</title>
<link rel="alternate" type="application/rss+xml" title="RSS" href="feed.xml" />
{utils.generate_style_tag()}
</head>
<body>
{utils.generate_header()}

<div class="h-card">
  <img class="u-photo" src="media/assets/avatar.jpg" alt="Foto de Victor Cosme">
  <div>
  <p class="p-name">João Victor Cosme Melo</p>
  <p class="p-note">Estudante de Ciência da Computação. Estritamente vegetariano. Chato de galochas.</p>
  <p><a class="u-url" href="{SITE_URL}">Meu blog</a> (you're already here, silly)</p>
  <p><a class="u-email" href="mailto:{AUTHOR_MAIL}">{AUTHOR_MAIL}</a></p>
  </div>
</div>

{utils.generate_footer()}
"""

with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_html)
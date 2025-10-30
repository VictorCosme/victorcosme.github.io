from config import SITE_TITLE
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
{utils.generate_footer()}
"""

with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_html)
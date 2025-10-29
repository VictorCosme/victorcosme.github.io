import os, re, markdown, datetime, html

# === CONFIGURAÇÕES ===
SITE_URL = "https://victorcosme.github.io"
SITE_TITLE = "Victor Cosme"

# === CAMINHOS ===
MD_DIR = "md_posts"
HTML_DIR = "posts"

os.makedirs(HTML_DIR, exist_ok=True)

# === LER TEMPLATE DO POST ===
with open("scripts/template_post.html", encoding="utf-8") as f:
    POST_TEMPLATE = f.read()

# === COLETAR POSTS ===
posts = []

for filename in sorted(os.listdir(MD_DIR), reverse=True):
    if filename.endswith(".md"):
        match = re.match(r"(\d{4}-\d{2}-\d{2})-(.*)\.md", filename)
        if not match:
            continue

        date_str, slug = match.groups()
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

        path_md = os.path.join(MD_DIR, filename)
        path_html = os.path.join(HTML_DIR, slug + ".html")

        with open(path_md, encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content, extensions=["extra"])
        title_match = re.search(r"^# (.*)", md_content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else slug.replace("-", " ").title()

        # gerar post html
        post_html = POST_TEMPLATE.replace("{{title}}", title)
        post_html = post_html.replace("{{date}}", date.strftime("%d/%m/%Y"))
        post_html = post_html.replace("{{content}}", html_content)

        with open(path_html, "w", encoding="utf-8") as f:
            f.write(post_html)

        posts.append({
            "title": title,
            "slug": slug,
            "date": date,
            "url": f"{SITE_URL}/posts/{slug}.html",
            "content_html": html_content
        })

# === GERAR INDEX.HTML ===
posts.sort(key=lambda p: p["date"], reverse=True)

index_html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>{SITE_TITLE}</title>
<link rel="alternate" type="application/rss+xml" title="RSS" href="feed.xml" />
<style>
body {{ font-family: sans-serif; max-width: 700px; margin: 40px auto; line-height: 1.6; color: #333; }}
a {{ color: #0077cc; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
h1, h2 {{ color: #111; }}
</style>
</head>
<body>
<h1>{SITE_TITLE}</h1>

<h2>Posts recentes</h2>
<ul>
"""

for p in posts:
    index_html += f'<li><a href="posts/{p["slug"]}.html">{p["title"]}</a> — {p["date"].strftime("%d/%m/%Y")}</li>\n'

index_html += """
</ul>
<p><a href="feed.xml">RSS</a></p>
</body></html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

# === GERAR FEED.RSS ===
rss_items = ""
for p in posts[:15]:  # últimos 15 posts
    safe_html = html.escape(p["content_html"])  # evita quebrar o XML
    rss_items += f"""
    <item>
        <title>{p['title']}</title>
        <link>{p['url']}</link>
        <guid>{p['url']}</guid>
        <pubDate>{p['date'].strftime('%a, %d %b %Y 00:00:00 +0000')}</pubDate>
        <description><![CDATA[{p["content_html"]}]]></description>
        <content:encoded><![CDATA[{p["content_html"]}]]></content:encoded>
    </item>
    """

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:content="http://purl.org/rss/1.0/modules/content/">
<channel>
    <title>{SITE_TITLE}</title>
    <link>{SITE_URL}</link>
    <language>pt-br</language>
    <lastBuildDate>{datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>
    {rss_items}
</channel>
</rss>
"""

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(rss)

print("✅ Blog e RSS gerados com sucesso!")

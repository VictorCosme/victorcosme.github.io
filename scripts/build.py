import os

import yaml
import markdown
import datetime

# Site info
SITE_TITLE = "Deveras Victor"
SITE_URL = "victorcosme.github.io/"

# Author info
AUTHOR_NAME = "Victor Cosme"
AUTHOR_MAIL = "victorcosmemelo@gmail.com"
AUTHOR_GITHUB = "github.com/victorcosme"

# Site links
BLOG_LINK = "blog.html"
ARCHIVE_PAGE_LINK = "archive.html"
ABOUT_PAGE_LINK = "index.html"
RSS_FEED_LINK = "feed.xml"
SITEMAP_LINK = "sitemap.xml"

# Directory tree
POSTS_DIR = "posts/"
MD_POSTS_DIR = "scripts/posts/"





def open_template(template):
    """Retorna o texto (pre-html) do template indicado."""
    with open(f"scripts/TEMPLATES/{template}_template.html", mode='r', encoding='UTF-8') as f:
        return f.read()


def save(content, path):
    """Salva o content (geralmente HTML) ao arquivo com o path indicado."""
    with open(path, mode='w', encoding='UTF-8') as f:
        f.write(content)


def identidade_autor():
    id = f"""
    <link rel="author" href="/{ABOUT_PAGE_LINK}" />
    <link rel="me" href="mailto:{AUTHOR_MAIL}" />
    <link rel="me" href="https://{AUTHOR_GITHUB}"/>
    """
    return id


def build_post(title, post_date_yyyy_mm_dd, content, tag_list, path):
    """Gera a página de uma postagem."""
    post_html = open_template('post')

    post_html = post_html.replace("{{POST_TITLE}}", title)
    post_html = post_html.replace("{{SITE_TITLE}}", SITE_TITLE)
    post_html = post_html.replace("{{ABOUT_PAGE_LINK}}", ABOUT_PAGE_LINK)
    post_html = post_html.replace("{{BLOG_LINK}}", BLOG_LINK)
    post_html = post_html.replace("{{AUTHOR_MAIL}}", AUTHOR_MAIL)
    post_html = post_html.replace("{{AUTHOR_GITHUB}}", AUTHOR_GITHUB)
    post_html = post_html.replace("{{POST_DATE_YYYY_MM_DD}}", post_date_yyyy_mm_dd)
    post_html = post_html.replace("{{POST_DATE_DD_bb_YYY}}", datetime.datetime.strptime(post_date_yyyy_mm_dd, "%Y-%m-%d").strftime("%d %b, %Y"))
    post_html = post_html.replace("{{AUTHOR_NAME}}", AUTHOR_NAME)
    post_html = post_html.replace("{{POST_CONTENT}}", content)
    post_html = post_html.replace("{{POST_TAGS}}", tags(tag_list))
    post_html = post_html.replace("{{SITE_URL}}", SITE_URL)
    post_html = post_html.replace("{{POSTS_DIR}}", POSTS_DIR)
    post_html = post_html.replace("{{POST_PATH}}", path)
    post_html = post_html.replace("{{footer}}", footer())
    post_html = post_html.replace("{{identidade_autor}}", identidade_autor())


    save(post_html, POSTS_DIR+path)


def build_about_page():
    about_html = open_template('about')

    about_html = about_html.replace("{{AUTHOR_NAME}}", AUTHOR_NAME)
    about_html = about_html.replace("{{RSS_FEED_LINK}}", RSS_FEED_LINK)
    about_html = about_html.replace("{{AUTHOR_MAIL}}", AUTHOR_MAIL)
    about_html = about_html.replace("{{AUTHOR_GITHUB}}", AUTHOR_GITHUB)
    about_html = about_html.replace("{{header}}", header())
    about_html = about_html.replace("{{SITE_URL}}", SITE_URL)
    about_html = about_html.replace("{{footer}}", footer())
    about_html = about_html.replace("{{identidade_autor}}", identidade_autor())


    save(about_html, ABOUT_PAGE_LINK)


def tags(tag_list):
    """Gera as tags de uma postagem a partir da lista de tags"""
    tags = ""
    for tag in tag_list:
        tags += f"<a href='tags/{tag}.html' rel='tag'>{tag}</a>\n"
    return tags

    
def header():
    header = f"""
    <header>
    <h1 class="p-name">{SITE_TITLE}</h1>
    <nav>
        <ul>
            <li><a href="/{ABOUT_PAGE_LINK}">Sobre mim</a></li>
            <li><a href="/{BLOG_LINK}">Blog</a></li>
            <li><a href="/{ARCHIVE_PAGE_LINK}">Arquivo</a></li>
            <li><a href="/{RSS_FEED_LINK}" target="_blank">RSS</a></li>
        </ul>
    </nav>
    </header>
    """
    return header

def footer():
    footer = f"""
    <footer>
        <p>© 2025 {AUTHOR_NAME} — Todos os direitos reservados.</p>
    </footer>
    """
    return footer


def load_posts():
    """Lê todos os arquivos .md com front matter YAML e retorna lista de posts."""
    posts = []
    for filename in os.listdir(MD_POSTS_DIR):
        if not filename.endswith(".md"):
            continue

        path = os.path.join(MD_POSTS_DIR, filename)
        with open(path, encoding="utf-8") as f:
            raw = f.read()

        if not raw.startswith("---"):
            print(f"[AVISO] Sem front matter em {filename}")
            continue

        parts = raw.split("---", 2)
        if len(parts) < 3:
            print(f"[AVISO] Front matter mal formatado em {filename}")
            continue

        meta = yaml.safe_load(parts[1])

        if meta.get("draft", False):
            continue  # ignora rascunhos

        body = parts[2]
        html_content = markdown.markdown(body, extensions=["fenced_code", "tables"])

        post = {
            "title": meta.get("title", "Sem título"),
            "date": str(meta.get("date", "0000-00-00")),
            "tags": meta.get("tags", []),
            "path": meta.get("path", filename.replace(".md", ".html")),
            "html": html_content,
        }

        posts.append(post)

    # Ordena por data (mais recente primeiro)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def update_posts(posts):
    """Gera os HTMLs individuais de cada post."""
    for post in posts:
        build_post(post["title"], post["date"], post["html"], post["tags"], post["path"])
        print(f"[OK] {post['title']} → {post['path']}")


def build_feed(posts):
    """Gera um feed RSS básico."""
    items = "\n".join(
        f"""
        <item>
            <title>{p['title']}</title>
            <link>https://{SITE_URL}{POSTS_DIR}{p['path']}</link>
            <pubDate>{p['date']}</pubDate>
            <description><![CDATA[{p['html']}]]></description>
        </item>
        """ for p in posts
    )

    rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>{SITE_TITLE}</title>
    <link>https://{SITE_URL}</link>
    <description>Feed de atualizações do blog</description>
    <lastBuildDate>{datetime.date.today()}</lastBuildDate>
    {items}
</channel>
</rss>"""

    with open(RSS_FEED_LINK, "w", encoding="utf-8") as f:
        f.write(rss)
    print("[OK] feed.xml atualizado.")


def build_index(posts):
    index_html = open_template('index')
    index_html = index_html.replace("{{SITE_TITLE}}", SITE_TITLE)
    index_html = index_html.replace("{{AUTHOR_NAME}}", AUTHOR_NAME)
    index_html = index_html.replace("{{RSS_FEED_LINK}}", RSS_FEED_LINK)
    index_html = index_html.replace("{{header}}", header())
    index_html = index_html.replace("{{footer}}", footer())
    index_html = index_html.replace("{{recent_posts}}", recent_posts(posts))
    index_html = index_html.replace("{{identidade_autor}}", identidade_autor())
    
    save(index_html, BLOG_LINK)


def recent_posts(posts):
    items = "\n".join(
            f'<li>{p["date"]} — <a href="{POSTS_DIR+p["path"]}">{p["title"]}</a></li>'
            for p in posts
    )
    recent = f"""
    <h2>Posts recentes</h2>
    <ul>
    {items}
    </ul>
    """
    return recent


def build_archive(posts):
    """Gera a página de arquivo geral e páginas de tags."""
    archive_html = open_template('archive')

    # Agrupa posts por tag
    tags_dict = {}
    for post in posts:
        for tag in post['tags']:
            tags_dict.setdefault(tag, []).append(post)

    # Cria se não existir o diretório 'tags'
    os.makedirs("tags", exist_ok=True)

    # Gera páginas individuais por tag
    for tag, tag_posts in tags_dict.items():
        tag_items = "\n".join(
            f'<li>{p["date"]} — <a href="../../{POSTS_DIR}{p["path"]}">{p["title"]}</a></li>'
            for p in tag_posts
        )
        tag_html = open_template('tag')
        tag_html = tag_html.replace("{{TAG_NAME}}", tag)
        tag_html = tag_html.replace("{{SITE_TITLE}}", SITE_TITLE)
        tag_html = tag_html.replace("{{header}}", header())
        tag_html = tag_html.replace("{{footer}}", footer())
        tag_html = tag_html.replace("{{TAG_POSTS}}", f"<ul>{tag_items}</ul>")
        tag_html = tag_html.replace("{{SITE_URL}}", SITE_URL)
        tag_html = tag_html.replace("{{identidade_autor}}", identidade_autor())


        save(tag_html, f"{POSTS_DIR}tags/{tag}.html")
        print(f"[OK] Página da tag '{tag}' criada.")

    # Monta o arquivo geral
    max_count = max(len(posts) for posts in tags_dict.values())
    min_count = min(len(posts) for posts in tags_dict.values())

    def scale_font(count, min_size=10, max_size=32):
        # Escala linear entre min_size e max_size
        if max_count == min_count:
            return (min_size + max_size) / 2
        return min_size + (count - min_count) * (max_size - min_size) / (max_count - min_count)

    all_tags_html = "\n".join(
        f"<a href='{POSTS_DIR}tags/{tag}.html' "
        f"style='font-size:{scale_font(len(posts))}px; margin:5px; text-decoration:none;'>"
        f"{tag}</a>"
        for tag, posts in tags_dict.items()
    )


    archive_html = archive_html.replace("{{SITE_TITLE}}", SITE_TITLE)
    archive_html = archive_html.replace("{{header}}", header())
    archive_html = archive_html.replace("{{footer}}", footer())
    archive_html = archive_html.replace("{{ALL_TAGS}}", all_tags_html)
    archive_html = archive_html.replace("{{identidade_autor}}", identidade_autor())

    save(archive_html, ARCHIVE_PAGE_LINK)
    print("[OK] Página archive.html criada.")


def main():
    posts = load_posts()
    update_posts(posts)
    build_index(posts)
    build_archive(posts)
    build_about_page()
    build_feed(posts)
    print("[✔] Site regenerado com sucesso.")


if __name__ == "__main__":
    main()
from datetime import datetime
from config import *

def open_template(template):
    """Retorna o texto (pre-html) do template indicado."""
    with open(f"scripts/TEMPLATES/{template}_template.html", mode='r', encoding='UTF-8') as f:
        return f.read()


def save(content, path):
    """Salva o content (geralmente HTML) ao arquivo com o path indicado."""
    with open(path, mode='w', encoding='UTF-8') as f:
        f.write(content)


def postagem(title, post_date_yyyy_mm_dd, content, tag_list, path):
    """Gera a página de uma postagem."""
    post_html = open_template('post')

    post_html = post_html.replace("{{POST_TITLE}}", title)
    post_html = post_html.replace("{{SITE_TITLE}}", SITE_TITLE)
    post_html = post_html.replace("{{ABOUT_PAGE_LINK}}", ABOUT_PAGE_LINK)
    post_html = post_html.replace("{{INDEX_PAGE_LINK}}", INDEX_PAGE_LINK)
    post_html = post_html.replace("{{AUTHOR_MAIL}}", AUTHOR_MAIL)
    post_html = post_html.replace("{{AUTHOR_GITHUB}}", AUTHOR_GITHUB)
    post_html = post_html.replace("{{POST_DATE_YYYY_MM_DD}}", post_date_yyyy_mm_dd)
    post_html = post_html.replace("{{POST_DATE_DD_bb_YYY}}", datetime.strptime(post_date_yyyy_mm_dd, "%Y-%m-%d").strftime("%d %b, %Y"))
    post_html = post_html.replace("{{AUTHOR_NAME}}", AUTHOR_NAME)
    post_html = post_html.replace("{{POST_CONTENT}}", content)
    post_html = post_html.replace("{{POST_TAGS}}", tags(tag_list))
    post_html = post_html.replace("{{SITE_URL}}", SITE_URL)
    post_html = post_html.replace("{{POSTS_DIR}}", POSTS_DIR)
    post_html = post_html.replace("{{POST_PATH}}", path)
    # post_html = post_html.replace("{{header}}", header())
    post_html = post_html.replace("{{footer}}", footer())

    save(post_html, POSTS_DIR+path)


def about_page():
    """Gera a página 'Sobre mim' do blog."""
    about_html = open_template('about')

    about_html = about_html.replace("{{AUTHOR_NAME}}", AUTHOR_NAME)
    about_html = about_html.replace("{{RSS_FEED_LINK}}", RSS_FEED_LINK)
    about_html = about_html.replace("{{AUTHOR_MAIL}}", AUTHOR_MAIL)
    about_html = about_html.replace("{{AUTHOR_GITHUB}}", AUTHOR_GITHUB)
    about_html = about_html.replace("{{header}}", header())
    about_html = about_html.replace("{{SITE_URL}}", SITE_URL)
    about_html = about_html.replace("{{footer}}", footer())

    save(about_html, "about.html")


def tags(tag_list):
    """Gera as tags de uma postagem a partir da lista de tags"""
    tags = ""
    for tag in tag_list:
        tags += f"<a href='tags/{tag}' rel='tag'>{tag}</a>\n"
    return tags


def header():
    header = f"""
    <header>
    <h1 class="p-name">{SITE_TITLE}</h1>
    <nav>
        <ul>
            <li><a href="{INDEX_PAGE_LINK}">Início</a></li>
            <li><a href="{ARCHIVE_PAGE_LINK}">Arquivo</a></li>
            <li><a href="{ABOUT_PAGE_LINK}">Sobre mim</a></li>
            <li><a href="{RSS_FEED_LINK}" target="_blank">RSS</a></li>
        </ul>
    </nav>
    <hr />
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
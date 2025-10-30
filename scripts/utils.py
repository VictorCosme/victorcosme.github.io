from config import SITE_TITLE, AUTHOR_MAIL

def get_home_page():
    return "index.html"

def get_about_page():
    return "about.html"

def get_archive_page():
    return "#"

def get_rss_link():
    return "feed.xml"



def generate_header():
    header = f"""
    <header>
        <h1>
            {SITE_TITLE}
        </h1>
        <nav>
            <ul>
                <li><a href="{get_home_page()}">Início</a></li>
                <li><a href="{get_archive_page()}">Arquivo</a></li>
                <li><a href="{get_about_page()}">Sobre mim</a></li>
                <li><a href="https://mail.google.com/mail/?view=cm&fs=1&to={AUTHOR_MAIL}" target="_blank">E-mail</a></li>
                <li><a href="{get_rss_link()}" target="_blank">RSS</a></li>
            </ul>
        </nav>
        <hr/>
    </header>
    """
    return header


def generate_footer():
    footer = f"""
    <footer>
    
    </footer>
    """
    return footer


def generate_style_tag():
    style = """
    <style>
        body { 
            font-family: sans-serif; 
            max-width: 700px; 
            margin: 40px auto; 
            line-height: 1.6; 
            color: #333;
        }
        a { 
            color: #0077cc; 
            text-decoration: none;
        }
        a:hover { 
            text-decoration: underline;
        }
        h1, h2 {
            color: #111;
        }
        nav ul {
            list-style: none;          /* remove os marcadores de lista */
            display: flex;             /* coloca os itens lado a lado */
            justify-content: justify;   
            gap: 20px;                 /* espaço entre os itens */
            padding: 0;                /* remove padding padrão */
            margin: 0;                 /* remove margem padrão */
        }
        nav li {
            display: inline;           /* mantém inline para links */
        }
        footer * {
            align-items: center;
        }
        footer a {
            display: inline-flex;           /* Coloca imagem e texto lado a lado */
            align-items: center;            /* Alinha verticalmente */
            text-decoration: none;          /* Remove o sublinhado */
            color: inherit;                 /* Mantém a cor do texto */
            font-size: 16px;                /* Ajuste conforme o tamanho desejado */
            gap: 8px;                       /* Espaço entre imagem e texto */
        }

        footer a img {
            width: 1em;                     /* Mesmo tamanho da altura do texto */
            height: 1em;                    /* Mantém proporção */
            vertical-align: middle;         /* Centraliza verticalmente */
        }
    </style>
    """
    return style
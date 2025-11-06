def build_index(posts):
    """Cria o index.html listando os posts mais recentes."""
    utils.ensure_output_dir()
    items = "\n".join(
        f"<li><a href='{p['path']}'>{p['title']}</a> <small>({p['date']})</small></li>"
        for p in posts
    )
    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <title>Blog de Victor</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <h1>Blog de Victor</h1>
    <ul>{items}</ul>
</body>
</html>"""
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] index.html atualizado.")

'''
auto generate pages from all .md files held in ./markdown
'''
from pathlib import Path
from dash import register_page, dcc, html
import importlib

# -- Create pages from markdown files
files = Path("posts").glob("*.md")
for file in files:
    filename = file.name[:-3]
    content = file.read_text()
    layout = dcc.Markdown(content)

    register_page(
        module=filename,
        path=f"/posts/{filename.lower()}",
        name=filename.replace("-"," ").replace("_"," "),
        layout=layout,
    )

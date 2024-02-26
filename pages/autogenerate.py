'''
auto generate pages from all .md files held in ./markdown
'''
from pathlib import Path
from dash import register_page, dcc, html

files = Path("markdown").glob("*.md")

for file in files:
    filename = file.name[:-3]
    content = file.read_text()
    layout = dcc.Markdown(content)

    register_page(
        filename,
        layout=layout,
    )


# -- Initial sandbox for an extended page
exlayout = [
    html.Div(
        children=html.H2("Custom Sidebar"),
        className="page-navbar",
    ),
    html.Div(
        children=html.H2("Custom Page"),
        className="page-body",
    ),
]
register_page(
        "testpage",
        layout=exlayout,
    )
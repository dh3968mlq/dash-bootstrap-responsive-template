'''
auto generate pages from all .md files held in ./markdown
'''
from pathlib import Path
from dash import register_page, html
import dash_bootstrap_components as dbc
from dash import dcc

""" files = Path("markdown").glob("*.md")

for file in files:
    filename = file.name[:-3]
    content = file.read_text()
    layout = dcc.Markdown(content)

    register_page(
        filename,
        layout=layout,
    ) """

from page_layouts import home
from src import default_content, utils

playout = utils.create_layout_structure(
    header_contents=default_content.create_header(),
    left_sidebar_contents=default_content.create_left_sidebar(),
    right_sidebar_contents=default_content.create_right_sidebar(),
    body_contents=home.body(),
    footer_contents=default_content.create_footer()
)

register_page("home", path='/', title='Dash Bootstrap Starter Kit', layout=playout)

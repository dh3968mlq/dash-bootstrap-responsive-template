'''
    Dash / Mantine boilerplate for a basic responsive multi-page app
    Author David Harris 2024 
    # -- ... based on https://github.com/snehilvj/dmc-docs, author Snehil Vijay
'''
import sys
sys.path.append('./markdown2dash')

from dash import Dash, page_registry
import gunicorn                         # Necessary for Heroku?
from lib.applayout import get_layout

from lib import callback_close_drawer   # The import defines the callback, no need to reference it
from lib import callback_open_drawer

app = Dash(__name__, use_pages=True)    # A multi-page app: https://dash.plotly.com/urls
app._favicon = "favicon.png"            # app.title must be set page by page
server = app.server                     # Necessary for Heroku?

app.layout = get_layout(page_registry.values())

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8050)  

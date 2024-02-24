'''
Home page
Rendered by calls to dbc components
'''
from dash import register_page, html
import dash_bootstrap_components as dbc
from src.lorem import lorem

def body():
    layout = [
        html.H1('Home page'),
        html.P(
            [
                'A template with boilerplate code for creating a basic website using',
                ' Dash and Dash Bootstrap components. ',
                html.A('Code on Github', href="https://github.com/dh3968mlq/dash-bootstrap-starter-kit", target="_blank")
            ]
        ),
        html.H2('Dash and Bootstrap Components'),
        html.P(
            [
                html.A('Dash', href="https://dash.plotly.com/", target="_blank"),
                ' allows ',
                html.A('multi-page web apps', href="https://dash.plotly.com/urls", target="_blank"),
                ' to be programmed (almost entirely) in Python'
            ]
        ),
        html.P(
            [
                html.A('Dash Bootstrap Components', href="https://dash-bootstrap-components.opensource.faculty.ai/", target="_blank"), 
                ' wraps the ',
                html.A('Bootstrap', href="https://getbootstrap.com/docs/3.4/components/", target="_blank"),
                ' components library'
            ]
        ),
        html.H2('This page'),
        html.P('Is implemented in Python, using dbc components'),
        html.P([
                'See the ',
                html.A('description', href="/description"),
                ' page for more details about the template'
            ]
        ),
        html.Hr(),
        html.H2("Long text to show scrolling"),
    ] + \
    [
        html.P(lorem) for i in range(20)
    ]
    return body
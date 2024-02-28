'''
Home page
Rendered by calls to dbc components
'''
from dash import register_page, html, dcc
import dash_bootstrap_components as dbc
from defaultlayouts.lorem import lorem

register_page(__name__, path='/', title='Dash Bootstrap Starter Kit') # https://dash.plotly.com/urls

layout = [
        dbc.Container(
            [html.H3(
                [
                    'A responsive site template using',
                    ' Dash and Dash Bootstrap Components. ',
                ],
                className="text-center"  # If using html.P... "fs-4 text-center"
            ),
            html.P(
                dbc.Button('Code on Github', href="https://github.com/dh3968mlq/dash-bootstrap-starter-kit",
                    target="_blank", color="primary"),
                className="fs-4 text-center"
            )],
            fluid='lg'
        ),
        html.Img(src="/static/pexels-pixabay-262367-cropped2.jpg",width="100%",
                 className="mx-0 mb-3 rounded"),
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
        html.H3('This page'),
        html.P('Is implemented in Python, using dbc components'),
        html.P([
                'See the ',
                dcc.Link('description', href="/posts/template-description"),
                ' page for more details about the template'
            ]
        ),
        html.H3('Some Stacking Elements'),
        dbc.Row([   # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
            dbc.Col(html.Div(html.H3("Item 1", className="mx-2"), className="bg-primary rounded-2"), lg=4 ),
            dbc.Col(html.Div(html.H3("Item 2", className="mx-2"), className="bg-secondary rounded-2"), lg=4),
            dbc.Col(html.Div(html.H3("Item 3", className="mx-2"), className="bg-info rounded-2"), lg=4),
            ],
            #className="g-5",    # Use this for wider gaps between columns. Put a Div within each Col
        ),
        html.Hr(),
        html.H3("Long text to show scrolling"),
    ] + \
    [
        html.P(lorem) for i in range(20)
    ]

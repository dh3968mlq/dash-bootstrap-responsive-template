'''
Home page
Rendered by calls to dmc components
'''
from dash import register_page
import dash_mantine_components as dmc
from lib.lorem import lorem

register_page(__name__, path='/', title='Dash Mantine Starter Kit') # https://dash.plotly.com/urls

layout = dmc.Container( # One possible container for page content. Set fluid=True to avoid width restrictions
    [
        dmc.Title('Home page', order=1),
        dmc.Text(
            [
                'A template with boilerplate code for creating a basic website using',
                ' Dash and Dash Mantine components. ',
                dmc.Anchor('Code on Github', href="https://github.com/dh3968mlq/dash-mantine-starter-kit", target="_blank")
            ]
        ),
        dmc.Title('Dash and Mantine Components', order=2),
        dmc.Text(
            [
                dmc.Anchor('Dash', href="https://dash.plotly.com/", target="_blank"),
                ' allows ',
                dmc.Anchor('multi-page web apps', href="https://dash.plotly.com/urls", target="_blank"),
                ' to be programmed (almost entirely) in Python'
            ]
        ),
        dmc.Text(
            [
                dmc.Anchor('Dash Mantine Components', href="https://www.dash-mantine-components.com/", target="_blank"), 
                ' wraps the ',
                dmc.Anchor('Mantine', href="https://mantine.dev/", target="_blank"),
                ' React components library'
            ]
        ),
        dmc.Title('This page', order=2),
        dmc.Text('Is implemented in Python, using dmc components'),
        dmc.Text([
                'See the ',
                dmc.Anchor('description', href="/description"),
                ' page for more details about the template'
            ]
        ),
        dmc.Divider(size=3),
        dmc.Title("Long text to show scrolling", order=2),
    ] + 
    [
        dmc.Text(lorem) for i in range(20)
    ],
    fluid=True
)
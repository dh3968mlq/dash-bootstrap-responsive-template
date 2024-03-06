# -- From https://dash.plotly.com/tutorial
from dash import html, dash_table, dcc, callback, Output, Input, register_page, ctx
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

header_height = 50    
footer_height = 30

register_page(module=__name__,
              name="Sample Graph",
              title='Sample Graph')

load_figure_template(["bootstrap", "bootstrap_dark"])

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df["lifeExp"] = df["lifeExp"].round(1)
df["gdpPercap"] = df["gdpPercap"].astype(int)

# App layout
layout = [
    html.Div([
        dbc.Row([
            html.Div('Example Graph', className="text-center fs-3"),
            html.Div([
                "This example, taken from ",
                html.A("https://dash.plotly.com/tutorial", 
                    href="https://dash.plotly.com/tutorial", target="_blank"),
                " shows how controls can be duplicated on a custom pop-up sidebar"
            ])
        ]),
        dbc.Row([
            dbc.RadioItems(options=[{"label": x, "value": x} for x in ['pop', 'lifeExp', 'gdpPercap']],
                        value='lifeExp',
                        inline=True,
                        id='radio-buttons-final', className='bg-info rounded-1 my-2')
        ],),
        dbc.Row(
            [
                dbc.Col([
                    dash_table.DataTable(
                        data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'},
                    )
                    ],
                    md=6,
                    id='col-datatable',
                ),
                dbc.Col([
                    dcc.Graph(figure={}, id='my-first-graph-final')
                    ],
                    id='col-graph',
                    md=6,
                ),
            ],
            className='dbc',
        ), 
    ], className="page-body"),
    # -- The custom pop-up drawer. Duplicates the radio buttons
    dbc.Offcanvas(
        id={"type":"drawer", "page": __name__}, # Needed for the open/close callbacks
        title="Graph Controls",
        children=
        [
            dcc.Link("Home", href="/"),
            dbc.RadioItems(options=[{"label": x, "value": x} for x in ['pop', 'lifeExp', 'gdpPercap']],
                        value='lifeExp',
                        id='radio-buttons-popup',
                        className="bg-info rounded-1 my-3"
            )
        ],
        style={   # Styling .page-navbar in CSS doesn't seem to work to do this...
            "top":f"{header_height}px",
            "bottom":f"{footer_height}px",
        }
    ),
]
# -------------------------------------------------------
# Handle radio buttons. Keep the two duplicates in sync
@callback(
    Output('my-first-graph-final', 'figure'),
    Output('radio-buttons-final', 'value'),
    Output('radio-buttons-popup', 'value'),
    Input('radio-buttons-final', 'value'),
    Input('radio-buttons-popup', 'value'),
    Input("core-lightswitch", "n_clicks"),
)
def update_graph(col_body, col_popup, nclicks):
    trigger = ctx.triggered_id
    col_chosen = col_body if trigger == 'radio-buttons-final' else col_popup
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', 
                       template="bootstrap_dark" if nclicks % 2 else "bootstrap")
    return fig, col_chosen, col_chosen

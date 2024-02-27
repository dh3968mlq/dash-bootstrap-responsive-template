'''
Handle an event in the left sidebar

There is extra complexity because all sidebar HTML content is duplicated, for the fixed drawer and for the pop-up
These two copies have different id prefixes to  avoid id duplication errors
To keep everything consistent both must be handled and both must be updated
'''

from dash import callback, Output, Input, ctx

@callback(    # https://dash.plotly.com/basic-callbacks
    Output("bar-button1-count", "children"),
    Output("drawer-button1-count", "children"),
    Output("bar-button1","n_clicks"),
    Output("drawer-button1","n_clicks"),
    Input("bar-button1","n_clicks"),
    Input("drawer-button1","n_clicks"),
    prevent_initial_call=True,
)
def increment_button1_clicks(nclicks_bar, nclicks_drawer):
    trigger = ctx.triggered_id
    nclicks = nclicks_bar if trigger == "bar-button1" else nclicks_drawer
    text = f"Button has been clicked {nclicks} times"
    return text, text, nclicks, nclicks

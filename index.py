from dash import html
from dash import dcc
from dash.dependencies import Input, Output

from app import app
from pages import introduction, visualization, conclusion

url_content_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div")
])

server = app.server

app.layout = url_content_layout

app.validation_layout = html.Div([
    url_content_layout,
    introduction.layout,
    visualization.layout,
    conclusion.layout,
])

@app.callback(
    Output(component_id="output-div",component_property="children"),
    Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/":
        return introduction.layout
    elif pathname == "/visualization":
        return visualization.layout
    elif pathname == "/conclusion":
        return conclusion.layout

if __name__ == "__main__":
    app.run_server(debug=True)
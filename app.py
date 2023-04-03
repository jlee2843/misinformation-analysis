import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, ctx

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.MINTY, dbc.icons.BOOTSTRAP],
                title="CANIS Hackathon",
                pages_folder="pages",
                suppress_callback_exceptions=True)

# server = app.server
# app.config.suppress_callback_exceptions = True


from dash import html
import dash
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output, State
from pages import introduction
import os

dropdown_menu = dbc.Navbar(
    dbc.Container([dbc.Row([
                        dbc.Col([
                            html.Img(src=dash.get_asset_url('news_icon2.png'), height="25px"),
                            dbc.NavbarBrand("Misinformation in News Analysis", className="ms-2")
                        ],
                        width={"size":"auto"})
                    ],
                    align="center",
                    className="ml-0"),

        dbc.Row([
            dbc.Col([
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Introduction", href="/")),
                    dbc.NavItem(dbc.NavLink("Visualization", href="/visualization")),
                    dbc.NavItem(dbc.NavLink("Conclusion", href="/conclusion")),
                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"),
                                            href="https://github.com/jlee2843/misinformation-analysis",
                                            external_link=True)),
                ], navbar=True)
            ], align="center", className="ml-auto"),

        ]),
    ]),
    color="primary",
    dark=True,
    className="mb-3",
)

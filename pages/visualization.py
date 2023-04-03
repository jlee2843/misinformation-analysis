from dash.dependencies import Input, Output
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from pages.create_visualization import boxplot_fig, radar_fig, nlp_df, word_bar_fig, name_bar, country_bar, scatter_fig, matrix_fig, lgs_fig, svc_fig, model_df, category_df, category_fig_true, category_fig_fake

from app import app
import menu
import dash

model_df_copy = model_df.copy()
model_df_copy = model_df.rename(columns={"True": "Classified True",
                                         "Fake": "Classified Fake",
                                         "News_Type": "News Type"})

dash.register_page(__name__, path="/visualization", title="Visualization")

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Word Count", style={"color": "#78c2ad"}),
            dcc.Graph(id="boxplot_fig", figure=boxplot_fig),
            html.H4("Most Mentioned Words", style={"color": "#78c2ad",
                                         "margin-bottom": "5px"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="word_bar_fig", figure=word_bar_fig),
                ])
            ]),
            html.H4("Most Mentioned Politicians & Countries", style={"color": "#78c2ad"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="name_bar_fig", figure=name_bar),
                ]),
                dbc.Col([
                    dcc.Graph(id="country_bar_fig", figure=country_bar),
                ]),
            ]),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Sentiment Analysis", style={"color": "#78c2ad"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="radar_fig", figure=radar_fig),
                    html.H6("Sentimental Analysis DataFrame", style={"color": "#86c8b5"}),
                    dbc.Table.from_dataframe(nlp_df, striped=False, bordered=False, hover=True)
                ]),
            ]),
            html.H4("Reading Time & Readability Score Analysis", style={"color": "#78c2ad",
                                                                        "margin-top": "15px"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="readability_fig", figure=scatter_fig)
                ]),
            ])
        ]
    ),
    className="mt-3",
)


sample_fig = go.Figure()

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Model Evaluation Performance", style={"color": "#78c2ad"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="matrix_fig", figure=matrix_fig),
                ], style={"margin-left": "15px",
                          "margin-right": "15px"}),
            ]),
            html.H4("Prediction on Russian Propaganda Data", style={"color": "#78c2ad"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="model_performance_fig", figure=sample_fig),
                ], width=9),
                dbc.Col([
                    html.Label("Select Model:", style={"margin-bottom": "5px"}),
                    dcc.Dropdown([{'label': "Logistic Regression", 'value': "Logistic Regression"},
                                  {'label': "Support Vector Machine", 'value': "Support Vector Machine"}],
                                 id="dropdown", value= "Support Vector Machine")
                ], width=3),
                dbc.Row([
                    dbc.Col([
                        html.H6("Model Performance Evaluation DataFrame", style={"color": "#86c8b5"}),
                        dbc.Table.from_dataframe(model_df_copy, striped=False, bordered=False, hover=True)
                    ])
                ])
            ])
        ]
    ),
    className="mt-3",
)

tab4_content = dbc.Card(
    dbc.CardBody(
        [
            html.H4("News Article Categorization", style={"color": "#78c2ad"}),
            dbc.Row([
                dbc.Col([
                    html.H6("Model Performance Evaluation DataFrame", style={"color": "#86c8b5"}),
                    dbc.Table.from_dataframe(category_df, striped=False, bordered=False, hover=True),
                    html.A("News Category Train Data Source", href="https://www.kaggle.com/competitions/learn-ai-bbc/data?select=BBC+News+Train.csv",
                           style={"margin-top":"10px", "margin-bottom": "30px", "color": "#a9a9a"})
                ], style={"margin-right": "15px"}),
            ]),
            html.H4("Support Vector Machine: News Categorization", style={"color": "#78c2ad", "margin-top": "20px"}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="pie_fig", figure=sample_fig),
                ], width=9),
                dbc.Col([
                    html.Label("Select News Type:", style={"margin-bottom": "5px"}),
                    dcc.Dropdown([{'label': "True News", 'value': "True News"},
                                  {'label': "Fake News", 'value': "Fake News"}],
                                 id="dropdown_pie", value= "True News")
                ], width=3),
            ]),
            dbc.Row([
                dbc.Col([
                    html.Label("Analysis", style={"font-weight":"bold", "fontSize": 18, "margin-bottom": "6px"}),
                    html.P("In addition to our questions, we derived a news article training dataset from Kaggle and "
                           "applied built models to the given Fake News and True News datasets. From the pie chart above,"
                           "it is evident that nearly 40% of the news articles labelled as Fake News are categorized "
                           "under 'Business' news category. Also, the proportion of 'Sports' news significantly increases from "
                           "True News to Fake News articles.")
                ])
            ])
        ]
    ),
    className="mt-3",
)

layout = html.Div(children=[
    menu.dropdown_menu,
    html.H1("Visualization", style={"color": "#78c2ad",
                                    "margin-left": "20px",
                                    "margin-bottom": "10px"}),
    dbc.Card([
        dbc.CardHeader(
            dbc.Tabs([
                dbc.Tab(tab1_content, label="Exploration"),
                dbc.Tab(tab2_content, label="NLP Analysis"),
                dbc.Tab(tab3_content, label="Model Evaluation"),
                dbc.Tab(tab4_content, label="News Categorization")
                ])
        ),
    ], className="mt-3",
        style={"margin-left": "20px",
               "margin-right": "20px"})
])

@app.callback(
    Output('model_performance_fig', 'figure'),
    [Input('dropdown', 'value')]
)
def update_output(value):
    if value == "Logistic Regression":
        return lgs_fig
    if value == "Support Vector Machine":
        return svc_fig

@app.callback(
    Output('pie_fig', 'figure'),
    [Input('dropdown_pie', 'value')]
)
def update_output(value):
    if value == "True News":
        return category_fig_true
    if value == "Fake News":
        return category_fig_fake
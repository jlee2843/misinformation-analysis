from dash import html
import dash_bootstrap_components as dbc
import menu
import dash

from pages.texts import participant_text, introductory_text, first_question, second_question, third_question, investigation_text

dash.register_page(__name__, path="/", title="Introduction")

all_questions = [first_question, second_question, third_question]

layout = html.Div(children=[
    menu.dropdown_menu,
    html.H1("Introduction", style={"color": "#78c2ad",
                                   "margin-left": "20px",
                                   "margin-bottom": "10px"}),
    dbc.Row([
       dbc.Col([
           html.Img(src=dash.get_asset_url("misinformation_crop.png"), style={"width":"50%", 'text-align': 'center',
                                                                              "justify-content": "center",
                                                                              "margin-bottom":"25px"},
                    className="align-self-center")
       ], width={"offset":4})
    ]),
    html.P(investigation_text, style={"margin-left": "20px", "margin-bottom": "20px", "margin-right":"20px"}),
    html.P(introductory_text, style={"margin-left": "20px", "margin-bottom": "20px", "margin-right":"20px"}),
    html.Div(
        children=[
            html.Label("Questions To Be Answered:", style={"font-weight":"bold", "margin-left": "20px",
                                                    "margin-bottom":"5px"}),
            html.Ul(id="questions_list", children=[html.Li(q) for q in all_questions],
                    style={"margin-left": "30px", "margin-bottom": "25px", "margin-right":"20px", "fontSize":15})
        ]
    ),

    html.H4("Participant", style={"color": "#78c2ad",
                                   "margin-left": "20px",
                                   "margin-bottom": "10px"}),

    dbc.Row([
        dbc.Col(html.Img(src=dash.get_asset_url('profile_circle.png'),
                         style={"margin-left": "20px",
                                "margin-bottom": "10px",
                                "width": "95%"}
                         ), width=2),
        dbc.Col([html.H6("Jenny Je-Eun Lee", style={"margin-left": "10px", "margin-bottom": "5px",
                                                   "text-align": "left", "font-weight": "bold", "fontSize": 16}),
                 html.Label("B.Sc. Major in Statistics ‧ University of British Columbia",
                        style={"fontSize": 15, "margin-left": "10px"}),
                 html.Br(),
                 html.P(participant_text,
                        style={"fontSize": 15, "margin-left": "10px", "margin-right": "20px", "margin-top": "10px"}),
                 html.A(html.I(className="bi bi-github", style={"margin-left": "10px"}), href="https://github.com/jlee2843"),
                 html.A(html.I(className="bi bi-chat-square-quote-fill", style={"margin-left": "10px"}),
                        href="https://jlee2843.github.io"),
                 ],
                className="ml-0")
    ])

])
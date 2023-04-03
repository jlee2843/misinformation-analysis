from dash import html
import menu
import dash
import dash_bootstrap_components as dbc

from pages.texts import suggestion_text, conclusion_text, first_list_text, second_list_text, third_list_text

dash.register_page(__name__, path="/conclusion", title="Conclusion")

layout = html.Div(children=[
    menu.dropdown_menu,
    dbc.Row([
        dbc.Col([
        html.H1("Conclusion", style={"color": "#78c2ad",
                                 "margin-left": "20px",
                                 "margin-bottom": "5px"}),
        html.P(conclusion_text, style={"margin-top": "10px",
                                           "margin-left": "20px",
                                           "margin-bottom": "10px",
                                           "margin-right":"20px",}),
            html.H6("Q1. Characteristic difference between Fake News and True News:", style={"color": "#86c8b5",
                                                                                             "margin-left": "20px",
                                                                                             "margin-bottom": "8px",
                                                                                            }),
            html.Label(first_list_text, style={"margin-left": "51px", "margin-bottom": "15px",
                                               "fontSize": 15, "margin-right": "20px"}),
            html.H6("Q2. What are the differences in the results of sentimental analysis?:", style={"color": "#86c8b5",
                                                                                             "margin-left": "20px",
                                                                                             "margin-bottom": "8px",
                                                                                             }),
            html.Label(second_list_text, style={"margin-left": "51px", "margin-bottom": "15px",
                                               "fontSize": 15, "margin-right": "20px"}),
            html.H6("Q3. Will the Russian Propaganda articles be classified as Fake News?:", style={"color": "#86c8b5",
                                                                                             "margin-left": "20px",
                                                                                             "margin-bottom": "8px",
                                                                                            }),
            html.Label(third_list_text, style={"margin-left": "51px", "margin-bottom": "15px",
                                               "fontSize": 15, "margin-right": "20px"}),
            html.H4("Future Suggestions", style={"color": "#78c2ad",
                                          "margin-top": "10px",
                                          "margin-left": "20px",
                                          "margin-right":"20px",
                                          "margin-bottom": "10px"}),
            html.P(suggestion_text, style={"margin-top": "10px",
                                           "margin-left": "20px",
                                           "margin-right":"20px",
                                           "margin-bottom": "10px"}),
            html.H4("References", style={"color": "#78c2ad",
                                          "margin-top": "20px",
                                          "margin-left": "20px",
                                          "margin-right":"20px",
                                          "margin-bottom": "10px"}),
            html.Ul([
                html.A(html.Li("Original Data"), href= "https://www.kaggle.com/datasets/stevenpeutz/misinformation-fake-news-text-dataset-79k?resource=download"),
                html.A(html.Li("News Category Data"), href="https://www.kaggle.com/competitions/learn-ai-bbc/data?select=BBC+News+Train.csv"),
                html.A(html.Li("Introduction Page Image"), href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.apa.org%2Fmonitor%2F2022%2F01%2Fcareer-fake-news&psig=AOvVaw02BYh_ABsjDy-o4lxeMj0v&ust=1680565299428000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOj-nN-vjP4CFQAAAAAdAAAAABAJ"),
                html.A(html.Li("Menu Icon Image"), href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fnewspaper_2965879&psig=AOvVaw3b6e19ThywywgKAMeOj7ls&ust=1680565335815000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMCp6_CvjP4CFQAAAAAdAAAAABBA"),
                html.A(html.Li("Conclusion Image"), href="https://unsplash.com/photos/6vs0oFTpoQc")
            ],style={"margin-left": "30px", "margin-bottom": "25px", "margin-right":"15px", "fontSize":15, "color": "#848484"})
        ], width=9),
        dbc.Col([
            html.Img(src=dash.get_asset_url("vertical_image.png"), style={"width":"92%"})
        ], width=3)
    ])

])
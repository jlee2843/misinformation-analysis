import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

true_news = pd.read_csv("analysis/csv/true_sample_nlp.csv")
fake_news = pd.read_csv("analysis/csv/fake_sample_nlp.csv")
true_news["label"] = "True News"
fake_news["label"] = "Fake News"
all_news = pd.concat([true_news, fake_news], axis=0)

boxplot_fig = go.Figure()
boxplot_fig.add_trace(go.Box(x=true_news["count"].tolist(), name="True News", boxmean=True,
                             marker=dict(color="#7294DC",
                                        outliercolor="#B50536",
                                         line=dict(
                                             color='#041D50',
                                             width=1)
                                         )))
boxplot_fig.add_trace(go.Box(x=fake_news["count"].tolist(), name="Fake News", boxmean=True,
                             marker=dict(color="#F49CB5",
                                        outliercolor="#041D50",
                                         line=dict(
                                             color='#B50536',
                                             width=1)
                                         )))
boxplot_fig.update_layout(title={'text': "Character Count Boxplot",
                                 'x':0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                         xaxis_title="Character Count",
                         legend_title="News Type")

boxplot_fig.update_layout(plot_bgcolor="white")
boxplot_fig.update_xaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")
boxplot_fig.update_yaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")

nlp_df = pd.read_csv("analysis/csv/nlp_summary_df.csv")

nlp_melt = pd.melt(nlp_df, id_vars=["News Type"],
                   value_vars=["Negative", "Positive", "Neutral", "Compound", "Subjectivity"],
                   var_name="Type",
                   value_name="Value")
categories = ["Negative", "Positive", "Neutral", "Compound", "Subjectivity"]
fake_melted = nlp_melt[nlp_melt["News Type"] == "Fake News"]
fake_melted_list = fake_melted["Value"].tolist()
true_melted = nlp_melt[nlp_melt["News Type"] == "True News"]
true_melted_list = true_melted["Value"].tolist()

radar_fig = go.Figure()
radar_fig.add_trace(go.Scatterpolar(r=true_melted_list,
                                   theta=categories,
                                   fill="toself",
                                   name="True News"))
radar_fig.add_trace(go.Scatterpolar(r=fake_melted_list,
                                   theta=categories,
                                   fill="toself",
                                   name="Fake News"))
radar_fig.update_layout(title={'text': "Radar Chart on Sentiment Analysis",
                                 'x':0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                         legend_title="News Type",
                        height=650)

fake_20 = pd.read_csv("analysis/csv/fake_top_20_words.csv")
true_20 = pd.read_csv("analysis/csv/true_top_20_words.csv")

word_bar_fig = make_subplots(rows=1, cols=2)

fake_20 = fake_20.sort_values(by="Frequency", ascending=True)
true_20 = true_20.sort_values(by="Frequency", ascending=True)

word_bar_fig.add_trace(
    go.Bar(y=true_20["Word"].tolist(),
          x=true_20["Frequency"].tolist(),
          name="True News", orientation="h",
          marker=dict(
               color='#7294DC',
               line=dict(
                   color='#041D50',
                   width=1),
          )),
    row=1, col=2
)

word_bar_fig.add_trace(
    go.Bar(y=fake_20["Word"].tolist(),
          x=fake_20["Frequency"].tolist(),
          name="Fake News", orientation="h",
           marker=dict(
               color='#F49CB5',
               line=dict(
                   color='#B50536',
                   width=1),
    )),
    row=1, col=1
)

word_bar_fig.update_layout(height=650,
                          title={'text': "Top 20 Most Mentioned Words",
                                 'x':0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                         legend_title="News Type")

word_bar_fig.update_layout(plot_bgcolor="white")
word_bar_fig.update_xaxes(showline=False, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")
word_bar_fig.update_yaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")

human_df = pd.read_csv("analysis/csv/human_names_df.csv")

name_bar = go.Figure()

name_bar.add_trace(go.Bar(
    y=human_df["Word"].tolist(),
    x=human_df["Count_Fake"].tolist(),
    name="Fake News",
    orientation="h",
    marker=dict(
        color='#F49CB5',
        line=dict(
            color='#B50536',
            width=2))
))

name_bar.add_trace(go.Bar(
    y=human_df["Word"].tolist(),
    x=human_df["Count_True"].tolist(),
    name="True News",
    orientation="h",
    marker=dict(
        color='#7294DC',
        line=dict(
            color='#041D50',
            width=2))
))

annotations = []
y_data = human_df["Word"].tolist()
x_data = list(zip(human_df.Count_Fake, human_df.Count_True))
new_x_data = []
for item in x_data:
    whole_number = item[0] + item[1]
    first_number = (item[0] / whole_number) * 100
    second_number = (item[1] / whole_number) * 100
    new_x_data.append([round(first_number), round(second_number)])

x_tract_0 = 0
x_tract_1 = 0

for yd, xd in zip(y_data, x_data):
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(new_x_data[x_tract_0][0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    x_tract_0 += 1

    space = xd[0]
    for i in range(1, len(xd)):
        annotations.append(dict(xref='x', yref='y',
                                x=space + (xd[i] / 2), y=yd,
                                text=str(new_x_data[x_tract_1][1]) + '%',
                                font=dict(family='Arial', size=14,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        x_tract_1 += 1
        space += xd[i]

name_bar.update_layout(barmode='stack', annotations=annotations)
name_bar.update_layout(height=500,
                       title={'text': "Politician Mentions Comparison",
                              'x': 0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
                       legend_title="News Type:",
                       xaxis_title="Frequency Mentioned",
                       legend=dict(x=0.8, y=1.1, traceorder="normal",
                                   orientation="h",
                                   xanchor="right"))

name_bar.update_layout(plot_bgcolor="white")
name_bar.update_xaxes(showline=False, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")
name_bar.update_yaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")

countries_df = pd.read_csv("analysis/csv/countries_df.csv")

country_bar = go.Figure()

country_bar.add_trace(go.Bar(
    y=countries_df["Word"].tolist(),
    x=countries_df["Count_Fake"].tolist(),
    name="Fake News",
    orientation="h",
    marker=dict(
        color='#F49CB5',
        line=dict(
            color='#B50536',
            width=2))
))

country_bar.add_trace(go.Bar(
    y=countries_df["Word"].tolist(),
    x=countries_df["Count_True"].tolist(),
    name="True News",
    orientation="h",
    marker=dict(
        color='#7294DC',
        line=dict(
            color='#041D50',
            width=2))
))

annotations = []
y_data = countries_df["Word"].tolist()
x_data = list(zip(countries_df.Count_Fake, countries_df.Count_True))
new_x_data = []
for item in x_data:
    whole_number = item[0] + item[1]
    first_number = (item[0] / whole_number) * 100
    second_number = (item[1] / whole_number) * 100
    new_x_data.append([round(first_number), round(second_number)])

x_tract_0 = 0
x_tract_1 = 0

for yd, xd in zip(y_data, x_data):
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(new_x_data[x_tract_0][0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    x_tract_0 += 1

    space = xd[0]
    for i in range(1, len(xd)):
        annotations.append(dict(xref='x', yref='y',
                                x=space + (xd[i] / 2), y=yd,
                                text=str(new_x_data[x_tract_1][1]) + '%',
                                font=dict(family='Arial', size=14,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        x_tract_1 += 1
        space += xd[i]

country_bar.update_layout(barmode='stack', annotations=annotations)
country_bar.update_layout(height=500,
                          title={'text': "Country Mentions Comparison",
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                          legend_title="News Type:",
                          xaxis_title="Frequency Mentioned",
                          legend=dict(x=0.8, y=1.1, traceorder="normal",
                                      orientation="h",
                                      xanchor="right"))

country_bar.update_layout(plot_bgcolor="white")
country_bar.update_xaxes(showline=False, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")
country_bar.update_yaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")

all_news = all_news[(all_news["readability_score"] < all_news["readability_score"].quantile(0.95)) &
                    (all_news["readability_score"] > all_news["readability_score"].quantile(0.05))]

scatter_fig = px.scatter(all_news, x="reading_time", y="readability_score", color="label", size="count",
                         title="Reading Time & Readability")
scatter_fig.update_xaxes(title=dict(text="Reading Time (Seconds)"))
scatter_fig.update_yaxes(title=dict(text="Dale-Chall Readability Score"))
scatter_fig.update_layout(title={'x':0.5})

scatter_fig.update_layout(plot_bgcolor="white")
scatter_fig.update_xaxes(showline=False, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")
scatter_fig.update_yaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")

lgs_matrix = [[0.47323529, 0.02727941], [0.02676471, 0.47272059]]
svc_matrix = [[0.47933824, 0.02338235], [0.02066176, 0.47661765]]

matrix_fig = make_subplots(rows=1, cols=2,
                          subplot_titles=["Logistic Regression", "Support Vector Machine"])
matrix_fig.add_trace(go.Heatmap(z=lgs_matrix,
                               x=["True", "Fake"],
                               y=["True", "Fake"],
                               hoverongaps=False,
                               texttemplate="%{z}",
                               coloraxis = "coloraxis",
                               name="Logistic Regression"), row=1, col=1)
matrix_fig.add_trace(go.Heatmap(z=svc_matrix,
                               x=["True", "Fake"],
                               y=["True", "Fake"],
                               hoverongaps=False,
                               texttemplate="%{z}",
                               coloraxis = "coloraxis",
                               name="Support Vector Machine"), row=1, col=2)
matrix_fig.update_layout(title={'text': "Confusion Matrix Evaluation Model Performance",
                              'x': 0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
                         showlegend=False,
                         coloraxis = {'colorscale':'blues'}, hoverlabel_namelength=-1)
matrix_fig.update_yaxes(showticklabels=False, row=1, col=2)

model_df = pd.read_csv("analysis/csv/model_df.csv")
news_types = model_df["News_Type"].unique().tolist()
lgs_df = model_df[model_df["Model"] == "Logistic Regression"]
svc_df = model_df[model_df["Model"] == "Support Vector Machine"]

lgs_fig = go.Figure(data=[
    go.Bar(name='Classified Fake', x=news_types, y=lgs_df["Fake"].tolist(), marker=dict(color='#F49CB5',
                                                                                        line=dict(color='#B50536',
                                                                                                  width=2))),
    go.Bar(name='Classified True', x=news_types, y=lgs_df["True"].tolist(), marker=dict(color='#7294DC',
                                                                                        line=dict(color='#041D50',
                                                                                                  width=2))),
])

lgs_fig.update_layout(barmode='group', hoverlabel_namelength=-1)
lgs_fig.update_layout(height=500,
                          title={'text': "Country Mentions Comparison",
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                          legend_title="News Type:",
                          xaxis_title="Type of News Article")

lgs_fig.update_layout(plot_bgcolor="white")
lgs_fig.update_xaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")
lgs_fig.update_yaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")

svc_fig = go.Figure(data=[
    go.Bar(name='Classified Fake', x=news_types, y=svc_df["Fake"].tolist(), marker=dict(color='#F49CB5',
                                                                                        line=dict(color='#B50536',
                                                                                                  width=2))),
    go.Bar(name='Classified True', x=news_types, y=svc_df["True"].tolist(), marker=dict(color='#7294DC',
                                                                                        line=dict(color='#041D50',
                                                                                                  width=2))),
])

svc_fig.update_layout(barmode='group', hoverlabel_namelength=-1)
svc_fig.update_layout(height=500,
                          title={'text': "Country Mentions Comparison",
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                          legend_title="News Type:",
                          xaxis_title="Type of News Article")

svc_fig.update_layout(plot_bgcolor="white")
svc_fig.update_xaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")
svc_fig.update_yaxes(showline=True, linecolor="#848484", showgrid=True, linewidth=1.2, gridcolor="#F3F3F3")

category_df = pd.read_csv("analysis/csv/category_df.csv")
category_select = category_df[category_df["Model"] == "Logistic Regression"]
category_melt = pd.melt(category_select, id_vars=["News Type"],
                        value_vars=["Business", "Entertainment", "Politics", "Sport", "Tech"],
                        var_name="Category",
                        value_name="Count")

color_map = {"Business": "lightcyan", "Politics": "cyan", "Entertainment": "royalblue", "Sports": "navy", "Tech": "darkblue"}
color_try = ["darkblue", "blue", "cyan", "lightcyan", "navy"]

category_fig_fake = px.pie(category_melt[category_melt["News Type"] == "Fake"], values="Count",
                           names="Category", hole=0.4, color=color_try)
category_fig_true = px.pie(category_melt[category_melt["News Type"] == "True"], values="Count",
                           names="Category", hole=0.4, color=color_try)
category_fig_true.update_layout(height=500,
                          title={'text': "Percentage Distribution Across True News Category",
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                          legend_title="News Category:")
category_fig_fake.update_layout(height=500,
                          title={'text': "Percentage Distribution Across Fake News Category",
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                          legend_title="News Category:")

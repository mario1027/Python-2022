from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objects  as go

app=Dash(__name__)

datos1=px.data.gapminder()
datos3d=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
fig=px.scatter(datos1,
                x="gdpPercap", 
                y="lifeExp", 
                animation_frame="year", 
                animation_group="country",
                size="pop",
                color="continent",
                facet_col="continent",
                log_x=True,
                size_max=60,
                range_y=[20,100])
fig3d=go.Figure(data=go.Surface(z=datos3d.values))
app.layout = html.Div([
    html.Center(html.H1(children="Plot Animated")),
    dcc.Graph(id="lifeExp", figure=fig),
    html.Center(html.H1(children="Plot 3D")),
    dcc.Graph(id="plot3d", figure=fig3d)
    ])       

if __name__=="__main__":
    app.run_server(debug=True)
import pandas as pd
import plotly.express as px
import dash 
from dash import dcc
from dash import html

airline_data_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'
default_encoding = "ISO-8859-1"

airline_data = pd.read_csv(
    airline_data_path,
    encoding=default_encoding,
    dtype={
        'Div1Airport':str,
        'Div2Airport':str,
        'Div3Airport':str,
        'Div4Airport':str,
    }
)

data = airline_data.sample(n=500, random_state=42)

fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance Group Proportions by flights')


app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1('Airline Dashboard'),
    html.P('A Pie chary Showing the Distance group proportions by flights'),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    app.run_server()

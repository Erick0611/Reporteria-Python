# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 16:20:40 2025

@author: Erick
"""

# ==============================================
# IMPORTAR LIBRERIAS
# ==============================================

import dash
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from jupyter_dash import JupyterDash
app = dash.Dash() #Incicialización del App

# ==============================================
# CARGA DATOS
# ==============================================

df = pd.read_excel("VentasEC.xlsx", sheet_name="ventas")

# ==============================================
# CREACIÓN DE LA PLANTILLA
# ==============================================

app.layout = html.Div(
    id = "parent", children = [
        html.H1(id = "H1", children = "Total de Ventas y Exportaciones", style = {"textAl ign":"center", \
                                                                                  "marginTop":40,"marginBottom":40}),
            #Creacion del combo desplegable por Provincia
            dcc.Dropdown( id = "dropdown",
            options = [
                {"label": "Azuay", "value":"AZUAY"},
                {"label": "Bolivar", "value":"BOLIVAR"},
                {"label": "Carchi", "value":"CARCHI"},
                {"label": "Cañar", "value":"CAÑAR"},
                {"label": "Chimborazo", "value":"CHIMBORAZO"},
                {"label": "Cotopaxi", "value":"COTOPAXI"},
                {"label": "El Oro", "value":"EL ORO"},
                {"label": "Esmeraldas", "value":"ESMERALDAS"},
                {"label": "Galapagos", "value":"GALAPAGOS"},
                {"label": "Imbabura", "value":"IMBABURA"},
                {"label": "Loja", "value":"LOJA"},
                {"label": "Los Rios", "value":"LOS RIOS"},
                {"label": "Manabí", "value":"MANABÍ"},
                {"label": "Morona Santiago", "value":"MORONA SANTIAGO"},
                {"label": "Napo", "value":"NAPO"},
                {"label": "ND", "value":"ND"},
                {"label": "Orellana", "value":"ORELLANA"},
                {"label": "Pastaza", "value":"PASTAZA"},
                {"label": "Pichincha", "value":"PICHINCHA"},
                {"label": "Sta. Elena", "value":"SANTA ELENA"},
                {"label": "Sto. Domingo de los Tsáchilas", "value":"SANTO DOMINGO"},
                {"label": "Sucumbios", "value":"SUCUMBIOS"},
                {"label": "Tungurahua", "value":"TUNGURAGUA"},
                {"label": "Zamora Chinchipe", "value":"ZAMORA CHINCHIPE"},
                ],
            value = "PICHINCHA", #VALOR QUE APARECE POR DEFECTO
            ),
            dcc.Graph(id = "bar_plot")
                ])
 # ==============================================
 # LLAMADA DEL GRÁFICO PARA SER ACTUALIZADO
 # ==============================================
@app.callback(Output(component_id="bar_plot", component_property= "figure"),
              [Input(component_id="dropdown", component_property= "value")])      
def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x = df["Fecha"], y = df["{}".format(dropdown_value)],\
                    line = dict(color = "firebrick", width = 4)
                    )
                     ])
    fig.update_layout(title = "Fuente Saiku SRI - Formulario 104",
                      xaxis_title = "Fechas",
                      yaxis_title = "Ventas y Exportaciones en USD"
                      )
    return fig
    

 # ==============================================
 # EJECUCIÓN DEL SERVIDOR
 # ==============================================

if __name__ == "__main__":
    app.run(debug=True)
    

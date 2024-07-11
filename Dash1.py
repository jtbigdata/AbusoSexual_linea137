# Dash1.py


from dash import Dash, dcc, html, Input, Output, callback  # Importar Input, Output y callback desde dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.io as pio
import functions
import plotly.express as px
import plotly.graph_objects as go


# Cargar el dataset
df = pd.read_csv('data/datos2.csv')
#print(df.VicGen.unique())

# Crear la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN, '/assets/style.css'])


# Configurar el tema personalizado
custom_template = {
    "layout": {
        "font": {"family": "Arial", "size": 16, "color": "#000000"},  # Color del texto en los gráficos
        "plot_bgcolor": "#FFFFFF",  # Cambiar el color de fondo de los gráficos a blanco
        "paper_bgcolor": "#FFFFFF",  # Cambiar el color de fondo del papel a blanco
    }
}

# Asignar el tema personalizado como el tema predeterminado
pio.templates["custom"] = custom_template
pio.templates.default = "custom"

# Definir el layout del dashboard custom-text-color
header = html.H4(
    "Abuso Sexual en Argentina",
    className="bg-custom-header p-2 mb-2 text-center",  # Utilizamos las nuevas clases de estilo
)

#inputs tab1
input1=functions.Lista1
input2=functions.Lista2
dic1=functions.Diccionario2
input3=list(dic1.keys())

#inputs tab2
input4=functions.Lista4
Lista3=functions.Lista3
dic3=functions.Diccionario3
input5=list(dic3.keys())

#inputs tab3
input6=functions.Lista5
input7=functions.Lista6

control1 =html.Div([
        dbc.Label("Tab1", className="label"),
        dcc.Dropdown(input1, input1[0],
                     clearable=False, className="dropdown custom-font",
                     id="in1",),
    ], className="mb-4 custom-plot-bg")


control1b=html.Div([
        dbc.Label("Tab1-Tab2", className="label"),
        dcc.Dropdown(input2, input2[0],
                     clearable=False, className="dropdown custom-font",
                     id="in1b",),
    ], className="mb-4 custom-plot-bg")

control1c=html.Div([
        dbc.Label("Tab1-Tab2", className="label"),
        dcc.Dropdown(input3,input3[0],
                     clearable=False, className="dropdown custom-font",
                     id="in1c",),
    ], className="mb-4 custom-plot-bg")

control2 =html.Div([
        dbc.Label("Tab1-Tab2", className="label"),
        dcc.Dropdown(input4, input4[0],
                     clearable=False, className="dropdown custom-font",
                     id="in2",),
    ], className="mb-4 custom-plot-bg")

control2b =html.Div([
        dbc.Label("Tab2", className="label"),
        dcc.Dropdown(input5, input5[0],
                     clearable=False, className="dropdown custom-font",
                     id="in2b",),
    ], className="mb-4 custom-plot-bg")

#control3=html.Div([
#        dbc.Label("Tab3", className="label"),
#        dcc.Dropdown(input6, input6[0],
#                     clearable=False, className="dropdown custom-font",
#                     id="in3",),
#    ], className="mb-4 custom-plot-bg")

#control3b=html.Div([
#        dbc.Label("Tab3", className="label"),
#        dcc.Dropdown(input7, input7[0],
#                     clearable=False, className="dropdown custom-font",
#                     id="in3b",),
#    ], className="mb-4 custom-plot-bg")

control = dbc.Col([control1,control1b,control1c,control2,control2b,#control3,control3b
                   ], width=2)


grafico1a=dbc.Col([dcc.Graph(id="out1", figure=px.pie()),
                   dcc.Graph(id='out1d',figure=px.line_polar())
                  ] ,width=6
                 )

grafico1b=dbc.Col([ dcc.Graph(id="out1b", figure=px.line()),
                  dcc.Graph(id="out1c", figure=px.line())
                  ] ,width=6
                 )
tab1 = dbc.Tab([dbc.Row([grafico1a,grafico1b])],style={'height': '550px'},label="Tab1")


grafico2a=dbc.Col([dcc.Graph(id="out2", figure=px.bar()),
                   dcc.Graph(id="out2c", figure=px.line())
                  ] ,width=6
                 )

grafico2b=dbc.Col([dcc.Graph(id='out2d',figure=px.line_polar()),
                   dcc.Graph(id='out2b',figure=px.density_heatmap())
                  ] ,width=6
                 )

tab2 = dbc.Tab([dbc.Row([grafico2a,grafico2b])], style={'height': '550px'}, label="Tab2")

#grafico3a=dbc.Col(['Tab3',#dcc.Graph(id="out2", figure=px.bar()),
                   #dcc.Graph(id="out2c", figure=px.line())] ,width=6)

#tab3= dbc.Tab([dbc.Row([grafico3a])], style={'height': '550px'}, label="Tab3")

tabs = dbc.Col(dbc.Card(dbc.Tabs([tab1,tab2])), width=10)

app.layout = dbc.Container([header, dbc.Row([control, tabs])],
                           fluid=True, className="dbc dbc-ag-grid custom-layout")


@callback([Output("out1", "figure"),Output("out1b", "figure"),Output("out1c", "figure"),Output("out1d", "figure") ], 
          [Input("in1", "value"),Input("in1b", "value"),Input("in1c", "value")])

def update(in1, in1b, in1c):
    global df
    inputdf = df
    inputi = in1
    inputii = in1b
    inputiii = in1c

    # Define un mapeo de colores para asegurar consistencia
    color_map = {
        value: px.colors.qualitative.Dark24[i % len(px.colors.qualitative.Dark24)]
        for i, value in enumerate(inputdf[inputi].unique())
    }

    # Gráfico figa (Pie chart)
    a = functions.F1(inputdf, inputi)

    if inputi=='VicNacion':
        a = a[~a['VicNacion'].isin(Lista3)]
    # Definir el gráfico de pastel con Plotly
    figa = px.pie(a, values='porcentaje', names=inputi, color=inputi, color_discrete_map=color_map)
    
    # Actualiza el layout del gráfico con el título y sus propiedades
    figa.update_layout(title={
        'text': f"Porcentaje de {inputi}",  # Especifica el título del gráfico
        'y':0.90,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color':'red'  # Color de la fuente
        }
    }
)   
    figa.update_traces(textinfo='value',#textinfo='label+value',
                      hoverinfo='text', #hoverinfo='label+text', 
                      text=a['porcentaje'].astype(str) + '%',
                       insidetextorientation='radial')
    
    figa.update_layout(height=275)

 
    # Obtener el DataFrame b con el orden específico
    b = functions.F2(inputdf, inputii, inputi)
    if inputii=='GrupoEdad':
        orden1=functions.ord1
        b[inputii] = pd.Categorical(b[inputii], categories=orden1, ordered=True)
        b = b.sort_values(inputii)
    if inputii=='Año':
        orden2=functions.ord2
        b[inputii] = pd.Categorical(b[inputii], categories=orden2, ordered=True)
        b = b.sort_values(inputii)
   
    if inputi=='VicNacion':
        b = b[~b['VicNacion'].isin(Lista3)]
    figb = px.line(b, x=inputii, y='porcentaje', color=inputi, markers=True, color_discrete_map=color_map)

    figb.update_layout(title={
        'text': f"Porcentaje vs {inputii}",  # Especifica el título del gráfico
        'y':0.95,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'red'  # Color de la fuente
        }
    }
)   
    figb.update_layout(
    xaxis_title={
        'text': "",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    },
    yaxis_title={
        'text': "%",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    }
)

    figb.update_layout(height=275)

    # Gráfico figc (Area chart)
    #print('uno',inputii, inputi)
    c1 = functions.F3(inputdf, inputii, inputi)
    c2 = functions.F1(inputdf, inputii)
    c3 = c1.merge(c2, on=inputii, how='right')
    c3['Delta'] = c3[f'{inputi}(%)'] - c3['porcentaje']
    #p
    ci=functions.F5(c3,inputii, inputi,0)
    if inputii=='GrupoEdad':
        orden1=functions.ord1
        ci[inputii] = pd.Categorical(ci[inputii], categories=orden1, ordered=True)
        ci = ci.sort_values(inputii)
    if inputii=='Año':
        orden2=functions.ord2
        ci[inputii] = pd.Categorical(ci[inputii], categories=orden2, ordered=True)
        ci = ci.sort_values(inputii)
    
    if inputi=='VicNacion':
        ci = ci[~ci['VicNacion'].isin(Lista3)]

    #print('Area',ci.columns)
    figc = px.area(ci, x=inputii, y="Delta",color=inputi, color_discrete_map=color_map #color_discrete_sequence=[color_fixed]
                   )
    figc.update_layout(title={
        'text': f"Delta vs {inputii}",  # Especifica el título del gráfico
        'y':0.90,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'red'  # Color de la fuente
        }
    }
)

    # Fija los nombres de los ejes X y Y
    figc.update_layout(
    xaxis_title={
        'text': "",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    },
    yaxis_title={
        'text': "%",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    }
)
    figc.update_layout(height=275)

    # Gráfico figd (Polar line chart)

    d = functions.F4(df, inputiii, inputi, dic1)
    d = d.sort_values(by='Porcentaje_SI', ascending=False)
   
    

    r_min = d['Porcentaje_SI'].min()
    r_max = d['Porcentaje_SI'].max()
    
    #ordenpolar=d.inputiii.unique()
    #print(ordenpolar,ordenpolar)
    ordenpolar=d['Columna'].unique()
    d['Columna'] = pd.Categorical(d['Columna'], categories=ordenpolar, ordered=True)
    d = d.sort_values('Columna')
    
    if inputi=='VicNacion':
        d = d[~d['VicNacion'].isin(Lista3)]
    figd = px.line_polar(d, r=d['Porcentaje_SI'], theta=d['Columna'], color=inputi, line_close=True, color_discrete_map=color_map,
                          #r_labels={'show': True, 'values': [r_min, r_max]}
                          )
    
    # Actualizar las etiquetas del eje r para mostrar solo los valores mínimo y máximo
    figd.update_layout(
    polar=dict(
        radialaxis=dict(
            tickmode='array',
            tickvals=[r_min, r_max],
            #tickvals=[r_min, r_max],
            ticktext=[r_min, r_max]
        )
    )
)   
    figd.update_layout(title={
        'text': f"Radar de {inputi}",  # Especifica el título del gráfico
        'y':0.90,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'red'  # Color de la fuente
        }
    }
)
    figd.update_layout(height=275)

    return figa, figb, figc, figd



@callback([Output("out2", "figure"),Output("out2b", "figure"),Output("out2c", "figure"),Output("out2d", "figure") ], 
          [Input("in2", "value"),Input("in2b", "value"),Input("in1", "value"),Input("in1b", "value"),Input("in1c", "value")])

def update(in2,in2b,in1,in1b,in1c):
    global df
    
    input_df=df
    Lista4=functions.Lista4

    

    color_map = {
        value: px.colors.qualitative.Dark24[i % len(px.colors.qualitative.Dark24)]
        for i, value in enumerate(input_df[in2].unique())
    }

    a=functions.F1(input_df, in2)
    a = a.sort_values(by='porcentaje', ascending=False)
    fig = px.bar(a, x=in2, y="porcentaje", color=in2,color_discrete_map=color_map)
    fig.update_layout(height=275)

    fig.update_layout(title={
        'text': f"Porcentaje vs {in2}",  # Especifica el título del gráfico
        'y':0.90,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'red'  # Color de la fuente
        }
    }
)
    
    fig.update_layout(
    xaxis_title={
        'text': "",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    },
    yaxis_title={
        'text': "%",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    }
)
 
    #================================================================

    d = functions.F4(input_df, in1c, in2,dic1)
    d = d.sort_values(by='Porcentaje_SI', ascending=False)

    r_min = d['Porcentaje_SI'].min()
    r_max = d['Porcentaje_SI'].max()

    ordenpolar=d['Columna'].unique()
    d['Columna'] = pd.Categorical(d['Columna'], categories=ordenpolar, ordered=True)
    d = d.sort_values('Columna')

    figd = px.line_polar(d, r='Porcentaje_SI', theta='Columna', color=in2,color_discrete_map=color_map, line_close=True)
    figd.update_layout(
    polar=dict(
        radialaxis=dict(
            tickmode='array',
            tickvals=[r_min, r_max],
            #tickvals=[r_min, r_max],
            ticktext=[r_min, r_max]
        )
    )
)
    figd.update_layout(title={
        'text': f"Radar de {in2}",  # Especifica el título del gráfico
        'y':0.90,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'red'  # Color de la fuente
        }
    }
)
    figd.update_layout(height=275)



    # Color map for VincAgr1
    color_map2 = {
    value: px.colors.qualitative.Pastel[i % len(px.colors.qualitative.Pastel)]
    for i, value in enumerate(input_df['VincAgr1'].unique())
}
    c1 = functions.F3(input_df, in1b,Lista4[1])
    c2 = functions.F1(input_df, in1b)    
    c3 = c1.merge(c2, on=in1b, how='right')
    c3['Delta'] = c3[f'{Lista4[1]}(%)'] - c3['porcentaje']
    c3 = c3[c3[Lista4[1]].isin(dic3[in2b])]

    ci=c3
    if in1b=='GrupoEdad':
        orden1=functions.ord1
        ci[in1b] = pd.Categorical(ci[in1b], categories=orden1, ordered=True)
        ci = ci.sort_values(in1b)
    if in1b=='Año':
        orden2=functions.ord2
        ci[in1b] = pd.Categorical(ci[in1b], categories=orden2, ordered=True)
        ci = ci.sort_values(in1b)
  
   # ci = ci[ci[Lista4[1]].isin(dic3[in2b])]
    #print('ci',ci.columns)
    
    figc = px.area(ci, x=in1b, y="Delta",color='VincAgr1',color_discrete_map=color_map2
                   )
    figc.update_layout(height=275)

    figc.update_layout(title={
        'text': f"Porcentaje vs {in1b}",  # Especifica el título del gráfico
        'y':0.90,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'red'  # Color de la fuente
        }
    }
)
    
    figc.update_layout(
    xaxis_title={
        'text': "",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    },
    yaxis_title={
        'text': "%",
        'font': {
            'size': 18,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'black'  # Color de la fuente
        }
    }
)

    #=====================================
    


    b= functions.F4(input_df, in1c,Lista4[1],dic1)

    b= b.sort_values(by='Porcentaje_SI', ascending=False)
    b = b[b[Lista4[1]].isin(dic3[in2b])]
    #print(b.head(2))
    r_min = b['Porcentaje_SI'].min()
    r_max = b['Porcentaje_SI'].max()

    ordenpolar=b['Columna'].unique()
    #print(ordenpolar)
    b['Columna'] = pd.Categorical(b['Columna'], categories=ordenpolar, ordered=True)
    b = b.sort_values('Columna')
    print('b-->',b.VincAgr1.unique())

    figb = px.line_polar(b, r='Porcentaje_SI', theta='Columna', color='VincAgr1',color_discrete_map=color_map2,line_close=True)
    figb.update_layout(
    polar=dict(
        radialaxis=dict(
            tickmode='array',
            tickvals=[r_min, r_max],
            #tickvals=[r_min, r_max],
            ticktext=[r_min, r_max]
        )
    )
)
    figb.update_layout(title={
        'text': f"Radar de {Lista4[1]}",  # Especifica el título del gráfico
        'y':0.90,  # Ubicación vertical del título (0.0 - abajo, 1.0 - arriba)
        'x':0.5,  # Ubicación horizontal del título (0.0 - izquierda, 1.0 - derecha)
        'xanchor': 'center',  # Alineación horizontal del título
        'yanchor': 'middle',  # Alineación vertical del título
        'font': {'size': 20,  # Tamaño de la fuente
            'family': 'Arial, sans-serif',  # Tipo de fuente
            'color': 'red'  # Color de la fuente
        }
    }
)
    figb.update_layout(height=275)




    return [fig,figb,figc,figd]

#@callback([Output("out3", "figure"),], 
#          [Input("in3", "value"),
#           Input("in3b", "value"),])


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050)


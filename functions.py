import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


#Listas 

Lista1=['VicConvAgresor', 'VicNacion', 'VicGen','VicDisc']

Lista2=['GrupoEdad','Año', 'Mes', 'Dia']

Lista3=['Haitiana','Mexicana','Corea del Sur','Dominicana','Japonesa','Estadounidense','Otra','NS/NC','Brasileña',
        'Uruguaya','Colombiana','Venezolana','Chilena']

Lista4=['VincAgre0', 'VincAgr1']

Lista4a=[ 'Padrastro', 'Padre', 'Otro familiar','Tío'  ,'Hermano/a', 'Abuelo/a', 'Madre','Madrastra']
Lista4b=['Ex pareja', 'Pareja']
Lista4c=['Conocido no familiar', 'Desconocido' ,'Sin datos']
Diccionario3={'Familiar':Lista4a,
              'Conyugal':Lista4b,
              'NoFamiliar':Lista4c}



ViolSex=['VsViaVaginal', 'VsViaAnal', 'VsViaOral', 'VsTentaViolacion',
       'VsTocSexual', 'VsIntentTocamiento', 'VsIntentVTerceraPersona',
       'VsGrooming', 'VsExhibicionismo', 'VsAmezsVrblsCntSexual',
       'VsExplotSex', 'VsExplotSexComercial', 'VsExplotSexTurismo',
       'VsSospechaTPers', 'VsExistFacilitadorNNYA',
       'VsObligFotosPornograficas', 'VsEyaculacionCuerpo', 'VsAcosoSex',
       'VsIniciacionSexForzada', 'VsOtraFormaVSex', 'VsNSN']

ViolSexa=['VsTocSexual','VsViaVaginal','VsViaAnal', 'VsViaOral','VsNSN']

ViolSexb=['VsOtraFormaVSex','VsIntentTocamiento','VsTentaViolacion','VsIniciacionSexForzada']

ViolSexc=['VsExhibicionismo','VsAcosoSex','VsAmezsVrblsCntSexual','VsGrooming''VsObligFotosPornograficas','VsEyaculacionCuerpo']

ViolSexc=['VsIntentVTerceraPersona','VsExplotSexComercial','VsSospechaTPers','VsExplotSex','VsExistFacilitadorNNYA','VsExplotSexTurismo']

#ViolSexd=['VsEyaculacionCuerpo','VsExplotSexTurismo']


OtraViol=['OfvSentAmnz',
       'OfvAmnzExplicit', 'OfvVFisica', 'OfvIntentAhorcar', 'OfvIntentQuemar',
       'OfvIntentAhogar', 'OfvAmnzMuerte', 'OfvUsoSust',
       'OfvIntentPrivacionLibrtd', 'OfvPrivacionLibrtd', 'OfvUsoArmaBnc',
       'OfvUsoArmaFueg', 'OfvEnganioSeduccion', 'OfvIntentMatar',
       'OfvUsoAnimalVictimizar', 'OfvGrooming', 'OfvOtraForma', 'OfvNSNC']

OtraViola=['OfvSentAmnz','OfvAmnzExplicit',  'OfvAmnzMuerte','OfvEnganioSeduccion','OfvNSNC'
           ]

OtraViolb=['OfvUsoSust','OfvUsoArmaBnc','OfvUsoArmaFueg','OfvVFisica','OfvOtraForma']          

OtraViolc=['OfvIntentAhorcar', 'OfvIntentQuemar','OfvIntentPrivacionLibrtd', 'OfvPrivacionLibrtd','OfvIntentAhogar','OfvIntentMatar']           

#OtraViold=['OfvUsoAnimalVictimizar', 'OfvGrooming',]        
      
#Diccionario1={'ViolSex':ViolSex,'OtraViol':OtraViol}
Diccionario2={'ViolSexa': ViolSexa, 'ViolSexb':ViolSexb,'ViolSexc':ViolSexc,
              'OtraViola':OtraViola,'OtraViolb':OtraViolb, 'OtraViolc':OtraViolc,
              #'OtraViold':OtraViold
              }


#orden de etiquetes
ord1=['0-5','6-10','11-15','16-20','21-25','26-30','31-35',
      '36-40','41-45','46-50','51-55','56-60','61-65',
      '66-70', '71-75','76-80','81-85','86-90''96-100'    
  ]
ord2=[2018,2019,2020,2021,2022,2023,2024]

Lista5=['0-5','6-10','11-15','16-20','21-25','26-30','31-35',
      '36-40','41-45','46-50','51-55','56-60','61-65',
      '66-70', '71-75','76-80','81-85',
      '86-90','96-100'    
  ]

Lista6=['Femenino',
        'Masculino',
        'Ns/Nc',
        'Trans']

#funcion F1 solo un input y porcentajes. 
def F1(df, input1):
    dfi=df
    col=input1
    # Agrupar por la columna especificada y calcular el conteo de filas
    grouped = df.groupby(col).size().reset_index(name='conteo')

    # Calcular el total de filas en df1
    total_filas = len(df)

    # Calcular el porcentaje para cada valor de la columna
    grouped['porcentaje'] = grouped['conteo'] / total_filas * 100
    grouped['porcentaje']=grouped['porcentaje'].round(2)
    # Ordenar por la columna para mantener un orden específico si es necesario
    grouped = grouped.sort_values(by=col)

    # Crear el nuevo DataFrame df2
    df2 = grouped.copy()

    return df2

def F2(df, input1, input2):
    dfi=df
    col1=input1
    col2=input2
    # Agrupar por las columnas especificadas y calcular el conteo de filas
    grouped = dfi.groupby([col1, col2]).size().reset_index(name='conteo')
    #print(grouped)
    total_filas_col2 = dfi.groupby(col2).size().reset_index(name='total_conteo')
    # Realizar un right join en la columna col2 para anexar total_conteo
    grouped = grouped.merge(total_filas_col2, on=col2, how='right')

    # Calcular el porcentaje para cada valor de col2 respecto a col2
    grouped['porcentaje'] = grouped['conteo'] / grouped['total_conteo'] * 100
    grouped['porcentaje']=grouped['porcentaje'].round(2)
   

    #print(grouped)
    return grouped

def F3(df, input1, input2):
    
    col1=input1
    col2=input2
    dfi = df#[df[col2] == 'SI']
    
    # Agrupar por las columnas especificadas y calcular el conteo de filas
    grouped = dfi.groupby([col1, col2]).size().reset_index(name='conteo')
    
    # Calcular el total de filas por valor de col2
    total_filas_col2 = dfi.groupby(col2).size().reset_index(name='total_conteo')
    
    # Realizar un right join en la columna col2 para anexar total_conteo
    grouped = grouped.merge(total_filas_col2, on=col2, how='right')

    # Calcular el porcentaje para cada valor de col2 respecto a col2
    grouped['porcentaje'] = grouped['conteo'] / grouped['total_conteo'] * 100
    grouped = grouped.sort_values(by=[col1, col2])
    grouped['porcentaje']=grouped['porcentaje'] .round(2) 
    
    # Renombrar columnas
    grouped.rename(columns={'porcentaje': f'{col2}(%)', 'conteo': f'{col2}(#)'}, inplace=True)
    
    # Eliminar columnas no deseadas
    #grouped.drop(columns=[col2, 'total_conteo'], inplace=True)
    
    return grouped

def F4(df, input1, input2,diccionario):
    key1=input1
    columna1=input2
    dic=diccionario
    if key1 not in dic:
        print(f"La clave '{key1}' no está definida en el diccionario.")
        return None
    
    # Obtener la lista de columnas a procesar
    columnas = dic[key1]
    
    # Filtrar el DataFrame según todas las categorías de columna1
    resultados = pd.DataFrame(columns=['Columna', 'Cantidad_SI', 'Porcentaje_SI', columna1])
    
    for categoria in df[columna1].unique():
        df_filtrado = df[df[columna1] == categoria]
        
        # Iterar sobre las columnas y calcular la cantidad de 'SI' y su porcentaje
        for col in columnas:
            # Contar la cantidad de 'SI' en la columna actual
            conteo_si = df_filtrado[col].eq('SI').sum()
            
            # Calcular el porcentaje de 'SI' respecto al total de filas del subset
            total_filas = len(df_filtrado)
            porcentaje_si = (conteo_si / total_filas) * 100
            
            # Si el porcentaje_si es menor o igual a 2, omitir esta columna
            if porcentaje_si <= 0:
                continue
            
            # Preparar los datos para añadir al DataFrame resultados
            data = {
                'Columna': [col],
                'Cantidad_SI': [conteo_si],
                'Porcentaje_SI': [porcentaje_si],
                columna1: [categoria]  # Agregar la categoría como columna adicional
            }
            
            # Convertir los datos en un DataFrame temporal
            df_temp = pd.DataFrame(data)
            
            # Concatenar el DataFrame temporal al DataFrame resultados
            resultados = pd.concat([resultados, df_temp], ignore_index=True)
            resultados['Porcentaje_SI']=resultados['Porcentaje_SI'].round(2)
    
    return resultados


def F5(df, col1, col2, fill_values):
    import itertools
    """
    Completa todas las combinaciones posibles de dos columnas en un DataFrame 
    e inserta filas con valores cero para las combinaciones faltantes.
    
    :param df: DataFrame original
    :param col1: Primera columna para las combinaciones
    :param col2: Segunda columna para las combinaciones
    :param fill_values: Diccionario con valores para llenar las columnas faltantes
    :return: DataFrame con todas las combinaciones posibles y filas faltantes completadas
    """
    # Lista de todas las posibles combinaciones de col1 y col2
    unique_col1 = df[col1].unique()
    unique_col2 = df[col2].unique()

    # Crear todas las combinaciones posibles
    combinaciones = pd.DataFrame(list(itertools.product(unique_col1, unique_col2)), columns=[col1, col2])

    # Hacer un merge con el DataFrame original
    df_full = combinaciones.merge(df, on=[col1, col2], how='left')

    # Rellenar valores NaN con los valores especificados en fill_values
    df_full = df_full.fillna(fill_values)

    return df_full
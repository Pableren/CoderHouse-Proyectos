#archivo reservado para las diferentes funciones que crearemos para manipulacion de datos, visualizacion, etc.
#from google.colab import drive
import numpy as np
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from time import time
from os import sys

def flotante(string):
    #Funcion para transformar string en flotante.
    try:
        return float(string)
    except:
        return float(0)

def graficar_histogramas(df, columnas):
  # Funcion para graficar todos los histogramas de cada una de las variables con los valores de asimetria y curtosis
  fig, axes = plt.subplots(nrows=len(columnas), ncols=1, figsize=(10, 4*len(columnas)))
  for i, columna in enumerate(columnas):
    # Calcular asimetría y curtosis
    asimetria = df[columna].skew()
    curtosis = df[columna].kurt() - 3
    # Graficar histograma
    sns.histplot(data=df, x=columna, ax=axes[i])
    axes[i].set_title(f"{columna}\nAsimetria: {asimetria:.2f}\nCurtosis: {curtosis:.2f}")
  plt.tight_layout()
  return fig

def time_series(dfe_agg,column,x_axis,title=''):
    # Funcion para graficar variables en base al tiempo
    n_rows = len(column)
    fig, axes = plt.subplots(nrows=n_rows, figsize=(10, 30))
    fig.tight_layout(h_pad=5)
    for i in range(n_rows):
        ax = axes[i]
        sns.lineplot(data=dfe_agg, x=x_axis, y=column[i], ax=ax)
        ax.set_title(f'{column[i]} {title}')
    return plt.show()

def grafico_de_caja(df,column, title=''):
    # Funcion para graficar todos los graficos de caja de cada una de las variables del dataframe.
    n_rows = len(column)
    fig, axes = plt.subplots(nrows=n_rows, figsize=(15, 20))
    fig.tight_layout()

    for i in range(n_rows):
        ax = axes[i]
        sns.boxplot(data=df[column[i]], ax=ax, orient='h')
        ax.set_title(f'{column[i]} {title}', loc="right")
    return plt.show()

def target(df, columna_objetivo):
    #Funcion target, creada para ver la correlacion de todas las variables contra 1 variable especifica.
    columns = df.columns # Obtener las columnas del DataFrame
    contra_columnas = [col for col in columns if col != columna_objetivo] # Filtrar las columnas para excluir la columna objetivo
    num_plots = len(contra_columnas) # Calcular el número de subgráficos necesarios
    # Calcular el número de filas y columnas para organizar los subgráficos
    num_rows = (num_plots // 3) + 1 # Organizar en filas de a lo sumo 3 subgráficos
    num_cols = min(num_plots, 3)
    fig, axes = plt.subplots(num_rows,num_cols, figsize=(9, 3*num_rows))
    fig.suptitle(f'Scatterplots: {columna_objetivo} vs demas columnas', y=1.02)
    if num_rows == 1 and num_cols == 1:
        axes = [[axes]] # Asegurarse de que 'axes' sea una matriz bidimensional para manejar el caso de una sola fila o columna
    for i in range(num_rows):
        for j in range(num_cols):
            if i * 3 + j < num_plots:
                contra_columna = contra_columnas[i * 3 + j]
                axes[i][j].scatter(df[contra_columna], df[columna_objetivo], alpha=0.5)
                axes[i][j].set_xlabel(contra_columna)
                axes[i][j].set_ylabel(columna_objetivo)
    plt.tight_layout()
    plt.show()


def variable_tiempo(df,variable):
    # funcion creada para ver la acumulacion de valores en diferentes marcos temporales de una variable.
    columnas_tiempo = ['year','quarter','month','weekday','hour','weekend']
    plt.figure(figsize=(18, 14))
    y = 3
    x = 2
    z = 1
    for col in columnas_tiempo:
        plt.subplot(x,y,z,facecolor = 'skyblue')
        z += 1
        df.groupby(col)[variable].sum().plot(kind='bar',color='blue')
        plt.title(f'{variable} vs {col}')
        plt.xlabel(col)
        plt.ylabel("kW")


def normalize(df):
    # funcion para normalizar el dataset
    result = df.copy()
    for feature_name in df.columns:
        max_val = df[feature_name].max()
        min_val = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_val) / (max_val - min_val)

    return result
![](https://apifootball.com/img/logo2.png)

----
## Descripción
<p>
Proyecto para analizar data de una api de fútbol, realizando el consumo de la misma a través de Python. Posteriormente, se agregan funcionalidades para realizar transformaciones de los datos y cargarlos en un servidor local.
</p>

## Herramientas ulizadas en el proyecto:

- Python (Pandas, Jupyter Notebook)
- SQL Server Management Studio (Vistas, Store Procedures)
- PowerBI
- Visual Studio (SSIS)

## Historias de usuario

- <b>Primer sprint</b>: Consumo de información de API FOOTBALL, más la funcionalidad de interpretación de datos en DataFrames.
- <b>Segundo sprint</b>: Creación de la base de datos local, más la conexión hacia la misma a través de un script de Python.
- <b>Tercer sprint</b>: Desarrollo de transformaciones para realizar la creación de la tabla y los respectivos inserts de cada una (También se desarrollaron mapeos de tipos de datos que llegan en un DataFrame para parsearlo a formato SQL Sever)
- <b>Cuarto sprint</b>: Desarrollo del script main.py para permitir la ejecución automatica del script de data_api_football.
- <b>Quinto sprint</b>: Creación de un bosquejo de el reporte en PBI, más la conexión al origen (SQL Server) y armado de modelo de datos.
- <b>Sexto sprint</b>: Mejoras en el proceso del script de python + mejora del reporte de PBI. Y realización de un ETL para almacenar los datos en otro Server, aplicándole transformaciones para enriquecer los mismos.

----
## Reporte PowerBI
![Enlace al Reporte PowerBI](https://github.com/ramiperez/Data-Api-Football/blob/main/pbi_reports/Cap_pbi_api_football.png)


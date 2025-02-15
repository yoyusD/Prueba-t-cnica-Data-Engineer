import pandas as pd
import re #Función para detectar las filas cuyo valores en company_name tienen el valor exadecimal 0xFFFF

# Guardo los datos de prueba en un dataframe
df = pd.read_csv('data_prueba_tecnica_1.csv')
print(df.head())

# Renombro columnas para que coincidan con el esquema propuesto
df = df.rename(columns={'name': 'company_name', 'paid_at': 'updated_at'})

# Convierto 'id' a string
df['id'] = df['id'].astype(str)
# Elimino filas donde 'id' es un valor nulo
df = df.dropna(subset=['id'])
df = df[df['id'] != 'nan']
# Convierto a string y conservar valores nulos para company_name y company_id
df['company_name'] = df['company_name'].astype('string')
df['company_id'] = df['company_id'].astype(str).replace({'nan': None})
df.loc[df['company_id'].str.contains(r'\*', na=False), 'company_id'] = None
# Convierto 'amount' a float redondeado a 2 decimales y 'status' a string
df['amount'] = df['amount'].astype(float).round(2)
df['status'] = df['status'].astype(str)
# Convierto 'created_at' y 'updated_at' a datetime y formatear a ISO YYYY-MM-DD para su uso en PostgreSQL
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce').dt.strftime('%Y-%m-%d')
df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce').dt.strftime('%Y-%m-%d')

# Elimino filas donde 'company_id' y 'company_name' sean nulos o vacíos
df = df[df['company_id'].notnull() & (df['company_id'] != '')]
df = df[df['company_name'].notnull() & (df['company_name'] != '')]
# Filtrar y eliminar filas cuyo company_name contenga un patrón hexadecimal (ej. "0xFFFF")
hex_pattern = r'0x[0-9A-Fa-f]+'
df = df[~df['company_name'].str.contains(hex_pattern, flags=re.IGNORECASE, na=False)]

# Guardo el data frame transformado
df.to_csv('data_prueba_tecnica_1_transformada.csv', index=False)

# Adaptamos las tablas para el punto 1.4 Dispersión de la información
# Con 'company_id' y 'company_name', eliminamos duplicados basados en 'company_id'
df_companies = df[['company_id', 'company_name']].drop_duplicates(subset=['company_id'], keep='first')
df_companies.to_csv('data_company.csv', index=False)
df_charges = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']]
df_charges.to_csv('data_charge.csv', index=False)



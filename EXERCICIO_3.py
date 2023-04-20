import pandas as pd #importando a biblioteca pandas

stores = pd.read_csv('Stores.csv', sep = ',') #lendo arquivo csv com pandas
stores_df = pd.DataFrame(stores) #criando um DataFrame
stores_df.rename(columns = {'Store ID' : 'ID_Loja', 'Store_Area' : 'Área', 'Items_Available' : 'Itens_disponíveis', 'Daily_Customer_Count' : 'Visitantes', 'Store_Sales' : 'Vendas(US$)'}, inplace = True) #renomeando colunas
#inicio das análises das colunas
print("Análise Itens disponíveis:")
print("Máximo Itens_disponíveis: {}" .format(stores_df['Itens_disponíveis'].max()))
print("Mínimo Itens_disponíveis: {}" .format(stores_df['Itens_disponíveis'].min()))
print("Média Itens_disponíveis: {:.2f}" .format(stores_df['Itens_disponíveis'].mean()))
print("Desvio padrão Itens_disponíveis: {:.2f}\n" .format(stores_df['Itens_disponíveis'].std()))

print("Análise Visitantes:")
print("Máximo Visitantes: {}" .format(stores_df['Visitantes'].max()))
print("Mínimo Visitantes: {}" .format(stores_df['Visitantes'].min()))
print("Média Visitantes: {:.2f}" .format(stores_df['Visitantes'].mean()))
print("Desvio padrão Visitantes: {:.2f}\n" .format(stores_df['Visitantes'].std()))

print("Análise Vendas:")
print("Máximo Vendas: {}" .format(stores_df['Vendas(US$)'].max()))
print("Mínimo Vendas: {}" .format(stores_df['Vendas(US$)'].min()))
print("Média Vendas: {:.2f}" .format(stores_df['Vendas(US$)'].mean()))
print("Desvio padrão Vendas: {:.2f}\n" .format(stores_df['Vendas(US$)'].std()))
#fim das análises das colunas


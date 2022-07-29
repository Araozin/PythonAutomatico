import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7262b3192171a67b1cf2eb3583b4f0f1"
# Your Auth Token from twilio.com/console
auth_token  = "cfdb954a8d9ac8bee494637646c678b4"
client = Client(account_sid, auth_token)

# lógica de progamação

# Abrir os 6 arquivos em excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
            to="+5586999378607",
            from_="+15017250604",
            body=f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        print(message.sid)



# Para cada arquivo:

# Verifica se algum valor na coluna Vendas arquivo é maior que 55.000

# Se for maior que 55.00 -> Envia um SMS com o nome, o mês e as vendas dele

# Caso não seja maior que 50.00 não quero fazer nada


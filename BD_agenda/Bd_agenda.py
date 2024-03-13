import mysql.connector
from faker import Faker
from faker.providers import BaseProvider

# localização do fake
locales = 'pt-BR'
fake = Faker(locales) 

#Criando uma nova classe do fake
class GruposProvider(BaseProvider):
    def grupos(self):
        return self.random_element(["Familia", "Amigos", "Trabalho", "Escola"])

fake.add_provider(GruposProvider)

# Conecte-se ao servidor MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="contatos"
)
# Verifique se conectou
if conexao.is_connected():
    print("Conectado com sucesso!")

    # Para executar consultas
    cursor = conexao.cursor()

    # Passar o comando SQL
    for _ in range(50):
        nome = fake.name()
        email = fake.email()
        telefone = fake.phone_number()
        grupo = fake.grupos()
        cursor.execute(f"INSERT INTO agenda (nome, email, telefone, grupos) VALUES ('{nome}', '{email}', '{telefone}', '{grupo}')") 

    # Commit das alterações
    conexao.commit()

    print("Inserção de dados concluída com sucesso!")

# Feche o cursor e a conexão
cursor.close()
conexao.close()

# Aula-BD-06-03
Exercicio de DB

 - SHOW DATABASES;

- CREATE DATABASE agenda_contatos;

- USE agenda_contatos;

- CREATE TABLE contatos(nome VARCHAR(255) NOT NULL,email VARCHAR(255),telefone VARCHAR(15));

- ALTER TABLE contatos ADD grupos VARCHAR(255);

- INSERT INTO contatos (nome,email,telefone,grupos)  VALUES

('Carlos','Minuscloth@gmail.com','16988505388','trabalho'),

('Carlos Silva', 'carlos.silva@email.com', '11987654321', 'trabalho'),

('Ana Souza', 'ana.souza@email.com', '21987654321', 'amigos'),

('Pedro Santos', 'pedro.santos@email.com', '31987654321', 'família'),

('Mariana Oliveira', 'mariana.oliveira@email.com', '41987654321', 'trabalho'),

('João Pereira', 'joao.pereira@email.com', '51987654321', 'amigos'),

('Fernanda Costa', 'fernanda.costa@email.com', '61987654321', 'família'),

('Rafaela Almeida', 'rafaela.almeida@email.com', '71987654321', 'trabalho'),

('Rodrigo Santos', 'rodrigo.santos@email.com', '81987654321', 'amigos'),

('Amanda Lima', 'amanda.lima@email.com', '91987654321', 'família'),

('Lucas Silva', 'lucas.silva@email.com', '101987654321', 'trabalho'),

('Isabela Souza', 'isabela.souza@email.com', '111987654321', 'amigos'),

('Gustavo Santos', 'gustavo.santos@email.com', '121987654321', 'família'),

('Carolina Oliveira', 'carolina.oliveira@email.com', '131987654321', 'trabalho'),

('Diego Pereira', 'diego.pereira@email.com', '141987654321', 'amigos'),

('Camila Costa', 'camila.costa@email.com', '151987654321', 'família'),

('Marcelo Almeida', 'marcelo.almeida@email.com', '161987654321', 'trabalho'),

('Bruna Santos', 'bruna.santos@email.com', '171987654321', 'amigos'),

('Guilherme Lima', 'guilherme.lima@email.com', '181987654321', 'família'),

('Natália Silva', 'natalia.silva@email.com', '191987654321', 'trabalho'),

('Felipe Souza', 'felipe.souza@email.com', '201987654321', 'amigos'),

('Laura Oliveira', 'laura.oliveira@email.com', '211987654321', 'família'),

('Vinícius Pereira', 'vinicius.pereira@email.com', '221987654321', 'trabalho'),

('Jéssica Costa', 'jessica.costa@email.com', '231987654321', 'amigos'),

('Matheus Almeida', 'matheus.almeida@email.com', '241987654321', 'família'),

('Beatriz Santos', 'beatriz.santos@email.com', '251987654321', 'trabalho'),

('Luan Lima', 'luan.lima@email.com', '261987654321', 'amigos'),

('Carla Silva', 'carla.silva@email.com', '271987654321', 'família'),

('Fábio Souza', 'fabio.souza@email.com', '281987654321', 'trabalho'),

('Renata Oliveira', 'renata.oliveira@email.com', '291987654321', 'amigos'),

('Paulo Pereira', 'paulo.pereira@email.com', '301987654321', 'família'),

('Vanessa Almeida', 'vanessa.almeida@email.com', '311987654321', 'trabalho'),

('Thiago Santos', 'thiago.santos@email.com', '321987654321', 'amigos'),

('Patrícia Lima', 'patricia.lima@email.com', '331987654321', 'família'),

('Gabriel Silva', 'gabriel.silva@email.com', '341987654321', 'trabalho'),

('Juliana Souza', 'juliana.souza@email.com', '351987654321', 'amigos'),

('Fernanda Almeida', 'fernanda.almeida@email.com', '371987654321', 'trabalho'),

('Rafael Santos', 'rafael.santos@email.com', '381987654321', 'amigos'),

('Bianca Lima', 'bianca.lima@email.com', '391987654321', 'família'),

('Anderson Silva', 'anderson.silva@email.com', '401987654321', 'trabalho'),

('Caroline Souza', 'caroline.souza@email.com', '411987654321', 'amigos'),

('Renato Oliveira', 'renato.oliveira@email.com', '421987654321', 'família'),

('Aline Almeida', 'aline.almeida@email.com', '431987654321', 'trabalho'),

('Marcos Santos', 'marcos.santos@email.com', '441987654321', 'amigos'),

('Tatiane Lima', 'tatiane.lima@email.com', '451987654321', 'família'),

('Douglas Silva', 'douglas.silva@email.com', '461987654321', 'trabalho'),

('Ana Carolina Souza', 'ana.carolina.souza@email.com', '471987654321', 'amigos'),

('Cristina Pereira', 'cristina.pereira@email.com', '511987654321', 'escola'),

('André Lima', 'andre.lima@email.com', '521987654321', 'escola'),

('Fernando Costa', 'fernando.costa@email.com', '531987654321', 'escola'),

('Rita Oliveira', 'rita.oliveira@email.com', '541987654321', 'escola');


- SELECT * FROM contatos;

- SELECT nome,telefone FROM contatos WHERE grupos='amigos';

- SELECT nome FROM contatos WHERE nome LIKE'car___';

- SELECT nome FROM contatos WHERE nome LIKE'car%';

- SELECT nome,grupos FROM contatos WHERE grupos='trabalho' ORDER BY nome LIMIT 5 OFFSET 2;

- UPDATE contatos set telefone='12222' WHERE nome LIKE 'Carlos%';

- SELECT telefone FROM contatos WHERE nome LIKE 'Carlos%';

- UPDATE contatos set grupos='escola' WHERE nome LIKE 'Rafa%';

- SELECT nome,grupos FROM contatos WHERE nome LIKE 'Rafa%';

- UPDATE contatos set grupos='escola';

- UPDATE contatos set email='cidaDaMandioca@email.com' WHERE nome='Carlos';

- SELECT * FROM contatos WHERE email='cidaDaMandioca@email.com';

- UPDATE contatos set telefone='9422' WHERE nome='Marcos Santos';

- SELECT telefone from contatos WHERE nome='Marcos Santos';

- UPDATE contatos SET telefone = '123456789' WHERE nome = 'Pedro Santos';

- UPDATE contatos SET email = 'novo_email@email.com' WHERE nome = 'Ana Souza';

- UPDATE contatos SET grupos = 'trabalho' WHERE nome LIKE '%Silva%';

- UPDATE contatos SET grupos = 'família' WHERE telefone LIKE '11%';

- UPDATE contatos SET grupos = 'trabalho' WHERE nome LIKE 'A%';

- DELETE FROM contatos WHERE nome = 'Ana Souza';

- DELETE FROM contatos WHERE nome='Carlos';
  
- DELETE FROM contatos WHERE email='rita.oliveira@email.com';
  
- ALTER TABLE contatos ADD favorito varchar(14);
  
- SET SQL_SAFE_UPDATES = 0; 

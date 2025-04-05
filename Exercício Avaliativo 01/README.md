# Exercício Avaliativo 1 - MongoDB

## Orientações

Neste exercício vamos criar um sistema simples de motoristas por aplicativo. Para isso devemos seguir o diagrama UML  juntamente com as especificações a seguir.

## 📏 Diagrama UML

![UM motorista pode ter varias corridas e uma corrida pode ter apenas um passageiro.](attachment:00e66163-268c-48f8-a5b3-395c1b8bab5e:Untitled.png)


## 🧾 Especificações

1. Deve haver uma classe **`Database`** que se conecta com o banco de dados. 
    
    <aside>
    📎 Enviar classe Database
    
    </aside>
    
2. Deve haver uma classe **`MotoristaDAO`** que apresenta uma relação de **composição** com a classe **`Database`,** para interagir com o banco de dados**, além de** métodos de **CRUD** (pelo menos um de cada) para criar, ler, atualizar e deletar uma **`Motorista`** do banco de dados.
    
    <aside>
    📎 Enviar classe **`MotoristaDAO` .**
    
    </aside>
    
3. Deve haver a estrutura do diagrama UML dentro do projeto com todas a suas características.
    
    <aside>
    📎 Enviar classes Motorista, Corrida e Passageiro.
    
    </aside>
    
4. Deve haver uma collection **`Motoristas`**dentro do banco de dados, que apresenta um array de **`Corridas`** . Em que cada **`Corrida`**temos a nota da corrida, a distancia percorrida o valor e um **`Pasageiro`** . O **`Passageiro`** deve ter nome e um documento
    
    <aside>
    📎 Enviar print da Collection Motorista no Compass.
    
    </aside>
    
5. Deve ser criada uma classe chamada **`MotoristaCLI`**, que irá gerenciar um menu em linha de comando e realizar os métodos de CRUD. Na opção "create", o programa deve criar um objeto do tipo **`Passageiro`**, seguido por um ou mais objetos do tipo **`Corrida`** , e finalmente um objeto do tipo **`Motorista`** (que apresenta as características do diagrama UML) que será passado para a classe **`MotoristaCLI`** para criar o motorista no banco de dados.
    
    <aside>
    📎 Enviar Classe **`MotoristaCLI` .**
    
    </aside>
    
6. Crie no Compass um Schema para a collection **`Motoristas`**.
    
    <aside>
    📎 Enviar print do Schema no Compass.
    
    </aside>
## Gods Unchained Machine Learning (GU-ML)

### Contexto
Gods Unchained é um jogo de cartas que envolve montar um deck com uma estratégia alinhada com o Deus, escolhido previamente, do jogador.
Para poder utilizar as diferentes cartas do deck é necessário que o valor de mana da carta seja igual ou menor ao valor de mana que o jogador possui na sua rodada. Além disso, o valor de mana adicionado a reserva do jogador altera a depender do momento do jogo. Por isso, é necessário que o jogador tenha conhecimento se a carta que ele irá adicionar no deck é uma carta para o momento "early" do jogo, ou para o momento "late" do jogo.

### Objetivo
* Rotular a carta de interesse do jogador para o momento "early" ou "late" do jogo.

#### Iniciando a aplicação localmente
O repositório possui um arquivo `compose.yaml` para desenvolvimento local. Para iniciar a aplicação basta realizar o comando.
```
make run-local
```
A aplicação conta com dois 'endpoints', um para inserir uma carta na base da aplicação.
```
'http://localhost:80/gu-ml/card'
```
E um endpoint para coletar as informações referentes a uma carta, utlizando o ID da carta.
```
'http://localhost:80/gu-ml/card/{card_id}'
```
Para informações a respeito das entidades retornadas e como realizar chamadas, pode-se consultar a documentação da aplicação no endpoint.
```
'http://localhost:80/docs'
```

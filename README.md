# Árvore Fractal usando o módulo Turtle em Python 🌳🐍🐢
A Árvore Fractal é uma estrutura gráfica que se assemelha a uma árvore ramificada. A biblioteca Turtle fornece um ambiente de desenho gráfico que permite criar figuras e animações interativas.

## Pré-requisitos
Certifique-se de ter o Python instalado no seu sistema antes de começar, ou o VS Code com a extensão do Python.
Como utilizarei o módulo Turtle que é uma biblioteca padrão do Python, não é necessário instalar nada.

## Passo 1: Importando o módulo Turtle
Antes de tudo, é necessário importar o módulo Turtle. Isso permitirá usar as funções e objetos do Turtle para desenhar a árvore.
```gql
import turtle
``` 

## Passo 2: Definindo a função `draw_tree` 
Em seguida, é importante definir uma função chamada `draw_tree` que será responsável por desenhar a árvore fractal. Essa função usará recursão para criar a estrutura ramificada da árvore.

A função draw_tree recebe três parâmetros:
- **t**: O objeto Turtle que usaremos para desenhar.
- **branch_len**: O comprimento do galho atual da árvore.
- **angle**: O ângulo de rotação entre os galhos da árvore.

```gql
def draw_tree(t, branch_len, angle):
    if branch_len < 5:
        t.color("green")  # Define a cor verde para as folhas
        t.stamp()  # Desenha uma folha
        t.color("black")  # Volta para a cor marrom para os galhos
        return
    else:
        t.forward(branch_len)
        t.right(angle)
        draw_tree(t, branch_len-15, angle)
        
        t.left(angle*2)
        draw_tree(t, branch_len-15, angle)
        
        t.right(angle)
        t.backward(branch_len)
```
A função `draw_tree` tem uma condição de parada. Se o comprimento do galho for menor que 5, significa que estou nas folhas da árvore. Nesse caso, a cor é alterada para verde, desenhamos uma folha e, em seguida, a cor é alterada novamente para preto para desenhar os galhos.
Caso contrário, avança pelo comprimento do galho, gira para a direita pelo ângulo especificado e chama recursivamente a função `draw_tree` duas vezes para desenhar os galhos menores. Após desenhar os galhos menores, faz as rotações e avanços necessários para retornar à posição original antes de chamar a função.

## Passo 3: Configurações iniciais
Antes de chamar a função `draw_tree`, é necessário configurar algumas opções iniciais para a tela e Turtle(🐢).
- Criei uma tela com uma resolução de 800x600 pixels e definindo um background como branco.
```gql
# Configurações iniciais
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("white")
```

## Passo 4: Criação
Agora, vou criar a 🐢 que usarei para desenhar a árvore fractal.
- A função `turtle.Turtle()` cria um objeto Turtle que posso usar para desenhar. 
- Defini a velocidade da 🐢 como 0, o que a faz se mover o mais rápido possível.
```gql
t = turtle.Turtle()
t.speed(0)
```

## Passo 5: Posicionando a tartaruga
Antes de desenhar a árvore fractal, vou posicionar a 🐢 no local inicial.
- Vou girar a 🐢 90 graus para a esquerda, movendo-a para cima (sem desenhar) e, em seguida, movendo-a para trás 200 unidades.
```gql
t.left(90)
t.up()
t.backward(200)
t.down()
```

## Passo 6: Chamando a função `draw_tree`
Agora que tudo está configurado, vou chamar a função `draw_tree` para desenhar a árvore.
- Estou chamando a função draw_tree passando a 🐢 t, o comprimento inicial do galho como 100 e o ângulo de rotação como 30 graus.
```gql
draw_tree(t, 100, 30)
```

## Passo 7: Fechando a janela
Por fim, vou garantir que a janela se feche quando eu clicar nela.
- A função `wn.exitonclick()` espera por um clique do usuário na janela e, em seguida, fecha a janela.
```gql
wn.exitonclick()
```
_Espero que esta documentação tenha sido útil para entender como construir uma Árvore Fractal usando o módulo Turtle em Python. Crie você mesmo sua própria árvore!🎄✨_

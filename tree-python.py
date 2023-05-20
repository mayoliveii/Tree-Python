import turtle

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

# Configurações iniciais
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("white")

# Criação 
t = turtle.Turtle()
t.speed(0)  # Define a velocidade (0 = a mais rápida)

# Posicionamento
t.left(90)
t.up()
t.backward(200)
t.down()

# Chamada da função para desenhar a árvore fractal
draw_tree(t, 100, 30)

# Finaliza a janela ao clicar nela
wn.exitonclick()
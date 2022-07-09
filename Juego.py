#Integrantes
#Ivan Durán 21.521.054-5
#Ariana Gómez 26.529.225-9
#Eduardo Barrera 21.229.402-0
#José Cáceres 21.205.805-K

from turtle import speed
import pygame, sys, random
                
# Aparicion Obstaculos y pociones

def valida_potions(x, y, potions_list):
    
    for i in range (len(potions_list)):

        # si colisiona 
        if potions_list[i][0]//30 == x//30 and potions_list[i][1]//30 == y//30:
            potions_list[i] = (-100, -100)
            
            print(potions_list)
            return (potions_list)
        

    

def valida_obstacle(x, y, obstacle_list):
    validacion = 0
    for i in range (len(obstacle_list)):

        # si colisiona 
        if obstacle_list[i][0]//30 == x//30 and obstacle_list[i][1]//30 == y//30:
            validacion = True

    if validacion:
        return(False)
    else:
        return(True)

    

def spawn(table, dado, pos1, pos2):
    count = 1
    list = []
    while count <= dado:
            for i in range (20):
            
                    for j in range (20):
                        
                        if table[j][i] == pos1 or table[j][i] == pos2:

                            if random.uniform(0, 1) <= 0.1:
                                if count <= dado:
                                    list.append((i*30, j*30))
                                    count += 1
    return(list)
    
# Aparicion Jugador y Computadoras
def bot_spawn(table):
    
    count = 0
    while count < 1:
            for i in range (20):
            
                    for j in range (20):
                        
                        if table[j][i] == 1 or table[j][i] == 2:

                            if random.uniform(0, 1) <= 0.001:
                                if count != 1:
                                    bot_x = i * 30
                                    bot_y = j * 30
                                count += 1

    return[bot_x, bot_y]

# Movimiento de las computadoras
def bot_move(table, bot_x, bot_y, bot_speed, bot_width):

    loop = True    
    while loop:
        if random.uniform(0, 1) <= 0.5:
            #horizontalmente
            if random.uniform(0, 1) <= 0.5:
                #derecha
                if table[(bot_y)//30] [(bot_x + bot_width) //30]!= 0 and table[(bot_y + bot_width)//30] [(bot_x + bot_width) //30]!= 0 and bot_x + 20 + bot_speed < 600 :      
                    bot_x += bot_speed                   
            else:
                #Izquierda
                if table[(bot_y)//30] [(bot_x - bot_speed) //30]!= 0 and table[(bot_y + bot_width)//30] [(bot_x - bot_speed) //30]!= 0 and (bot_x - bot_speed) > 0:                                                          
                    bot_x  -= bot_speed

        else:
            #Verticalmente
            if random.uniform(0, 1) <= 0.5:
                #Arriba
                if table[(bot_y - bot_speed)//30] [(bot_x) //30]!= 0 and table[(bot_y - bot_speed)//30] [(bot_x + bot_width) //30]!= 0 and bot_y - bot_speed > 0:                                                        
                    bot_y  -= bot_speed
                    
            else:
                #Abajo
                if table[(bot_y + bot_width)//30] [(bot_x) //30]!= 0 and table[(bot_y + bot_width)//30] [(bot_x + bot_width) //30]!= 0 and bot_y + 20 + bot_speed < 600:                                                          
                    bot_y  += bot_speed
        loop = False





    return [bot_x, bot_y]


def main():
    
    
    pygame.init()
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50, 10)

    # Ventana y música

    screen_WIDTH = 600
    screen_HEIGHT = 600
    screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))

    background = pygame.image.load("background.png")
    pygame.display.set_caption('La Cosa')

    soundtrack = pygame.mixer.Sound("soundtrack.wav") #Music: Lost Woods. Composers: Koji Kondo.
    soundtrack.play(-1)
    soundtrack.set_volume(0.2)

    # Tablero. 0 paredes, 1 piezas, 2 Camino
    table = [
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
[0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
[1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
[1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
[1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],
[0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
[0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
[0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
[0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
[0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
[2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
[2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
[2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
]
 


    # Jugador

    player_sprite = pygame.image.load("player.png")
    player_sprite = pygame.transform.scale(player_sprite, (20, 20))
    player_rect = player_sprite.get_rect()
    player_rect.x, player_rect.y  = bot_spawn(table)
    player_speed = 2
    

    # Computadoras

    bot_sprite = pygame.image.load("bot.png")
    bot_sprite = pygame.transform.scale(bot_sprite, (20, 20))
    
    bot_1_rect = bot_sprite.get_rect()
    bot_2_rect = bot_sprite.get_rect()
    bot_3_rect = bot_sprite.get_rect()
    

    bot_1_rect.x, bot_1_rect.y  = bot_spawn(table) 
    
    bot_2_rect.x, bot_2_rect.y = bot_spawn(table)
    
    bot_3_rect.x, bot_3_rect.y  = bot_spawn(table)

    bot_speed = 10


    # Tablero y obstaculos

    tree = pygame.image.load("Arbol.png")
    tree = pygame.transform.scale(tree, (30, 30))
    

    room = pygame.image.load("flowers.png")
    room = pygame.transform.scale(room, (30, 30))

    
    road = pygame.image.load("road.png")
    road = pygame.transform.scale(road, (30, 30))

    potions_sprite = pygame.image.load("pociones.png")
    potions_sprite = pygame.transform.scale(potions_sprite, (18, 18))

    potions_dado = random.randint(35, 50)
    potions_list = spawn(table, potions_dado, 1, 2)
    


    obstacle_sprite = pygame.image.load("obstaculo.png")
    obstacle_sprite = pygame.transform.scale(obstacle_sprite, (25, 25))

    obstacle_dado = random.randint(10, 15)
    obstacle_list = spawn(table, obstacle_dado, 1, 1)
    
    
                    


    # La Cosa
    dado = random.randint(0,3)
    
    if dado == 0:
        la_cosa = player_rect
    elif dado == 1:
        la_cosa = bot_1_rect
    elif dado == 2:
        la_cosa = bot_2_rect
    elif dado == 3:
        la_cosa = bot_3_rect
    

    run = True
    bot_count_move = 0 

    print(potions_list)

    while  run :
        
        screen.blit(background, [0,0])

        clock.tick(60)


        # Tablero
        for i in range (20):
    
            for j in range (20):
        
                
                # Paredes
                if table[j][i] == 0:
                    
                    screen.blit(tree, (i*30, j*30))

                
                # Habitaciones
                if table[j][i] == 1:
                    
                    screen.blit(room, (i*30, j*30))
                
                # Camino
                if table[j][i] == 2:
                    
                    screen.blit(road, (i*30, j*30))


        # Pociones y Obstaculos
        for i in range(potions_dado):
            
            screen.blit(potions_sprite, potions_list[i])
        for i in range(obstacle_dado):
            
            screen.blit(obstacle_sprite, obstacle_list[i])
        
        
        # Eventos       
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    run = False

            # ----- Movimiento Jugador
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_w:                          
                    if table[(player_rect.y - player_speed)//30][player_rect.x//30] != 0 and table[player_rect.y//30][(player_rect.x + player_sprite.get_width() - player_speed) //30] != 0 and player_rect.y - player_speed > 0 :
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x, player_rect.y - player_speed, obstacle_list) and valida_obstacle(player_rect.x + player_sprite.get_width(), player_rect.y - player_speed, obstacle_list) :
                            player_rect.y -= player_speed
                        
                        
                if event.key == pygame.K_a:
                    if table[player_rect.y//30][(player_rect.x - player_speed) //30] != 0 and table[(player_rect.y + player_sprite.get_height() - player_speed)//30][(player_rect.x - player_speed) //30] != 0 and player_rect.x - player_speed > 0 :
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x - player_speed, player_rect.y, obstacle_list) and valida_obstacle(player_rect.x - player_speed, player_rect.y + player_sprite.get_height(), obstacle_list) :
                            player_rect.x -= player_speed

                if event.key == pygame.K_s:
                    if table[(player_rect.y + player_sprite.get_height())//30][(player_rect.x + player_sprite.get_width() - player_speed)//30] != 0 and table[(player_rect.y + player_sprite.get_height())//30][(player_rect.x)//30] != 0 and player_rect.y + player_sprite.get_height() + player_speed < screen_HEIGHT:
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x , player_rect.y + player_sprite.get_height() + player_speed, obstacle_list) and valida_obstacle(player_rect.x + player_sprite.get_width(), player_rect.y + player_sprite.get_height(), obstacle_list) :
                            player_rect.y += player_speed
                       

                if event.key == pygame.K_d:
                    
                    if table[player_rect.y//30][(player_rect.x + player_sprite.get_width())//30] != 0 and table[(player_rect.y + player_sprite.get_height() - player_speed)//30][(player_rect.x + player_sprite.get_width())//30] != 0 and player_rect.x + player_sprite.get_width() + player_speed < screen_WIDTH :
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x + player_sprite.get_width() + player_speed, player_rect.y , obstacle_list) and valida_obstacle(player_rect.x + player_sprite.get_width(), player_rect.y + player_sprite.get_height(), obstacle_list):
                            player_rect.x += player_speed
                
    

        #! potions_list = valida_potions(player_rect.x, player_rect.y, potions_list)
        


        # Movimiento Computadoras

        bot_count_move += 1

        if bot_count_move == 6:
            bot_count_move = 0
            
            bot_1_rect.x, bot_1_rect.y  = bot_move(table, bot_1_rect.x, bot_1_rect.y, bot_speed, bot_sprite.get_width())
            bot_2_rect.x, bot_2_rect.y  = bot_move(table, bot_2_rect.x, bot_2_rect.y, bot_speed, bot_sprite.get_width())
            bot_3_rect.x, bot_3_rect.y  = bot_move(table, bot_3_rect.x, bot_3_rect.y, bot_speed, bot_sprite.get_width())
        
       
        # Pantalla

        screen.blit(player_sprite, player_rect)
        screen.blit(bot_sprite, bot_1_rect)
        screen.blit(bot_sprite, bot_2_rect)
        screen.blit(bot_sprite, bot_3_rect)
        
        
        

            
        pygame.display.flip()
    sys.exit()



main()
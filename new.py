import pygame 
import sys
from pygame.math import Vector2
import random
 
class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)
    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)
        
        
class SNAKE:
    def __init__(self):
       self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]  
       self.direction=Vector2(1,0)
       self.new_block=False
       self.head_up=pygame.image.load('graphics/head_up.png').convert_alpha()
       self.head_down=pygame.image.load('graphics/head_down.png').convert_alpha()
       self.head_right=pygame.image.load('graphics/head_right.png').convert_alpha()
       self.head_left=pygame.image.load('graphics/head_left.png').convert_alpha()
       self.tail_up=pygame.image.load('graphics/tail_up.png').convert_alpha()
       self.tail_down=pygame.image.load('graphics/tail_down.png').convert_alpha()
       self.tail_right=pygame.image.load('graphics/tail_right.png').convert_alpha()
       self.tail_left=pygame.image.load('graphics/tail_left.png').convert_alpha()
       self.body_tr=pygame.image.load('graphics/body_tr.png').convert_alpha()
       self.body_tl=pygame.image.load('graphics/body_tl.png').convert_alpha()
       self.body_br=pygame.image.load('graphics/body_br.png').convert_alpha()
       self.body_bl=pygame.image.load('graphics/body_bl.png').convert_alpha()
       self.body_vertical=pygame.image.load('graphics/body_vertical.png').convert_alpha()
       self.body_horizontal=pygame.image.load('graphics/body_horizontal.png').convert_alpha()
       self.crunch_sound=pygame.mixer.Sound('graphics/crunch.wav')
       

    def draw_snake(self): 
        self.update_head_graphics()
        self.update_tail_graphics()
        # for block in self.body:
        #     block_rect=pygame.Rect(int(block.x*cell_size),int(block.y*cell_size),cell_size,cell_size)
        #     pygame.draw.rect(screen,(183,121,110),block_rect)
        for index,block in enumerate(self.body):
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            if index==0:
                screen.blit(self.head,block_rect)
            elif index==len(self.body)-1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                if previous_block.x==next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y==next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                 if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                     screen.blit(self.body_tl,block_rect)
                 elif previous_block.x==-1 and next_block.y==1 or previous_block.y==1 and next_block.x==-1:
                      screen.blit(self.body_bl,block_rect)
                 elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                      screen.blit(self.body_tr,block_rect)
                 elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                      screen.blit(self.body_br,block_rect)  

            
    def update_head_graphics(self):
        head_relation=self.body[1]-self.body[0]
        if head_relation==Vector2(1,0):self.head=self.head_left
        if head_relation==Vector2(0,-1):self.head=self.head_down
        if head_relation==Vector2(-1,0):self.head=self.head_right
        if head_relation==Vector2(0,1):self.head=self.head_up
    def update_tail_graphics(self):
        tail_relation=self.body[-2]-self.body[-1]
        if tail_relation==Vector2(1,0):self.tail=self.tail_left
        if tail_relation==Vector2(-1,0):self.tail=self.tail_right
        if tail_relation==Vector2(0,1):self.tail=self.tail_up
        if tail_relation==Vector2(0,-1):self.tail=self.tail_down
               
            
    def move_snake(self):
        if self.new_block==True:
          body_copy=self.body[:]
          body_copy.insert(0,body_copy[0]+self.direction)
          self.body=body_copy[:]
          self.new_block=False
        else:
          body_copy=self.body[:-1]
          body_copy.insert(0,body_copy[0]+self.direction)
          self.body=body_copy[:]
    
        
    def add_block(self):
        self.new_block=True
    def play_crunch_sound(self):
        self.crunch_sound.play()  
    def reset(self):
       self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]  
       self.direction=Vector2(0,0)
        
       
class Main:
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=FRUIT()
    def draw_grass(self):
        grass_colour=(100,225,50)
        for row in range (cell_number):
          if  row%2==0:
             for col in range(cell_number):
                if col%2==0:
                   grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                   pygame.draw.rect(screen,grass_colour,grass_rect)
          else:
              for col in range(cell_number):
                 if col%2!=0:
                   grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                   pygame.draw.rect(screen,grass_colour,grass_rect)
              
    def update(self):
        self.snake.move_snake()
        self.check_eating()
        self.kill()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    def check_eating(self):
       if self.fruit.pos==self.snake.body[0]:
          self.fruit.randomize()
          self.snake.add_block()
          self.snake.play_crunch_sound()
       for block in self.snake.body[1:]:
           if block==self.fruit.pos:
               self.fruit.randomize()
    def kill(self):
        if not 0<=self.snake.body[0].x<=cell_number-1:
            self.game_over()
        if not 0<=self.snake.body[0].y<=cell_number-1:
            self.game_over()
        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_over()
         
    def game_over(self):
       self.snake.reset()
    def draw_score(self):
        score_text=str(len(self.snake.body)-3)   
        score_surface=game_font.render(score_text,True,(56,100,56)) 
        score_x=int(cell_size*cell_number-60)
        score_y=int(cell_size*cell_number-40)
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        apple_rect=apple.get_rect(midright=(score_rect.left,score_rect.centery))
        screen.blit(score_surface,score_rect)     
        screen.blit(apple,apple_rect)
            
            
          
    
        
pygame.mixer.pre_init(44100,-16,2,512)    
pygame.init()

cell_size=40
cell_number=20

screen=pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))# this is a display surface can be only one display surface it is default 
apple=pygame.image.load('graphics/apple.png').convert_alpha()
clock=pygame.time.Clock()
#surface is a layer we can paint we can have different number of surfaces not displayed by default 
# test_surface=pygame.Surface((100,200))#made test surface
# test_surface.fill('blue')
#test_rect=pygame.Rect(100,200,100,100)# x,y height,width
main_game=Main()
game_font=pygame.font.Font('graphics/versatylo_rounded/Versatylo.ttf',25)

SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           pygame.quit()
           sys.exit()#sometimes pygame.quit() does not function properly sp we need to import the sys library 
       if event.type==SCREEN_UPDATE:
           main_game.update ()
       if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_w:
               if main_game.snake.direction.y!=1:
                main_game.snake.direction=Vector2(0,-1)
           if event.key==pygame.K_s:
              if main_game.snake.direction.y!=-1:
                  main_game.snake.direction=Vector2(0,1)
           if event.key==pygame.K_d:
              if main_game.snake.direction.x!=-1:
                 main_game.snake.direction=Vector2(1,0)
           if event.key==pygame.K_a:
               if main_game.snake.direction.x!=1:
                  main_game.snake.direction=Vector2(-1,0)
         
           
       screen.fill((100,215,50))# this is required to fill the color on the surface we can use rgb tuple or we can use color object 
      
       
       main_game.draw_elements()
      

       pygame.display.update()
       clock.tick(60)

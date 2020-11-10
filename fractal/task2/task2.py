import pygame, math, sys, time

class square:
    def __init__(self, rectangle, rot):
        self.ax, self.ay = rectangle.left, rectangle.top
        self.bx, self.by = rectangle.right, rectangle.top
        self.cx, self.cy = rectangle.right, rectangle.bottom
        self.dx, self.dy = rectangle.left, rectangle.bottom
        self.points = ((self.ax, self.ay), (self.bx, self.by), (self.cx, self.cy), (self.dx, self.dy))
        self.size = rectangle.width
        self.mx = rectangle.centerx
        self.my = rectangle.centery
        self.rotation = rot
        self.default_rotation = rot

        self.default_size = self.size
        self.default_points = [[self.ax, self.ay],[self.bx, self.by],[self.cx, self.cy],[self.dx, self.dy]]

    def copy(self):
        return self

    def affine_scaling(self, limit, shrink=True):
        default = False
        k = 0.01
        if shrink:
            if self.size > limit:
                self.default_points[0][0] += 1; self.default_points[0][1] += 1;
                self.default_points[1][0] -= 1; self.default_points[1][1] += 1;
                self.default_points[2][0] -= 1; self.default_points[2][1] -= 1;
                self.default_points[3][0] += 1; self.default_points[3][1] -= 1;
            else:
                shrink = False
                default = False
                self.rotation *= -1
        else:
            if self.size < self.default_size:
                self.default_points[0][0] -= 1; self.default_points[0][1] -= 1;
                self.default_points[1][0] += 1; self.default_points[1][1] -= 1;
                self.default_points[2][0] += 1; self.default_points[2][1] += 1;
                self.default_points[3][0] -= 1; self.default_points[3][1] += 1;
            else:
                shrink = True
                default = True
                self.rotation = self.default_rotation

        self.update_square(True)
        return shrink, default

    def affine_rotation(self, clockwise=True):
        it = self.rotation
        if clockwise:
            c = math.cos(it*math.pi/36)
            s = math.sin(it*math.pi/36)
        else:
            c = math.cos(-it*math.pi/36)
            s = math.sin(-it*math.pi/36)

        self.ax =int(c*(self.default_points[0][0]-self.mx)*(1) - s*(self.default_points[0][1]-self.my)) + self.mx
        self.ay =int(s*(self.default_points[0][0]-self.mx)*(1) + c*(self.default_points[0][1]-self.my)) + self.my

        self.bx =int(c*(self.default_points[1][0]-self.mx)*(1) - s*(self.default_points[1][1]-self.my)) + self.mx
        self.by =int(s*(self.default_points[1][0]-self.mx)*(1) + c*(self.default_points[1][1]-self.my)) + self.my

        self.cx =int(c*(self.default_points[2][0]-self.mx)*(1) - s*(self.default_points[2][1]-self.my)) + self.mx
        self.cy =int(s*(self.default_points[2][0]-self.mx)*(1) + c*(self.default_points[2][1]-self.my)) + self.my

        self.dx =int(c*(self.default_points[3][0]-self.mx)*(1) - s*(self.default_points[3][1]-self.my)) + self.mx
        self.dy =int(s*(self.default_points[3][0]-self.mx)*(1) + c*(self.default_points[3][1]-self.my)) + self.my

        self.update_square(False)

    def update_square(self, x):
        if x:
            self.points = ((self.ax, self.ay), (self.bx, self.by), (self.cx, self.cy), (self.dx, self.dy))
            w = math.sqrt((math.pow(self.ax-self.bx, 2)) + (math.pow(self.ay - self.by, 2)))
            self.size = pygame.Rect(self.ax, self.ay, w, w).width
        else:
            self.points = ((self.ax, self.ay), (self.bx, self.by), (self.cx, self.cy), (self.dx, self.dy))
            self.rotation += 1


def game(inputs):
    x = int(inputs[0])
    y = int(inputs[1])
    size = int(inputs[2])
    rotation = int(inputs[3])
    limit = int(inputs[4])
    r, g, b = inputs[5].split(',')
    color = (int(r),int(g),int(b))

    rect1 = pygame.Rect(x,y,size,size)
    sq1 = square(rect1, int(rotation/5))


    display.fill((0,0,0))
    sq1.affine_rotation()
    pygame.draw.polygon(display,color, sq1.points)

    shrink = True
    running = True
    default = False

    while running:
        if not default:
            display.fill((0,0,0))
            shrink, default = sq1.affine_scaling(limit, shrink)
            sq1.affine_rotation(shrink)
            if sq1.rotation == sq1.default_rotation+1:
                default = True
            pygame.draw.polygon(display, color, sq1.points)

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu(inputs, active)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    default = False
        # debug


def main_menu(inputs, active):
    click = False
    while True:
        display.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()
        start_button = pygame.Rect(660,550,200,50)
        text_surface = pygame.font.SysFont(None, 50).render('start', True, (255,255,255))
        button_text = text_surface.get_rect()
        button_text.center = (760,575)

        label1 = font.render(':x', True, (255,255,255))
        display.blit(label1, (75,3))
        label2 = font.render(':y', True, (255,255,255))
        display.blit(label2, (75,33))
        label3 = font.render(':ilgis', True, (255,255,255))
        display.blit(label3, (75,63))
        label4 = font.render(':posūkis', True, (255,255,255))
        display.blit(label4, (75,93))
        label5 = font.render(':riba', True, (255,255,255))
        display.blit(label5, (75,123))
        label6 = font.render(':spalva', True, (255,255,255))
        display.blit(label6, (205,153))

        input1 = font.render(inputs[0], True, (255,255,255))
        input1_rect = pygame.Rect(0,3,70,30)
        pygame.draw.rect(display,(255,255,255),input1_rect,2)
        input2 = font.render(inputs[1], True, (255,255,255))
        input2_rect = pygame.Rect(0,33,70,30)
        pygame.draw.rect(display,(255,255,255),input2_rect,2)
        input3 = font.render(inputs[2], True, (255,255,255))
        input3_rect = pygame.Rect(0,63,70,30)
        pygame.draw.rect(display,(255,255,255),input3_rect,2)
        input4 = font.render(inputs[3], True, (255,255,255))
        input4_rect = pygame.Rect(0,93,70,30)
        pygame.draw.rect(display,(255,255,255),input4_rect,2)
        input5 = font.render(inputs[4], True, (255,255,255))
        input5_rect = pygame.Rect(0,123,70,30)
        pygame.draw.rect(display,(255,255,255),input5_rect,2)
        input6 = font.render(inputs[5], True, (255,255,255))
        input6_rect = pygame.Rect(0,153,205,30)
        pygame.draw.rect(display,(255,255,255),input6_rect,2)


        display.blit(input1, (input1_rect.x+5, input1_rect.y))
        display.blit(input2, (input2_rect.x+5, input2_rect.y))
        display.blit(input3, (input3_rect.x+5, input3_rect.y))
        display.blit(input4, (input4_rect.x+5, input4_rect.y))
        display.blit(input5, (input5_rect.x+5, input5_rect.y))
        display.blit(input6, (input6_rect.x+5, input6_rect.y))




        if start_button.collidepoint((mx,my)):
            if click:
                game(inputs)
        click = False
        pygame.draw.rect(display, (180,0,20), start_button)
        display.blit(text_surface, button_text)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    if click:
                        if input1_rect.collidepoint((mx,my)):
                            active[0] = False; active[1] = False; active[2] = False;
                            active[3] = False; active[4] = False; active[5] = False;
                            active[0] = True
                        if input2_rect.collidepoint((mx,my)):
                            active[0] = False; active[1] = False; active[2] = False;
                            active[3] = False; active[4] = False; active[5] = False;
                            active[1] = True
                        if input3_rect.collidepoint((mx,my)):
                            active[0] = False; active[1] = False; active[2] = False;
                            active[3] = False; active[4] = False; active[5] = False;
                            active[2] = True
                        if input4_rect.collidepoint((mx,my)):
                            active[0] = False; active[1] = False; active[2] = False;
                            active[3] = False; active[4] = False; active[5] = False;
                            active[3] = True
                        if input5_rect.collidepoint((mx,my)):
                            active[0] = False; active[1] = False; active[2] = False;
                            active[3] = False; active[4] = False; active[5] = False;
                            active[4] = True
                        if input6_rect.collidepoint((mx,my)):
                            active[0] = False; active[1] = False; active[2] = False;
                            active[3] = False; active[4] = False; active[5] = False;
                            active[5] = True
            if event.type == pygame.KEYDOWN:
                if active[0]:
                    if event.key == pygame.K_BACKSPACE:
                        inputs[0] = inputs[0][:-1]
                    elif len(inputs[0]) < 3:
                        inputs[0] += event.unicode
                if active[1]:
                    if event.key == pygame.K_BACKSPACE:
                        inputs[1] = inputs[1][:-1]
                    elif len(inputs[1]) < 3:
                        inputs[1] += event.unicode
                if active[2]:
                    if event.key == pygame.K_BACKSPACE:
                        inputs[2] = inputs[2][:-1]
                    elif len(inputs[2]) < 3:
                        inputs[2] += event.unicode
                if active[3]:
                    if event.key == pygame.K_BACKSPACE:
                        inputs[3] = inputs[3][:-1]
                    elif len(inputs[3]) < 3:
                        inputs[3] += event.unicode
                if active[4]:
                    if event.key == pygame.K_BACKSPACE:
                        inputs[4] = inputs[4][:-1]
                    elif len(inputs[4]) < 3:
                        inputs[4] += event.unicode
                if active[5]:
                    if event.key == pygame.K_BACKSPACE:
                        inputs[5] = inputs[5][:-1]
                    elif len(inputs[5]) < 11:
                        inputs[5] += event.unicode
        pygame.display.update()
        clock.tick(60)


pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((860,600))
pygame.display.set_caption('...')
font = pygame.font.SysFont(None, 50)
click = False
inputs = ['350', '200', '200', '0', '20', '0,120,0']
active = [False, False, False, False, False, False]

main_menu(inputs, active)

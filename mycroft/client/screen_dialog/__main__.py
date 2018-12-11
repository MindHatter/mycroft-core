
import os
import time

import pygame
from pygame.locals import *

client_directory=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class ScreenFace():

    question = ''
    answer = ''

    WIDTH = 1420
    HEIGHT = 940

    def __init__(self):
        pygame.init()
        infoObject = pygame.display.Info()
        size = self.WIDTH, self.HEIGHT = (infoObject.current_w, infoObject.current_h)
        self.screen = pygame.display.set_mode(size, RESIZABLE)

        # Установить заголовок окна
        pygame.display.set_caption('NIKA')
        directory=os.path.dirname(os.path.realpath(__file__))
        #self.avatar = pygame.image.load(directory+'/gorodgeroev.jpg')
        self.clock=pygame.time.Clock()
        self.font = pygame.font.Font(directory+'/font.otf', 100)
        os.environ["SDL_VIDEODRIVER"] = "x11"

    def contunue_game_loop(self):
        while True:
            try:
                self.refresh()
                time.sleep(0.3)
            except KeyboardInterrupt as e:
                self.close_window()

    def update_question(self):
        try:
            with open(client_directory + '/question', 'r') as file:
                utterance = file.read()
                self.question = utterance
        except Exception as e:
            self.question = str(e)

    def update_answer(self):
        try:
            with open(client_directory + '/answer', 'r') as file:
                utterance = file.read()
                self.answer = utterance
        except Exception as e:
            self.answer =str(e)

    def refresh(self):
        self.update_answer()
        self.update_question()
        self.__refresh()
        self.__refresh()

    def __refresh(self):
        # Пользователь что-то сделал
        for event in pygame.event.get():
            # Реагируем на действия пользователя
            if event.type == pygame.QUIT:
                self.close_window()

        # Тут можно рисовать
        green = (0, 128, 0)   # зеленый
        white = (255, 255, 255)   # белый
        black = (0, 0, 0)  # белый
        gray = (27, 28, 31)  # белый
        blue = (147, 165, 191)

        self.screen.fill(white)
        #self.screen.blit(self.avatar, (1, 1))
        # set_question
        rect_x1, rect_y1, rect_x2, rect_y2 = self.blit_text(self.screen, self.question,
                                                            (self.WIDTH/6, self.HEIGHT/10),
                                                            self.font, white)
        self.draw_rect(self.screen, rect_x1, rect_y1, rect_x2, rect_y2, blue)
        rect_x1, rect_y1, rect_x2, rect_y2 = self.blit_text(self.screen, self.question,
                                                            (self.WIDTH /6, self.HEIGHT /10),
                                                            self.font, white)

        # set_answer
        rect_x1, rect_y1, rect_x2, rect_y2 = self.blit_text(self.screen, self.answer,
                                                            (self.WIDTH/8, self.HEIGHT/2),
                                                            self.font, gray)
        self.draw_rect(self.screen, rect_x1, rect_y1, rect_x2, rect_y2, green)
        rect_x1, rect_y1, rect_x2, rect_y2 = self.blit_text(self.screen, self.answer,
                                                            (self.WIDTH /8, self.HEIGHT /2),
                                                            self.font, gray)
        # Рисунок появится после обновления экрана
        pygame.display.flip()
        self.clock.tick(30)


    def close_window(self):
        pygame.quit()
        quit()

    def blit_text(self, surface, text, pos, font,
                  color=pygame.Color('black'),
                  rect_margin = 10) -> []:
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        max_width = max_width - pos[0]
        x, y = start_x, start_y = pos
        max_x, max_y = 0, 0
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                max_x = max(x+word_width, max_x)
                max_y = max(y+word_height, max_y)
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

        return start_x - rect_margin, start_y-rect_margin, max_x-start_x + rect_margin*2, max_y-start_y + rect_margin*2


    def draw_rect(self, surface, x, y, width, height, color = pygame.Color('white')):
        surf1 = pygame.Surface((width, height))
        surf1.fill(color)  # желтая
        rect = pygame.Rect([x,
                            y,
                           width,
                           height
                            ])
        surface.blit(surf1, rect)

def main():
    lb = ScreenFace()
    lb.contunue_game_loop()


if __name__ == "__main__":
    main()

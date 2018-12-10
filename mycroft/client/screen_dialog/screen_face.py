import os
import time

import pygame
from pygame.rect import Rect


class ScreenFace():

    question = ''
    answer = ''

    def __init__(self):
        pygame.init()
        size = WIDTH, HEIGHT = (1024, 720)
        self.screen = pygame.display.set_mode(size)

        # Установить заголовок окна
        pygame.display.set_caption('NIKA')
        directory=os.path.dirname(os.path.realpath(__file__))
        #self.avatar = pygame.image.load(directory+'/gorodgeroev.jpg')
        self.clock=pygame.time.Clock()

    def set_question(self, text):
        self.question = text

    def set_answer(self, text):
        self.answer = text

    def refresh(self):
        self.__refresh()
        self.__refresh()

    def __refresh(self):
        # Пользователь что-то сделал
        for event in pygame.event.get():
            # Реагируем на действия пользователя
            if event.type == pygame.QUIT:
                self.close_window()

        # Тут можно рисовать
        fontObj = pygame.font.Font('./12890.otf', 90)
        green = (0, 128, 0)   # зеленый
        white = (255, 255, 255)   # белый

        self.screen.fill(white)
        #self.screen.blit(self.avatar, (1, 1))
        # set_question
        self.blit_text(self.screen, self.question, (100, 100), fontObj,green)
        # set_answer
        self.blit_text(self.screen, self.answer, (100, 250), fontObj, green)

        # Рисунок появится после обновления экрана
        pygame.display.flip()
        self.clock.tick(30)


    def close_window(self):
        pygame.quit()
        quit()

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        max_width = max_width - pos[0]
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

if __name__ == '__main__':
    lb=ScreenFace()
    for i in range(5):
        lb.set_question('Привет, Ника')
        lb.set_answer('Привет, кожанный')
        lb.refresh()
        time.sleep(10)

    lb.close_window()
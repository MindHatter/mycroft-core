
import os
import time

import pygame
from pygame.locals import *

client_directory=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class ScreenFace():


    dialog = []

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
        self.font = pygame.font.Font(directory+'/font.otf', 80)
        os.environ["SDL_VIDEODRIVER"] = "x11"

    def contunue_game_loop(self):
        while True:
            try:
                self.refresh()
                time.sleep(0.3)
            except KeyboardInterrupt as e:
                self.close_window()

    def update_dialog(self):
        try:
            with open(client_directory + '/dialog', 'r') as file:
                self.dialog = str(file.read()).split('\n')
        except Exception as e:
            self.dialog.append(str(e))

    def refresh(self):
        self.update_dialog()
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

        HEIGHT_PADDING = 40
        WIDTH_PADDING = 40
        RECT_PADDING = 5
        phrase_count = 0

        current_y = self.HEIGHT
        for phrase in self.dialog[::-1]:
            phrase_count = phrase_count + 1
            if not phrase.startswith('>>'):
                 rect_color = blue
                 text_color = white
                  #set_question
            else:
                rect_color = green
                text_color = gray
                    # set_answer
            rect_width, rect_height = self.__get_size(self.screen, phrase, WIDTH_PADDING, HEIGHT_PADDING, self.font)
            current_y = current_y - rect_height - HEIGHT_PADDING
            self.draw_rect(self.screen, WIDTH_PADDING-RECT_PADDING, current_y-RECT_PADDING, rect_width+2*RECT_PADDING, rect_height+2*RECT_PADDING, rect_color)
            self.__blit_text(self.screen, phrase, (WIDTH_PADDING, current_y), self.font, text_color, 10, HEIGHT_PADDING)
        # Рисунок появится после обновления экрана
        pygame.display.flip()
        self.clock.tick(30)


    def close_window(self):
        pygame.quit()
        quit()

    def __blit_text(self, surface, text, pos, font,
                  color=pygame.Color('black'),
                  x_margin = 10, y_margin = 10) -> []:
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

        return start_x - x_margin, start_y-y_margin, max_x-start_x + x_margin*2, max_y-start_y + y_margin*2

    def __get_size(self, surface, text, x_margin, y_margin, font) -> ():
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        max_width = max_width - x_margin
        x, y = x_margin, y_margin
        max_x, max_y = 0, 0
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, (0, 0, 0))
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = x_margin  # Reset the x.
                    y += word_height  # Start on new row.
                max_x = max(x+word_width, max_x)
                max_y = max(y+word_height, max_y)
                x += word_width + space
            x = x_margin  # Reset the x.
            y += word_height  # Start on new row.

        return (max_x-x_margin, max_y-y_margin)


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

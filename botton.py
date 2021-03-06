# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:55:48 2020

@author: Филипп
"""
import pygame as pg

pg.init()

class Botton():
    """Класс кнопки.
    """
    def __init__(self, screen, coords, width, height, color, text):
        
        self.screen = screen
        """Холст, на котором размещается кнопка."""
        
        self.coords = coords
        """Координаты верхнего левого угла кнопки на экране."""
        
        self.height = height
        """Высота кнопки."""
        
        self.width = width
        """Ширина кнопки."""
        
        self.color = color
        """Цвет кнопки."""
        
        self.text = text
        """Текст кнопки."""
        
        self.font = pg.font.SysFont("dejavusansmono", 25)
        """Шрифт текста кнопки."""
        
        
    def draw(self):
        """Функция, отрисовывающая кнопку.
        """
        ltop_corner = (self.coords[0] - int(self.width / 2), 
                       self.coords[1] - int(self.height / 2))
        pg.draw.rect(self.screen, self.color, (ltop_corner[0], ltop_corner[1],
                    self.width, self.height))
        botton_text = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(botton_text, (ltop_corner[0], self.coords[1]))
        
    
    def click(self, mouse_coord):
        """
        Функция, регистрирующая нажатие на кнопку.

        Parameters
        ----------
        mouse_coord : list
            Координаты мыши при щелчке.

        Returns
        -------
        bool
            Произошло ли нажатие на кнопку.

        """
        if (mouse_coord[0] >= self.coords[0] - self.width / 2) & (
            mouse_coord[0] <= self.coords[0] + self.width / 2) & (
            mouse_coord[1] >= self.coords[1] - self.height / 2) & (
            mouse_coord[1] <= self.coords[1] + self.height / 2):
                    return True
        else:
            return False
        
        
class Botton_image():
    """Класс кнопки. Использует изображение для отображения кнопки.
    """
    def __init__(self, screen, coords, filename, botton_form):
        
        self.screen = screen
        """Холст, на котором размещается кнопка."""
        
        self.image = pg.image.load(filename).convert_alpha()
        """Изображение кнопки."""
        
        self.coords = coords
        """Координаты верхнего левого угла изображения кнопки на экране."""
        
        self.rad = self.image.get_width()/2
        """Радиус кнопки, если она круглая."""
        
        self.width = self.image.get_width()
        """Ширина кнопки."""
        
        self.height = self.image.get_height()
        """Высота кнопки."""
        
        self.botton_form = botton_form
        """Форма кнопки: круглая или прямоугольная."""
        
        
    def draw(self):
        """Функция, отрисовывающая кнопку.
        """
        self.rect = self.image.get_rect(center=(self.coords[0], self.coords[1]))
        self.screen.blit(self.image, self.rect)
        
    
    def click(self, mouse_coord):
        """
        Функция, регистрирующая нажатие на кнопку.

        Parameters
        ----------
        mouse_coord : list
            Координаты мыши при щелчке.

        Returns
        -------
        bool
            Произошло ли нажатие на кнопку.

        """
        if self.botton_form == "circle":    
            if (mouse_coord[0] - self.coords[0])**2 + (mouse_coord[1] - self.coords[1])**2 <= self.rad**2:
                        return True
            else:
                return False
        if self.botton_form == "rect":  
            if (mouse_coord[0] >= self.coords[0] - self.width / 2) & (
                mouse_coord[0] <= self.coords[0] + self.width / 2) & (
                mouse_coord[1] >= self.coords[1] - self.height / 2) & (
                mouse_coord[1] <= self.coords[1] + self.height / 2):
                        return True
            else:
                return False        
    
    

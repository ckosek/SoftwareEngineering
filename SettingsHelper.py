import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import pygame as pg
import pygame_menu as pm
from pygame_menu import sound

#Color List for quick reference
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIME = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
SILVER = (192,192,192)
GRAY = (128,128,128)
MAROON = (128,0,0)
OLIVE = (128,128,0)
GREEN = (0,128,0)
PURPLE = (128,0,128)
TEAL = (0,128,128)
NAVY = (0,0,128)


class Settings_Helper:

	def __init__(self):
		return self

	#Method: Creates the theme used for all menus
	def set_theme(back_color, color):
		pg.init()
		screen_res = pg.display.Info()
		w = screen_res.current_w
		new_w_offset = w/2 - len("The Ship Predicament")/0.0625

		eight_bit_font = pm.font.FONT_8BIT
		title_theme = pm.widgets.MENUBAR_STYLE_NONE
		font_size = 37
		select_box_color = WHITE
		if back_color == WHITE:
			select_box_color = BLACK
		
		current_theme = pm.themes.Theme(background_color=back_color, widget_font=eight_bit_font, title_bar_style=title_theme, 
								menubar_close_button=True, title_font=eight_bit_font, title_font_color=color, 
								title_font_size=font_size, title_offset=(new_w_offset,0), selection_color=select_box_color)
		return current_theme

	#Method: Creates the sound engine used with menus and gameplay
	def create_sound_engine():
		engine = sound.Sound()
		engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, sound.SOUND_EXAMPLE_CLICK_MOUSE)
		engine.set_sound(sound.SOUND_TYPE_CLOSE_MENU, sound.SOUND_EXAMPLE_CLOSE_MENU)
		engine.set_sound(sound.SOUND_TYPE_ERROR, sound.SOUND_EXAMPLE_ERROR)
		engine.set_sound(sound.SOUND_TYPE_EVENT, sound.SOUND_EXAMPLE_EVENT)
		engine.set_sound(sound.SOUND_TYPE_EVENT_ERROR, sound.SOUND_EXAMPLE_EVENT_ERROR)
		engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION, sound.SOUND_EXAMPLE_KEY_ADD)
		engine.set_sound(sound.SOUND_TYPE_KEY_DELETION, sound.SOUND_EXAMPLE_KEY_DELETE)
		engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, sound.SOUND_EXAMPLE_OPEN_MENU)
		engine.set_sound(sound.SOUND_TYPE_WIDGET_SELECTION, sound.SOUND_EXAMPLE_WIDGET_SELECTION)
		return engine
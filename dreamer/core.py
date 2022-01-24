import json
from typing import Dict, NoReturn

import pygame as pg

# from pong.assets import FontAssets, SFXAssets
from dreamer.colors import GREEN, WHITE, BLACK
from dreamer.const import HEIGHT, WIDTH, FPS
from dreamer.helper import resource_path
# from pong.scenes.scene_manager import SceneManager


class GameCore:
    def __init__(self):
        # init game
        pg.init()
        pg.display.set_caption("dreamer")
        # pg.display.set_icon(pg.image.load('assets/icon/icon.png'))
        self.clock = pg.time.Clock()
        # conf
        self.conf = self.read_config()
        # assets
        # self.font_assets = FontAssets()
        # self.sfx_assets = SFXAssets(self.conf.get('volume', 1.0))
        # screen
        self.screen_mode = pg.FULLSCREEN if self.conf.get('fullscreen') else 0
        self.screen = pg.display.set_mode(size=(WIDTH, HEIGHT), flags=0)
        pg.event.get()  # get pg event and apply screen settings to avoid open lag on macOS
        self.screen = pg.display.set_mode(size=(WIDTH, HEIGHT), flags=self.screen_mode)
        # init scenes
        # self.scene = SceneManager(self)
        # self.scene.load(scene_name='main_menu', wait_for_key_up=False)
        self.playground()

    @staticmethod
    def read_config() -> Dict:
        with open(resource_path('config/config.json'), 'r') as json_conf:
            conf = json.load(json_conf)
            return conf

    def write_config(self) -> NoReturn:
        with open(resource_path('config/config.json'), 'w') as json_conf:
            json.dump(self.conf, json_conf)

    def _debug(self, *args, **kwargs):
        font = pg.font.SysFont('arial', 24)
        info_text = font.render(str(args), False, GREEN)
        info_rect = info_text.get_rect()
        info_rect.topleft = (0, 0)
        self.screen.blit(info_text, info_rect)
        for i in range(0, WIDTH, 10):
            pg.draw.line(self.screen, WHITE, [i, 0], [i, HEIGHT], 1 if i % 50 else 3)
        for i in range(0, HEIGHT, 10):
            pg.draw.line(self.screen, WHITE, [0, i], [WIDTH, i], 1 if i % 50 else 3)

    def playground(self):
        running = True
        self.screen.fill(BLACK)
        while running:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            pg.display.flip()
        pg.quit()
        quit()

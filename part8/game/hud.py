
import pygame as pg
from .utils import draw_text


class Hud:

    def __init__(self, resource_manager, width, height):

        self.resource_manager = resource_manager
        self.width = width
        self.height = height

        self.hud_colour = (198, 155, 93, 175)

        # resouces hud
        self.resouces_surface = pg.Surface((width, height * 0.02), pg.SRCALPHA)
        self.resources_rect = self.resouces_surface.get_rect(topleft=(0, 0))
        self.resouces_surface.fill(self.hud_colour)

        # building hud
        self.build_surface = pg.Surface((width * 0.15, height * 0.25), pg.SRCALPHA)
        self.build_rect = self.build_surface.get_rect(topleft=(self.width * 0.84, self.height * 0.74))
        self.build_surface.fill(self.hud_colour)

        # select hud
        self.select_surface = pg.Surface((width * 0.3, height * 0.2), pg.SRCALPHA)
        self.select_rect = self.select_surface.get_rect(topleft=(self.width * 0.35, self.height * 0.79))
        self.select_surface.fill(self.hud_colour)

        self.images = self.load_images()
        self.tiles = self.create_build_hud()

        self.selected_tile = None
        self.examined_tile = None

    def create_build_hud(self):

        render_pos = [self.width * 0.84 + 10, self.height * 0.74 + 10]
        object_width = self.build_surface.get_width() // 5

        tiles = []

        for image_name, image in self.images.items():

            pos = render_pos.copy()
            image_tmp = image.copy()
            image_scale = self.scale_image(image_tmp, w=object_width)
            rect = image_scale.get_rect(topleft=pos)

            tiles.append(
                {
                    "name": image_name,
                    "icon": image_scale,
                    "image": self.images[image_name],
                    "rect": rect,
                    "affordable": True
                }
            )

            render_pos[0] += image_scale.get_width() + 10

        return tiles

    def update(self):

        mouse_pos = pg.mouse.get_pos()
        mouse_action = pg.mouse.get_pressed()

        if mouse_action[2]:
            self.selected_tile = None

        for tile in self.tiles:
            if self.resource_manager.is_affordable(tile["name"]):
                tile["affordable"] = True
            else:
                tile["affordable"] = False
            if tile["rect"].collidepoint(mouse_pos) and tile["affordable"]:
                if mouse_action[0]:
                    self.selected_tile = tile

    def draw(self, screen):

        # resouce hud
        screen.blit(self.resouces_surface, (0, 0))
        # build hud
        screen.blit(self.build_surface, (self.width * 0.84, self.height * 0.74))
        # select hud
        if self.examined_tile is not None:
            w, h = self.select_rect.width, self.select_rect.height
            screen.blit(self.select_surface, (self.width * 0.35, self.height * 0.79))
            img = self.examined_tile.image.copy()
            img_scale = self.scale_image(img, h=h*0.7)
            screen.blit(img_scale, (self.width * 0.35 + 10, self.height * 0.79 + 40))
            draw_text(screen, self.examined_tile.name, 40, (255, 255, 255), self.select_rect.topleft)

        for tile in self.tiles:
            icon = tile["icon"].copy()
            if not tile["affordable"]:
                icon.set_alpha(100)
            screen.blit(icon, tile["rect"].topleft)

        # resources
        pos = self.width - 400
        for resource, resource_value in self.resource_manager.resources.items():
            txt = resource + ": " + str(resource_value)
            draw_text(screen, txt, 30, (255, 255, 255), (pos, 0))
            pos += 100

    def load_images(self):

        # read images
        lumbermill = pg.image.load("assets/graphics/building01.png")
        stonemasonry = pg.image.load("assets/graphics/building02.png")

        images = {
            "lumbermill": lumbermill,
            "stonemasonry": stonemasonry
        }

        return images

    def scale_image(self, image, w=None, h=None):

        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pg.transform.scale(image, (int(w), int(h)))
        elif w == None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pg.transform.scale(image, (int(w), int(h)))
        else:
            image = pg.transform.scale(image, (int(w), int(h)))

        return image


from pygame.math import Vector2

# Screen Properties
Screen_Width = 1280
Screen_Height = 720
Tile_Size = 64

# Overlay Locations
Overlay_Locations = {
    'tool': (40, Screen_Height - 15),
    'seed': (70, Screen_Height - 5)
}

Player_Tool_Position = {
    'left': Vector2(-50, 40),
    'right': Vector2(50, 40),
    'up': Vector2(0, -10),
    'down': Vector2(0, 50)
}

# Layering levels for the graphics
Terrain_Layers = {
    'water': 0,
    'ground': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'rain drops': 10
}

Apple_POS = {

}

# Rate of plant growth
Grow_Speed = {
    'corn': 0,
    'tomato': 0
}

# Value of items when sold
Sale_Values = {
    'wood': 0,
    'apple': 0,
    'corn': 0,
    'tomato': 0
}

# Value of items when purchased
Purchase_Values = {
    'corn': 0,
    'tomato': 0
}
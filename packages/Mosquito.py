import pygame

class Mosquito:
    def __init__(self, position):
        self.size = (100,100)
        self.type = 'normal'
        self.apreared_image_path = ""
        self.crushed_image_path = ""
        self.crushed_sound_path = ""
        self.position = position


    def getCrushedSound(self):
        return self.crushed_sound

    def getPosition(self):
        return self.crushed_image_path
    
    def image(self):
        return self.apreared_image_path


        
    

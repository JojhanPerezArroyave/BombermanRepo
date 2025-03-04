from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from core.model import BombermanModel
from agents.bomberman import Bomberman
from agents.rock import Rock
from agents.metal import Metal

def agent_portrayal(agent):
    portrayal = {"Shape": "rect", "Filled": "true", "Layer": 0}
    
    if isinstance(agent, Bomberman):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "blue"
        portrayal["r"] = 0.8
    
    elif isinstance(agent, Rock):
        portrayal["Color"] = "brown"
        portrayal["w"] = 1
        portrayal["h"] = 1
    
    elif isinstance(agent, Metal):
        portrayal["Color"] = "gray"
        portrayal["w"] = 1
        portrayal["h"] = 1
    
    return portrayal

grid = CanvasGrid(agent_portrayal, 7, 7, 500, 500)
server = ModularServer(BombermanModel, [grid], "Bomberman Model", {"width": 7, "height": 7, "map_file": "data/map.txt"})
server.port = 8521
server.launch()

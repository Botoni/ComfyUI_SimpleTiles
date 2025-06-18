from .standard import TileSplit, TileMerge, TileCalc
from .dynamic import DynamicTileSplit, DynamicTileMerge

NODE_CLASS_MAPPINGS = {
    "TileSplit": TileSplit,
    "TileMerge": TileMerge,
    "TileCalc": TileCalc,
    "DynamicTileSplit": DynamicTileSplit,
    "DynamicTileMerge": DynamicTileMerge,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TileSplit": "TileSplit (Legacy)",
    "TileMerge": "TileMerge (Legacy)",
    "TileCalc": "TileCalc (Legacy)",
    "DynamicTileSplit": "TileSplit (Dynamic)",
    "DynamicTileMerge": "TileMerge (Dynamic)",
}

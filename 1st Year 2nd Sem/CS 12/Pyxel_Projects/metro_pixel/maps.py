from dataclasses import dataclass
import importlib

@dataclass(frozen=True)
class MapInfo:
    map_id : str
    name : str
    module_name : str
    thumbnail: str | None = None

    def load_data(self):
        return importlib.import_module(self.module_name)

MAP_REGISTRY : dict[str, MapInfo] = {
    "ncr" : MapInfo(
        map_id="ncr",
        name = "Metro Manila (NCR)",
        module_name= "map_packs.map_data_ncr",
        thumbnail= "480_270_PhNcr.png"
        )

    }
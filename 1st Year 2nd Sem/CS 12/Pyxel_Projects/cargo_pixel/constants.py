from enum import Enum

class ShipType(Enum):
	Tugboat = {
		"name" : "Tugboat",
		"hp" : 100, 
		"speed" : 100, 
		"cargo" : 50, 
		"fuel" : 100, 
		"min_lvl_req" : 0}
	Mini_Bulk_Carriers = {
		"name" : "Mini-Bulk Carriers",
		"hp" : 100, 
		"speed" : 100, 
		"cargo" : 50, 
		"fuel" : 100, 
		"min_lvl_req" : 0}
	Roro = {
		"name" : "RORO Ship",
		"hp" : 100, 
		"speed" : 100, 
		"cargo" : 50, 
		"fuel" : 100, 
		"min_lvl_req" : 0}
	Super_Tanker = {
		"name" : "Super Tanker",
		"hp" : 100, 
		"speed" : 100, 
		"cargo" : 50, 
		"fuel" : 100, 
		"min_lvl_req" : 0}

Level_to_Ship = {
	0 : ShipType.Tugboat,
	1 : ShipType.Mini_Bulk_Carriers,
	2 : Roro,
	3 : Super_Tanker
}

class ShipToTile(IntEnum):
	Tugboat = (0,8),
	Mini_Bulk_Carriers = (8, 8),
	Roro = (16, 8),
	Super_Tanker = (24, 8)


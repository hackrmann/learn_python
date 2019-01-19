# import networkx as nx
pantagonia_bus = {
    "title": "pantagonia bus",
    "created_by": "Colt Steele",
    "a": {
        "album": "hello",
        "len": 120
    },
    "b": dict(album="mellow",len=240),
    "c": dict([("album","jello"),("len",250),(5,5)]),
    "dummyList": []

}
pantagonia_bus["dummyList"].extend([3,4,5])
for ke,val in pantagonia_bus.items():
    print(ke,"\t",val)
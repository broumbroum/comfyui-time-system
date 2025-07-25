import datetime

class SecondTimeNode:
    
    def __init__(self):
        pass
        
     
    @classmethod    
    def INPUT_TYPES(s):
        return {}
    RETURN_TYPES = ("STRING","INT")
    RETURN_NAMES = ("Second","Second_int")
    
    FUNCTION = "Second"
    
    CATEGORY = "TimeSystem"
    
    def Second(self):
        dt = datetime.datetime.now().strftime("%S")
        i = int(datetime.datetime.now().strftime("%S"))
        return (dt,i)
    
NODE_CLASS_MAPPINGS = {
    "SecondTimeNode" : SecondTimeNode,
}

# Optionally, you can rename the node in the `NODE_DISPLAY_NAME_MAPPINGS` dictionary.
NODE_DISPLAY_NAME_MAPPINGS = {
    "SecondTimeNode": "SecondTimeNode",
}
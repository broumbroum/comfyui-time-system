import datetime

class MonthTimeNode:
    
    def __init__(self):
        pass
        
     
    @classmethod    
    def INPUT_TYPES(s):
        return {}
    RETURN_TYPES = ("STRING","INT")
    RETURN_NAMES = ("Month","Month_int")
    
    FUNCTION = "Month"
    
    CATEGORY = "TimeSystem"
    
    def Month(self):
        dt = datetime.datetime.now().strftime("%m")
        i = int(datetime.datetime.now().strftime("%m"))
        return (dt,i)
    
NODE_CLASS_MAPPINGS = {
    "MonthTimeNode" : MonthTimeNode,
}

# Optionally, you can rename the node in the `NODE_DISPLAY_NAME_MAPPINGS` dictionary.
NODE_DISPLAY_NAME_MAPPINGS = {
    "MonthTimeNode": "MonthTimeNode",
}
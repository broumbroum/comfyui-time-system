import datetime

class DayTimeNode:
    
    def __init__(self):
        pass
        
     
    @classmethod    
    def INPUT_TYPES(s):
        return {}
    RETURN_TYPES = ("STRING","INT")
    RETURN_NAMES = ("Day","Day_int")
    
    FUNCTION = "Day"
    
    CATEGORY = "TimeSystem"
    
    def Day(self):
        dt = datetime.datetime.now().strftime("%d")
        i = int(datetime.datetime.now().strftime("%d"))
        return (dt,i)
    
NODE_CLASS_MAPPINGS = {
    "DayTimeNode" : DayTimeNode,
}

# Optionally, you can rename the node in the `NODE_DISPLAY_NAME_MAPPINGS` dictionary.
NODE_DISPLAY_NAME_MAPPINGS = {
    "DayTimeNode": "DayTimeNode",
}
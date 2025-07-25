import datetime

class HourTimeNode:
    
    def __init__(self):
        pass
        
     
    @classmethod    
    def INPUT_TYPES(s):
        return {}
    RETURN_TYPES = ("STRING","INT")
    RETURN_NAMES = ("Hour","Hour_int")
    
    FUNCTION = "Hour"
    
    CATEGORY = "TimeSystem"
    
    def Hour(self):
        dt = datetime.datetime.now().strftime("%H")
        i = int(datetime.datetime.now().strftime("%H"))
        return (dt,i)
    
NODE_CLASS_MAPPINGS = {
    "HourTimeNode" : HourTimeNode,
}

# Optionally, you can rename the node in the `NODE_DISPLAY_NAME_MAPPINGS` dictionary.
NODE_DISPLAY_NAME_MAPPINGS = {
    "HourTimeNode": "HourTimeNode",
}
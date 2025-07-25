import datetime

class MinuteTimeNode:
    
    def __init__(self):
        pass
        
     
    @classmethod    
    def INPUT_TYPES(s):
        return {}
    RETURN_TYPES = ("STRING","INT")
    RETURN_NAMES = ("Minute","Minute_int")
    
    FUNCTION = "Minute"
    
    CATEGORY = "TimeSystem"
    
    def Minute(self):
        dt = datetime.datetime.now().strftime("%M")
        i = int(datetime.datetime.now().strftime("%M"))
        return (dt,i)
    
NODE_CLASS_MAPPINGS = {
    "MinuteTimeNode" : MinuteTimeNode,
}

# Optionally, you can rename the node in the `NODE_DISPLAY_NAME_MAPPINGS` dictionary.
NODE_DISPLAY_NAME_MAPPINGS = {
    "MinuteTimeNode": "MinuteTimeNode",
}
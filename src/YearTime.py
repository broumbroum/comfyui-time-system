import datetime

class YearTimeNode:
    
    def __init__(self):
        pass
        
     
    @classmethod    
    def INPUT_TYPES(s):
        return {}
    RETURN_TYPES = ("STRING","INT")
    RETURN_NAMES = ("Year","Year_int")
    
    FUNCTION = "Year"
    
    CATEGORY = "TimeSystem"
    
    def Year(self):
        dt = datetime.datetime.now().strftime("%Y")
        i = int(datetime.datetime.now().strftime("%Y"))
        return (dt,i)
    
NODE_CLASS_MAPPINGS = {
    "YearTimeNode" : YearTimeNode,
}

# Optionally, you can rename the node in the `NODE_DISPLAY_NAME_MAPPINGS` dictionary.
NODE_DISPLAY_NAME_MAPPINGS = {
    "YearTimeNode": "YearTimeNode",
}
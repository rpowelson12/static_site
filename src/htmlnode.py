

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        pass

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        # Now you need to convert each key-value pair to a string
        # and join them together with spaces
        # Don't forget the leading space!
        
        # Return the formatted string
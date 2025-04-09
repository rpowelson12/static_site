from textnode import TextType, TextNode

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        formatted_props = []
        # Now you need to convert each key-value pair to a string
        for key, value in self.props.items():
            formatted_props.append(f'{key}="{value}"')

        # and join them together with spaces
        formatted_string = " " + " ".join(formatted_props)
        # Don't forget the leading space!
        # Return the formatted string
        return formatted_string

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=None)
    
    def to_html(self):
        ## Value Checks
        if not self.tag:
            raise ValueError("ParentNode needs a tag value")
        if not self.children:
            raise ValueError("Every ParentNode needs children")
        
        #Children Loops and HTML building
        html_parts = [child.to_html() for child in self.children]
        html = ''.join(html_parts)
        return f"<{self.tag}>{html}</{self.tag}>"

def text_node_to_html_node(text_node):
    type = text_node.TextType
    value = text_node.text 

    if type == TextType.TEXT:
        return LeafNode(None, value)
    elif type == TextType.BOLD:
        return LeafNode("b",value)
    elif type == TextType.CODE:
        return LeafNode('code', value)
    elif type == TextType.IMAGE:
        return LeafNode('img', "", {"src": text_node.url, "alt":value})
    elif type == TextType.ITALIC:
        return LeafNode('i', value)
    elif type == TextType.LINK:
        return LeafNode('a', value, {"href": text_node.url})
    else: 
        raise ValueError(f'Invalid text type: {type}')
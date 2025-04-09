from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for item in old_nodes:
        if item.text_type != TextType.TEXT:
            new_list.append(item)
            continue
        
        text = item.text 

        while delimiter in text:
            first_delimiter = text.find(delimiter)
            if first_delimiter > 0:
                new_list.append(TextNode(text[:first_delimiter], TextType.TEXT))
            last_delimiter = text.find(delimiter, first_delimiter + len(delimiter))
            if last_delimiter == -1:
                raise Exception(f"No closing delimiter found for {delimiter}")
            
            content = text[first_delimiter + len(delimiter):last_delimiter]
            new_list.append(TextNode(content, text_type))

            text = text[last_delimiter + len(delimiter):]
        
        # Add any remaining text after all delimiter pairs
        if text:
            new_list.append(TextNode(text, TextType.TEXT))
    
    return (new_list)
        
        

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
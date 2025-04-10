

import re

from textnode import TextNode, TextType


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)    

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)

        if not images:
            result.append(old_node)
            continue

        current_text = old_node.text 

        for img_text, img_url in images:
            markdown_image = f'![{img_text}]({img_url})'

            parts = current_text.split(markdown_image, 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
                
            result.append(TextNode(img_text, TextType.IMAGE, img_url))

            if len(parts) > 1:
                current_text = parts[1]

        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
    
    return result
   
    
def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        links = extract_markdown_links(old_node.text)

        if not links:
            result.append(old_node)
            continue

        current_text = old_node.text

        for link_text, link_url in links:
            markdown_link = f"[{link_text}]({link_url})"

            parts = current_text.split(markdown_link, 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
            
            result.append(TextNode(link_text, TextType.LINK, link_url))

            if len(parts) > 1:
                current_text = parts[1]

        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))

    return result


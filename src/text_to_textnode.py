from regex_extraction import split_nodes_image, split_nodes_link
from markdown_to_text import split_nodes_delimiter
from textnode import TextType, TextNode

def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]
    bolded = split_nodes_delimiter(text_node, "**", TextType.BOLD)
    italics = split_nodes_delimiter(bolded, "_", TextType.ITALIC)
    coded = split_nodes_delimiter(italics, "`", TextType.CODE)
    images = split_nodes_image(coded)
    links = split_nodes_link(images)
    return links


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
text_to_textnodes(text)
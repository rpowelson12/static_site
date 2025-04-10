import unittest

from htmlnode import text_node_to_html_node
from markdown_to_text import split_nodes_delimiter
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        

    def test_not_eq(self):
        node = TextNode("this is an image", TextType.IMAGE)
        node2 = TextNode("image", TextType.IMAGE)
        self.assertNotEqual(node, node2)
    
    def test_eq(self):
        node3 = TextNode("Another Node", TextType.CODE)
        node4 = TextNode("Another Node", TextType.CODE) 
        self.assertEqual(node3, node4)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("this is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "this is a bold node")

    def test_image(self):
        node = TextNode("this is an image node", TextType.IMAGE, {'href': 'google.com'})
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.props, {'src': {'href': 'google.com'}, 'alt': 'this is an image node'})

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        expected = [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                ]
           
        

        actual = text_to_textnodes(text)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
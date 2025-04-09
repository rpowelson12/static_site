import unittest

from htmlnode import text_node_to_html_node
from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
import unittest

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


if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        # Create an HTMLNode with some props
        node = HTMLNode(tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        
        # Call the method and store the output
        actual_output = node.props_to_html()
        
        # Expected output
        expected_output = ' href="https://www.example.com" target="_blank"'
        
        # Use assertEqual to check if actual matches expected
        self.assertEqual(actual_output, expected_output)

    def test_empty_dict(self):
        node = HTMLNode(props={})
        actual_output = node.props_to_html()

        expected_output = ""

        self.assertEqual(actual_output, expected_output)

    def test_none_props(self):

        node = HTMLNode(props=None)
        actual_output = node.props_to_html()

        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me</a>')

import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div", 
            "Hello, world!", 
            None, 
            {"class": "greeting", "id": "main"}
        )
        self.assertEqual(
            node.props_to_html(), 
            ' class="greeting" id="main"'
        )

    def test_values(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("a", "link", None, {"href": "https://google.com"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(a, link, children: None, {'href': 'https://google.com'})"
        )

if __name__ == "__main__":
    unittest.main()

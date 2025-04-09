from textnode import TextNode, TextType

def main():
    test = TextNode("this is some dummy data", TextType.LINK, "https://www.google.com")
    print(test)

main()
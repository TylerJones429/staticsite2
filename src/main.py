from textnode import TextNode, TextType


def main():
    node = TextNode("This is a test node", TextType.BOLD, "www.boot.dev")
    print (node)


main()
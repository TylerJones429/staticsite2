from textnode import TextNode, TextType

def main():
    test_node = TextNode("This is a test node", TextType.BOLD, "www.boot.dev")
    print (test_node)

main()
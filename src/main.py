from textnode import TextNode, TextType


def main():
    node = TextNode("This is my site", TextType.LINK, "https://kozykoding.com")
    print(node)


if __name__ == "__main__":
    main()

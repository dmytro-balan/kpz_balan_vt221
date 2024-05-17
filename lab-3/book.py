from LightHTML import LightElementNode
from LightHTML import LightTextNode
class LightHTML:
    def __init__(self):
        self.root = None
        self.total_nodes = 0

    def parse_text_to_html(self, text):
        lines = text.split('\n')
        self.root = self.parse_lines(lines)

    def parse_lines(self, lines):
        root = None
        current_parent = None
        for line in lines:
            line = line.strip()
            if len(line) < 20:
                node = LightElementNode('h2')
            elif line.startswith(' '):
                node = LightElementNode('blockquote')
            else:
                node = LightElementNode('p')
            node.add_child(LightTextNode(line))
            self.total_nodes += 1
            if root is None:
                root = node
            elif current_parent is None:
                root.add_child(node)
            else:
                current_parent.add_child(node)
            if node.tag_name != 'blockquote':
                current_parent = node
        return root

def main():
    text = """ THE PROLOGUE.

ACT I
Scene I. A public place.
Scene II. A Street.
Scene III. Room in Capulet’s House.
Scene IV. A Street.
Scene V. A Hall in Capulet’s House. 
 Dramatis Personæ """

    light_html = LightHTML()
    light_html.parse_text_to_html(text)
    with open("output.html", "w", encoding="utf-8") as file:
        file.write(light_html.root.render())
    print("Total nodes in the HTML tree:", light_html.total_nodes)

if __name__ == "__main__":
    main()


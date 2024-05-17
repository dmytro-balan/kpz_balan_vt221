class LightNode:
    def render(self):
        pass

class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class LightElementNode(LightNode):
    def __init__(self, tag_name, display_type='block', closing_type='paired', css_classes=None):
        self.tag_name = tag_name
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes if css_classes is not None else []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_outer_html(self):
        css_class_string = ' '.join(self.css_classes)
        opening_tag = f'<{self.tag_name}{" class=\"" + css_class_string + "\"" if css_class_string else ""}>'
        closing_tag = f'</{self.tag_name}>' if self.closing_type == 'paired' else ''
        inner_html = ''.join(child.render() for child in self.children)
        return f'{opening_tag}{inner_html}{closing_tag}'

    def get_inner_html(self):
        return ''.join(child.render() for child in self.children)

    def render(self):
        return self.get_outer_html()
def main():

    body = LightElementNode('body', 'block', 'paired')

    h1 = LightElementNode('h1', 'block', 'paired')
    h1.add_child(LightTextNode('Hello, Mykola Oleksandrovich!'))

    ul = LightElementNode('ul', 'block', 'paired', ['list', 'unordered'])
    li1 = LightElementNode('li', 'block', 'paired')
    li1.add_child(LightTextNode('First li item'))
    li2 = LightElementNode('li', 'block', 'paired')
    li2.add_child(LightTextNode('Second li item'))
    ul.add_child(li1)
    ul.add_child(li2)

    body.add_child(h1)
    body.add_child(ul)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(body.render())

if __name__ == "__main__":
    main()


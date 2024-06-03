using System;
using System.Collections;
using System.Collections.Generic;

namespace HTMLFramework
{
    // Абстрактний клас Node
    abstract class Node
    {
        public abstract void Accept(IVisitor visitor);
    }

    // Клас TextNode, що представляє текстовий вузол
    class TextNode : Node
    {
        public string Content { get; set; }

        public TextNode(string content)
        {
            Content = content;
        }

        public override void Accept(IVisitor visitor)
        {
            visitor.Visit(this);
        }
    }

    // Клас ElementNode, що представляє елемент вузол
    class ElementNode : Node, IEnumerable<Node>
    {
        public string Tag { get; }
        public bool IsBlock { get; }
        public bool IsSelfClosing { get; }
        public List<string> Classes { get; }
        private List<Node> children;

        public ElementNode(string tag, bool isBlock, bool isSelfClosing)
        {
            Tag = tag;
            IsBlock = isBlock;
            IsSelfClosing = isSelfClosing;
            Classes = new List<string>();
            children = new List<Node>();
        }

        public void AddChild(Node child)
        {
            children.Add(child);
        }

        public IEnumerator<Node> GetEnumerator()
        {
            return children.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        public override void Accept(IVisitor visitor)
        {
            visitor.Visit(this);
            foreach (var child in children)
            {
                child.Accept(visitor);
            }
        }
    }

    // Інтерфейс IVisitor для шаблону Відвідувач
    interface IVisitor
    {
        void Visit(TextNode textNode);
        void Visit(ElementNode elementNode);
    }

    // Ітератор для перебору вузлів у глибину
    class DepthIterator : IEnumerator<Node>
    {
        private Stack<IEnumerator<Node>> stack = new Stack<IEnumerator<Node>>();

        public DepthIterator(Node root)
        {
            stack.Push(new SingleNodeEnumerator(root));
        }

        public Node Current
        {
            get
            {
                return stack.Peek().Current;
            }
        }

        object IEnumerator.Current => Current;

        public void Dispose() { }

        public bool MoveNext()
        {
            if (stack.Count == 0)
                return false;

            var enumerator = stack.Peek();
            if (!enumerator.MoveNext())
            {
                stack.Pop();
                return MoveNext();
            }

            if (Current is ElementNode elementNode)
            {
                stack.Push(elementNode.GetEnumerator());
            }

            return true;
        }

        public void Reset()
        {
            throw new NotImplementedException();
        }
    }

    // Ітератор для перебору вузлів у ширину
    class BreadthIterator : IEnumerator<Node>
    {
        private Queue<IEnumerator<Node>> queue = new Queue<IEnumerator<Node>>();

        public BreadthIterator(Node root)
        {
            queue.Enqueue(new SingleNodeEnumerator(root));
        }

        public Node Current
        {
            get
            {
                return queue.Peek().Current;
            }
        }

        object IEnumerator.Current => Current;

        public void Dispose() { }

        public bool MoveNext()
        {
            if (queue.Count == 0)
                return false;

            var enumerator = queue.Peek();
            if (!enumerator.MoveNext())
            {
                queue.Dequeue();
                return MoveNext();
            }

            if (Current is ElementNode elementNode)
            {
                queue.Enqueue(elementNode.GetEnumerator());
            }

            return true;
        }

        public void Reset()
        {
            throw new NotImplementedException();
        }
    }

    // Клас для одного елемента
    class SingleNodeEnumerator : IEnumerator<Node>
    {
        private Node node;
        private bool isFirst = true;

        public SingleNodeEnumerator(Node node)
        {
            this.node = node;
        }

        public Node Current => node;

        object IEnumerator.Current => Current;

        public void Dispose() { }

        public bool MoveNext()
        {
            if (isFirst)
            {
                isFirst = false;
                return true;
            }
            return false;
        }

        public void Reset()
        {
            isFirst = true;
        }
    }

    // Інтерфейс IAction
    interface IAction
    {
        void Execute();
    }

    // Клас елементів HTML з підтримкою команди
    class ElementNodeWithAction : ElementNode
    {
        private Dictionary<string, List<IAction>> eventHandlers = new Dictionary<string, List<IAction>>();

        public ElementNodeWithAction(string tag, bool isBlock, bool isSelfClosing)
            : base(tag, isBlock, isSelfClosing) { }

        public void AddEventHandler(string eventType, IAction action)
        {
            if (!eventHandlers.ContainsKey(eventType))
            {
                eventHandlers[eventType] = new List<IAction>();
            }
            eventHandlers[eventType].Add(action);
        }

        public void TriggerEvent(string eventType)
        {
            if (eventHandlers.ContainsKey(eventType))
            {
                foreach (var action in eventHandlers[eventType])
                {
                    action.Execute();
                }
            }
        }
    }

    // Приклад команди для обробки події кліку
    class ClickAction : IAction
    {
        private string message;

        public ClickAction(string message)
        {
            this.message = message;
        }

        public void Execute()
        {
            Console.WriteLine(message);
        }
    }

    // Інтерфейс IState
    interface IState
    {
        void Handle(ElementNodeWithState element);
    }

    // Клас елементів HTML з підтримкою стану
    class ElementNodeWithState : ElementNode
    {
        public IState CurrentState { get; set; }

        public ElementNodeWithState(string tag, bool isBlock, bool isSelfClosing)
            : base(tag, isBlock, isSelfClosing) { }

        public void Request()
        {
            CurrentState.Handle(this);
        }
    }

    // Реалізація конкретного стану
    class DefaultState : IState
    {
        public void Handle(ElementNodeWithState element)
        {
            Console.WriteLine($"Element {element.Tag} is in default state.");
        }
    }

    class HoverState : IState
    {
        public void Handle(ElementNodeWithState element)
        {
            Console.WriteLine($"Element {element.Tag} is in hover state.");
        }
    }

    // Клас елементів HTML з шаблонним методом
    abstract class ElementNodeWithHooks : ElementNode
    {
        protected ElementNodeWithHooks(string tag, bool isBlock, bool isSelfClosing)
            : base(tag, isBlock, isSelfClosing) { }

        public void Render()
        {
            OnCreated();
            OnInserted();
            OnStylesApplied();
            OnClassesApplied();
            OnTextRendered();
        }

        protected virtual void OnCreated() { }
        protected virtual void OnInserted() { }
        protected virtual void OnStylesApplied() { }
        protected virtual void OnClassesApplied() { }
        protected virtual void OnTextRendered() { }
    }

    // Конкретний елемент з хуками життєвого циклу
    class ParagraphWithHooks : ElementNodeWithHooks
    {
        public ParagraphWithHooks()
            : base("p", true, false) { }

        protected override void OnCreated()
        {
            Console.WriteLine("Paragraph created.");
        }

        protected override void OnInserted()
        {
            Console.WriteLine("Paragraph inserted.");
        }

        protected override void OnStylesApplied()
        {
            Console.WriteLine("Paragraph styles applied.");
        }

        protected override void OnClassesApplied()
        {
            Console.WriteLine("Paragraph class list applied.");
        }

        protected override void OnTextRendered()
        {
            Console.WriteLine("Paragraph text rendered.");
        }
    }

    // Реалізація відвідувача для друку елементів
    class PrintVisitor : IVisitor
    {
        public void Visit(TextNode textNode)
        {
            Console.WriteLine($"Text: {textNode.Content}");
        }

        public void Visit(ElementNode elementNode)
        {
            Console.WriteLine($"Element: <{elementNode.Tag}>");
        }
    }

    // Головна програма для демонстрації роботи
    class Program
    {
        static void Main(string[] args)
        {
            // Створення елементів
            var body = new ElementNode("body", true, false);
            var div = new ElementNode("div", true, false);
            var paragraph = new ParagraphWithHooks();
            var text = new TextNode("Hello, World!");

            // Додавання дочірніх елементів
            body.AddChild(div);
            div.AddChild(paragraph);
            paragraph.AddChild(text);

            // Демонстрація шаблонного методу
            paragraph.Render();

            // Демонстрація ітератора
            Console.WriteLine("Depth-first iteration:");
            var depthIterator = new DepthIterator(body);
            while (depthIterator.MoveNext())
            {
                var node = depthIterator.Current;
                if (node is ElementNode element)
                {
                    Console.WriteLine($"Element: <{element.Tag}>");
                }
                else if (node is TextNode textNode)
                {
                    Console.WriteLine($"Text: {textNode.Content}");
                }
            }

            Console.WriteLine("Breadth-first iteration:");
            var breadthIterator = new BreadthIterator(body);
            while (breadthIterator.MoveNext())
            {
                var node = breadthIterator.Current;
                if (node is ElementNode element)
                {
                    Console.WriteLine($"Element: <{element.Tag}>");
                }
                else if (node is TextNode textNode)
                {
                    Console.WriteLine($"Text: {textNode.Content}");
                }
            }

            // Демонстрація шаблону Команда
            var button = new ElementNodeWithAction("button", false, false);
            button.AddEventHandler("click", new ClickAction("Button clicked!"));
            button.TriggerEvent("click");

            // Демонстрація шаблону Стейт
            var hoverState = new HoverState();
            var defaultState = new DefaultState();

            var elementWithState = new ElementNodeWithState("div", true, false);
            elementWithState.CurrentState = defaultState;
            elementWithState.Request();

            elementWithState.CurrentState = hoverState;
            elementWithState.Request();

            // Демонстрація шаблону Відвідувач
            var visitor = new PrintVisitor();
            body.Accept(visitor);
        }
    }
}

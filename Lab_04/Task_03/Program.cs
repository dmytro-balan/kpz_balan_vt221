using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

// Інтерфейс для обробки подій
interface IEventObserver
{
    void OnEvent(string eventType, HtmlElement element);
}

// Клас для обробки подій
class EventObserver : IEventObserver
{
    private string observerName;

    public EventObserver(string name)
    {
        observerName = name;
    }

    public void OnEvent(string eventType, HtmlElement element)
    {
        Console.WriteLine($"{observerName} received {eventType} event from <{element.Tag}>");
    }
}

// Абстрактний клас для вузлів HTML
abstract class HtmlNode
{
    public abstract string OuterHtml { get; }
    public abstract string InnerHtml { get; }
}

// Клас для текстових вузлів HTML
class HtmlTextNode : HtmlNode
{
    public string Text { get; set; }

    public HtmlTextNode(string text)
    {
        Text = text;
    }

    public override string OuterHtml => Text;
    public override string InnerHtml => Text;
}

// Клас для елементів HTML
class HtmlElement : HtmlNode
{
    public string Tag { get; set; }
    public bool IsBlockElement { get; set; }
    public bool IsSelfClosing { get; set; }
    public List<string> CssClasses { get; set; }
    public List<HtmlNode> Children { get; set; }
    private Dictionary<string, List<IEventObserver>> eventObservers;

    public HtmlElement(string tag, bool isBlockElement = true, bool isSelfClosing = false)
    {
        Tag = tag;
        IsBlockElement = isBlockElement;
        IsSelfClosing = isSelfClosing;
        CssClasses = new List<string>();
        Children = new List<HtmlNode>();
        eventObservers = new Dictionary<string, List<IEventObserver>>();
    }

    public void AddChild(HtmlNode child)
    {
        if (!IsSelfClosing)
        {
            Children.Add(child);
        }
    }

    public void AddEventObserver(string eventType, IEventObserver observer)
    {
        if (!eventObservers.ContainsKey(eventType))
        {
            eventObservers[eventType] = new List<IEventObserver>();
        }
        eventObservers[eventType].Add(observer);
    }

    public void RemoveEventObserver(string eventType, IEventObserver observer)
    {
        if (eventObservers.ContainsKey(eventType))
        {
            eventObservers[eventType].Remove(observer);
        }
    }

    public void TriggerEvent(string eventType)
    {
        if (eventObservers.ContainsKey(eventType))
        {
            foreach (var observer in eventObservers[eventType])
            {
                observer.OnEvent(eventType, this);
            }
        }
    }

    public override string OuterHtml
    {
        get
        {
            StringBuilder sb = new StringBuilder();
            sb.Append($"<{Tag}");

            if (CssClasses.Count > 0)
            {
                sb.Append($" class=\"{string.Join(" ", CssClasses)}\"");
            }

            if (IsSelfClosing)
            {
                sb.Append(" />");
            }
            else
            {
                sb.Append(">");
                foreach (var child in Children)
                {
                    sb.Append(child.OuterHtml);
                }
                sb.Append($"</{Tag}>");
            }

            return sb.ToString();
        }
    }

    public override string InnerHtml
    {
        get
        {
            if (IsSelfClosing)
            {
                return string.Empty;
            }

            StringBuilder sb = new StringBuilder();
            foreach (var child in Children)
            {
                sb.Append(child.InnerHtml);
            }
            return sb.ToString();
        }
    }
}

// Фабрика для створення елементів HTML
class HtmlElementFactory
{
    private Dictionary<string, HtmlElement> elements = new Dictionary<string, HtmlElement>();

    public HtmlElement GetElement(string tag, bool isBlockElement = true, bool isSelfClosing = false)
    {
        string key = $"{tag}_{isBlockElement}_{isSelfClosing}";
        if (!elements.ContainsKey(key))
        {
            elements[key] = new HtmlElement(tag, isBlockElement, isSelfClosing);
        }
        return elements[key];
    }
}

// Головний клас програми
class Program
{
    static void Main(string[] args)
    {
        // Створення тестового файлу книги
        CreateTestBookFile();

        string[] bookLines = File.ReadAllLines("book.txt");

        HtmlElementFactory factory = new HtmlElementFactory();
        HtmlElement root = factory.GetElement("div", true, false);

        foreach (string line in bookLines)
        {
            HtmlElement element;

            if (string.IsNullOrWhiteSpace(line))
            {
                continue;
            }
            else if (line.Length < 20)
            {
                element = factory.GetElement("h2");
                element.AddChild(new HtmlTextNode(line));
            }
            else if (line.StartsWith(" "))
            {
                element = factory.GetElement("blockquote");
                element.AddChild(new HtmlTextNode(line.Trim()));
            }
            else
            {
                element = factory.GetElement("p");
                element.AddChild(new HtmlTextNode(line));
            }

            root.AddChild(element);
        }

        // Додавання спостерігачів
        EventObserver clickObserver = new EventObserver("ClickObserver");
        EventObserver mouseOverObserver = new EventObserver("MouseOverObserver");

        root.AddEventObserver("click", clickObserver);
        root.AddEventObserver("mouseover", mouseOverObserver);

        // Виклик подій для демонстрації
        Console.WriteLine("HTML Output:");
        Console.WriteLine(root.OuterHtml);

        Console.WriteLine("\nTriggering click event...");
        root.TriggerEvent("click");

        Console.WriteLine("\nTriggering mouseover event...");
        root.TriggerEvent("mouseover");

        long memoryUsed = GC.GetTotalMemory(true);
        Console.WriteLine($"\nMemory used: {memoryUsed} bytes");
    }

    static void CreateTestBookFile()
    {
        string[] bookLines = {
            "The Great Gatsby",
            "by F. Scott Fitzgerald",
            "",
            "In my younger and more vulnerable years my father gave me some advice that I’ve been turning over in my mind ever since.",
            " ",
            "“Whenever you feel like criticizing any one,” he told me, “just remember that all the people in this world haven’t had the advantages that you’ve had.”",
            " ",
            "He didn’t say any more but we’ve always been unusually communicative in a reserved way, and I understood that he meant a great deal more than that.",
            " "
        };

        File.WriteAllLines("book.txt", bookLines);
    }
}

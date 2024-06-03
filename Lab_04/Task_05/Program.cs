using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Threading.Tasks;

public class TextDocument
{
    public string Content { get; set; }

    public TextDocument(string content)
    {
        Content = content;
    }
}
public class Memento
{
    public string Content { get; }

    public Memento(string content)
    {
        Content = content;
    }
}

public class TextEditor
{
    private TextDocument _document;
    private Stack<Memento> _history;

    public TextEditor(string initialContent)
    {
        _document = new TextDocument(initialContent);
        _history = new Stack<Memento>();
    }

    public void Write(string content)
    {
        SaveState();
        _document.Content = content;
    }

    public void SaveState()
    {
        _history.Push(new Memento(_document.Content));
    }

    public void Undo()
    {
        if (_history.Count > 0)
        {
            Memento memento = _history.Pop();
            _document.Content = memento.Content;
        }
    }

    public string GetContent()
    {
        return _document.Content;
    }
}
class Program
{
    static void Main(string[] args)
    {
        TextEditor editor = new TextEditor("Initial content");
        Console.WriteLine($"Initial content: {editor.GetContent()}");

        editor.Write("First change");
        Console.WriteLine($"After first change: {editor.GetContent()}");

        editor.Write("Second change");
        Console.WriteLine($"After second change: {editor.GetContent()}");

        editor.Undo();
        Console.WriteLine($"After undo: {editor.GetContent()}");

        editor.Undo();
        Console.WriteLine($"After second undo: {editor.GetContent()}");
    }
}

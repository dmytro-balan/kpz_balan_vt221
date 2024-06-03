using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public interface IHandler
{
    void SetNext(IHandler handler);
    void HandleRequest(string request);
}
public abstract class BaseHandler : IHandler
{
    private IHandler _nextHandler;

    public void SetNext(IHandler handler)
    {
        _nextHandler = handler;
    }

    public virtual void HandleRequest(string request)
    {
        if (_nextHandler != null)
        {
            _nextHandler.HandleRequest(request);
        }
        else
        {
            Console.WriteLine("No handler could process the request.");
        }
    }
}
public class Level1Support : BaseHandler
{
    public override void HandleRequest(string request)
    {
        if (request == "1")
        {
            Console.WriteLine("Level 1 support handling the request.");
        }
        else
        {
            base.HandleRequest(request);
        }
    }
}

public class Level2Support : BaseHandler
{
    public override void HandleRequest(string request)
    {
        if (request == "2")
        {
            Console.WriteLine("Level 2 support handling the request.");
        }
        else
        {
            base.HandleRequest(request);
        }
    }
}

public class Level3Support : BaseHandler
{
    public override void HandleRequest(string request)
    {
        if (request == "3")
        {
            Console.WriteLine("Level 3 support handling the request.");
        }
        else
        {
            base.HandleRequest(request);
        }
    }
}

public class Level4Support : BaseHandler
{
    public override void HandleRequest(string request)
    {
        if (request == "4")
        {
            Console.WriteLine("Level 4 support handling the request.");
        }
        else
        {
            base.HandleRequest(request);
        }
    }
}
public class SupportSystem
{
    private IHandler _handlerChain;

    public SupportSystem()
    {
        var level1 = new Level1Support();
        var level2 = new Level2Support();
        var level3 = new Level3Support();
        var level4 = new Level4Support();

        level1.SetNext(level2);
        level2.SetNext(level3);
        level3.SetNext(level4);

        _handlerChain = level1;
    }

    public void Start()
    {
        while (true)
        {
            Console.WriteLine("Please choose an option:");
            Console.WriteLine("1. Level 1 support");
            Console.WriteLine("2. Level 2 support");
            Console.WriteLine("3. Level 3 support");
            Console.WriteLine("4. Level 4 support");
            Console.WriteLine("5. Exit");

            var input = Console.ReadLine();

            if (input == "5")
            {
                break;
            }

            _handlerChain.HandleRequest(input);
        }
    }
}
class Program
{
    static void Main(string[] args)
    {
        SupportSystem supportSystem = new SupportSystem();
        supportSystem.Start();
    }
}

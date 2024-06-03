using System;
using System.Net.Http;
using System.Threading.Tasks;
public interface IImageLoadingStrategy
{
    void LoadImage(string path);
}


public class FileImageLoadingStrategy : IImageLoadingStrategy
{
    public void LoadImage(string path)
    {
        Console.WriteLine($"Loading image from file system: {path}");
        // Реалізація завантаження зображення з файлової системи
        // Наприклад, File.ReadAllBytes(path) для отримання байтів зображення
    }
}

public class NetworkImageLoadingStrategy : IImageLoadingStrategy
{
    public async void LoadImage(string url)
    {
        Console.WriteLine($"Loading image from network: {url}");
        // Реалізація завантаження зображення з мережі
        using (HttpClient client = new HttpClient())
        {
            try
            {
                byte[] imageData = await client.GetByteArrayAsync(url);
                // Обробка завантаженого зображення
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Failed to load image from network: {ex.Message}");
            }
        }
    }
}
public class ImageElement
{
    private IImageLoadingStrategy _imageLoadingStrategy;

    public ImageElement(IImageLoadingStrategy strategy)
    {
        _imageLoadingStrategy = strategy;
    }

    public void SetImageLoadingStrategy(IImageLoadingStrategy strategy)
    {
        _imageLoadingStrategy = strategy;
    }

    public void LoadImage(string path)
    {
        _imageLoadingStrategy.LoadImage(path);
    }
}
class Program
{
    static void Main(string[] args)
    {
        // Використання стратегії для завантаження зображення з файлової системи
        ImageElement fileImage = new ImageElement(new FileImageLoadingStrategy());
        fileImage.LoadImage("path/to/local/image.jpg");

        // Використання стратегії для завантаження зображення з мережі
        ImageElement networkImage = new ImageElement(new NetworkImageLoadingStrategy());
        networkImage.LoadImage("http://example.com/image.jpg");

        // Зміна стратегії під час виконання
        networkImage.SetImageLoadingStrategy(new FileImageLoadingStrategy());
        networkImage.LoadImage("path/to/another/local/image.jpg");
    }
}

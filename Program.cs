using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        try
        {
            using var client = new HttpClient();

            var json = JsonSerializer.Serialize(new { amount_in_rs = 1000 });

            var response = await client.PostAsync(
                "http://localhost:3000/convert",
                new StringContent(json, Encoding.UTF8, "application/json"));

            Console.WriteLine("Status: " + response.StatusCode);
            Console.WriteLine(await response.Content.ReadAsStringAsync());
        }
        catch (Exception e)
        {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}
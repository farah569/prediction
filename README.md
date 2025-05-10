# Greenhouse AI Backend Integration Guide

---

## Step 1: Clone the Project from github 
---

## Step 2: Set Up Python Environment make sure python is installed (i used version 3.10.9):

# write in terminal : python -m venv venv
# then write this in terminal to activate (for windows) : venv\Scripts\activate
# then write this in terminal to activate (if you are using  Linux/macOS:) : source venv/bin/activate
---

# Step 3: Install Python Dependencies:

# write in terminal : pip install -r requirements.txt
---

# Step 4: Run the Flask API: 

# run in terminal : python app.py (in this step replace the URL in the code with the URL you have from output)
# to get the URL  you should see output like this : http://127.0.0.1:5000

------

# Step 5: Connect with C# Backend:

# In your C# backend, use the following class to send data and receive predictions from the AI API
# 📌 Make sure Flask is still running in the background before calling the API from C#.
# this is the code that contains sensor readings in order to get results :
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

public class GreenhouseAIClient
{
    public async Task<string> GetAIPredictionAsync()
    {
        var httpClient = new HttpClient();
        var jsonPayload = new
        {
            sequence = new float[][]
                   {
                new float[] {23.0f, 60.1f, 30.0f, 1, 0, 0},
                new float[] {23.6f, 60.2f, 30.1f, 1, 0, 0},
                new float[] {23.7f, 60.3f, 30.2f, 1, 0, 0},
                new float[] {23.8f, 60.2f, 30.1f, 1, 0, 0},
                new float[] {23.9f, 60.1f, 30.0f, 1, 0, 0},
                new float[] {24.0f, 60.0f, 29.9f, 1, 0, 0},
                new float[] {24.1f, 59.9f, 29.8f, 1, 0, 0},
                new float[] {24.2f, 59.8f, 29.7f, 1, 0, 0},
                new float[] {24.3f, 59.7f, 29.6f, 1, 0, 0},
                new float[] {24.4f, 59.6f, 29.5f, 1, 0, 0},
                new float[] {24.5f, 59.5f, 29.4f, 1, 0, 0},
                new float[] {24.6f, 59.4f, 29.3f, 1, 0, 0},
                new float[] {24.7f, 59.3f, 29.2f, 1, 0, 0},
                new float[] {24.8f, 59.2f, 29.1f, 1, 0, 0},
                new float[] {24.9f, 59.1f, 29.0f, 1, 0, 0},
                new float[] {25.0f, 59.0f, 28.9f, 1, 0, 0},
                new float[] {25.1f, 58.9f, 28.8f, 1, 0, 0},
                new float[] {25.2f, 58.8f, 28.7f, 1, 0, 0},
                new float[] {25.3f, 58.7f, 28.6f, 1, 0, 0},
                new float[] {25.4f, 58.6f, 28.5f, 1, 0, 0},
                new float[] {25.5f, 58.5f, 28.4f, 1, 0, 0},
                new float[] {25.6f, 58.4f, 28.3f, 1, 0, 0},
                new float[] {25.7f, 58.3f, 28.2f, 1, 0, 0},
                new float[] {25.8f, 58.2f, 28.1f, 1, 0, 0}
            }
        };

        var json = JsonSerializer.Serialize(jsonPayload);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var response = await httpClient.PostAsync("http://127.0.0.1:5000/predict", content); #you can replace this with the URL you have
        var result = await response.Content.ReadAsStringAsync();

        return result;
    }
}
 ----- 

 # Step 6: Test the Integration
 # In your C# app, create a method to test the client:

 public async Task TestPrediction()
{
    var client = new GreenhouseAIClient();
    var prediction = await client.GetAIPredictionAsync();
    Console.WriteLine("Prediction: " + prediction);
}

# Run this and ensure you see the prediction printed in your console.
# you should see output like this :  {"predicted_humidity": 61.36, "predicted_moisture": 58.13, "predicted_temperature": 22.94}
# note : Ensure Flask is running before testing from C#.


















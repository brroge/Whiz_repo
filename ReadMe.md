
Fantasy League Data Service (AWS Serverless Solution)
Designed and deployed a serverless data platform using AWS Lambda, API Gateway, S3, only fetching when the page is loaded(On-demand fetch = always live, zero background cost) to deliver real-time NBA game stats from the Balldontlie API. 
Enabled secure, automated data retrieval and live score visualization for fantasy league applications.

----------NBA STAT AWS----------
https://app.balldontlie.io/


Architecture

1.Lambda: Calls Balldontlie API with your key  fetches game data, and returns JSON.
2.API Gateway: Creates a public HTTPS endpoint to call your Lambda.
3. HTML Page: Calls your API Gateway URL, not Balldontlie directly.

Your API key stays hidden inside Lambda.
The HTML just reads JSON → builds the table.
-----------FINAL--------------
How It Works
You open your S3 static website (your dashboard).
The browser runs JavaScript → calls your API Gateway URL.
API Gateway triggers your Lambda function.
Lambda fetches live NBA game data from Balldontlie’s /games endpoint.
Lambda sends the JSON back through API Gateway → browser.
Your dashboard displays team matchups, scores, and game status.
---
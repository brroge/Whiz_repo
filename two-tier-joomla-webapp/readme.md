What This Project Does – Plain English
1 You have a website (Joomla)

This is your “main application” where you post blogs or content.

It’s stored on a virtual server (EC2) and uses a database (RDS) to save all your data.

The database is private, meaning only your web server can reach it — safer from hackers.

2 Your website is now “behind a security gate” (API Gateway + Cognito)

Cognito: Think of it like a front door with a security guard. People have to log in before accessing the website or API.

API Gateway: This is the “door” that controls who can go through, checks their login, and passes them to the website.

So now, only registered users (or guests with approved logins) can reach your site.

3 Load Balancer (ALB)

Imagine your website is a store, and suddenly hundreds of people show up.

The Load Balancer acts like a smart traffic director:

Sends users to different servers so none get overwhelmed.

Makes sure the website stays fast, even if traffic spikes.

4 Logging & Accounting (CloudWatch + DynamoDB)

Every time someone visits or does something, the system keeps a record.

You can see:

Who logged in

What pages or APIs they used

When they did it

This is called Accounting, the “A” in AAA (Authentication, Authorization, Accounting).

5 Security & Optional Protections

CloudFront + WAF: Acts like a shield, blocking bad traffic and speeding up content delivery.

Secrets Manager: Stores passwords or keys safely so no one can steal them.

Private Subnets: Keeps your database and servers hidden from the public internet.

 Why This Is Useful

Safe – Only authorized users can access your site or APIs.

Scalable – Handles more visitors without crashing.

Auditable – You can track everything users do.

Professional/Enterprise-ready – Shows real-world cloud architecture, security, and best practices.


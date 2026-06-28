# --- Student Registration Serverless API on AWS-----

## Project Overview--

This project demonstrates how to build a **Serverless REST API** using AWS services.

The API accepts student details and processes them using AWS Lambda. If an error occurs or invalid data is detected, Amazon SNS sends an email notification.

---

## Architecture anf flow of project

```text
Client
   │
   ▼
API Gateway
   │
Request Validator
   │
Lambda (Python)
   │
 ┌─────────────┐
 │             │
 ▼             ▼
CloudWatch     SNS
 Logs      Email Notification
```

---

## what  AWS Services Used in this project

* Amazon API Gateway
* AWS Lambda
* Amazon SNS
* Amazon CloudWatch
* IAM Roles & Policies

---

## Features

* REST API
* Lambda Proxy Integration
* Request Validation
* CloudWatch Logging
* SNS Email Alerts
* IAM Permissions
* JSON Request Processing

---

## Sample Request

```json
{
  "name":"Vivek",
  "age":22,
  "department":"MCA"
}
```

---

## Sample Response

```json
{
  "message":"Student Registered Successfully",
  "name":"Vivek",
  "age":22,
  "department":"MCA"
}
```

---

## Error Handling

If invalid data is received, Lambda publishes an alert to Amazon SNS and an email notification is sent.

## [Note]-when give endpoints in sns then u get mail in give email id then u go there and conferm it ****

## u can also test in postman  as well as in the  api gateway console   ->go to test->{ "name":"Vivek", "age":22, "department":"MCA" }
## ->test (u get answer )

import json
import boto3

sns = boto3.client("sns")

TOPIC_ARN = "arn:aws:sns:ap-south-1:835688182082:vivek-cw-01"

def lambda_handler(event, context):

    try:

        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event

        name = body["name"]
        age = body["age"]
        department = body["department"]

        # Validation
        if age < 18:

            sns.publish(
                TopicArn=TOPIC_ARN,
                Subject="Student Registration Alert",
                Message=f"Invalid age received.\n\nName: {name}\nAge: {age}\nDepartment: {department}"
            )

            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Age must be 18 or above."
                })
            }

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Student Registered Successfully",
                "name": name,
                "age": age,
                "department": department
            })
        }

    except Exception as e:

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="Student API Error",
            Message=str(e)
        )

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
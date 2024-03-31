import json
import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Select the DynamoDB table
table = dynamodb.Table('your-table-name')

def lambda_handler(event, context):
    # Extract book details from the event
    book_title = event['bookTitle']
    
    author = event['author']
    ISBN = event['ISBN']
    genre = event['genre']
    year = int(event['year'])
    
    # Check if the year is valid
    if year > 0:
        # If valid, store the book details in the DynamoDB table
        response = table.put_item(
            Item={
                'ISBN': ISBN,
                'bookTitle': book_title,
                'author': author,
                'genre': genre,
                'year': year
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Reservation successful!')
        }
    else:
        # If not valid, return a message indicating the issue
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid year. Please provide a valid year.')
        }

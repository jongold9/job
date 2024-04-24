import boto3, os

def lambda_handler(event, context):
    # Create an S3 client
    myS3 = boto3.client('s3')

    try:
        # List all buckets using the S3 client
        results = myS3.list_buckets()
        print(results)  # Optionally print all results

        output = ""
        for bucket in results['Buckets']:
            output += bucket['Name'] + "<br>"

        # Output the list of bucket names in HTML format
        return ("<h1><font color='green'>S3 Bucket List:</font></h1><br><br>" + output)

    except Exception as e:
        # Print error message in red in HTML format
        return ("<h1><font color='red'>Error:</font></h1><br><br>" + str(e))
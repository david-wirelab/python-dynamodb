#!/bin/python
"""
Interact with DynamoDB using Python definitions. Pseudo code - Example only.
"""

from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr

TABLE_NAME = 'foo'
DYNAMODB = boto3.resource('dynamodb', region_name='foo')
TABLE = DYNAMODB.Table('TABLE_NAME')

def table_put(name):
    """
    Put an item to the table
    """
    table = name
    response = table.put_item(
        Item={
            'FileID': 'foobar.xml',
            'Stamp': '1234',
            }
    )
    return response

def query_table(name):
    """
    Query exising table
    """
    table = name
    response = table.query(
        KeyConditionExpression=Key('FileID').eq('foobar.xml')
    )
    items = response['Items']
    return items

def main():
    """
    Main
    """
    name = TABLE_NAME
    if table_put(name):
        query_table(name)
    else:
        print 'There was a booboo.'

if __name__ == '__main__':
    main()

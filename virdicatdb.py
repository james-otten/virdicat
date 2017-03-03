import boto3
from boto3.dynamodb.conditions import Key, Attr
import hashlib

LAST_SEEN_ITEM_ID = 'LastSeen'

class VirdicatDb:
    def __init__(self, tableName='virdicat'):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(tableName)
        
    def get_content_options(self):
        response = self.table.scan(FilterExpression=Attr('Used').eq(False))
        items = response['Items']
        return items
    
    def set_content_used(self, item):
        #This will set all items with the same ItemId to used
        # thus taking care of duplicate links in the database
        self.table.update_item(Key={'ItemId':item['ItemId']},
                          UpdateExpression='SET Used = :val1',
                          ExpressionAttributeValues={':val1':True})
    
    def create_content(self, link, post_type):
        #ItemId is the SHA512 of the link
        itemId = hashlib.sha512(link).hexdigest()
        self.table.put_item(Item={'ItemId':itemId,
                                  'Link':link,
                                  'Type':post_type,
                                  'Used':False})
        return itemId

    def get_last_seen(self):
        response = self.table.get_item(Key={'ItemId':LAST_SEEN_ITEM_ID})
        return response['Item']['Link']
    
    def set_last_seen(self, link):
        self.table.update_item(Key={'ItemId':LAST_SEEN_ITEM_ID},
                          UpdateExpression='SET Link = :val1',
                          ExpressionAttributeValues={':val1':link})

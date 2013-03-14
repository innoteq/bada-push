#!/usr/bin/env python
import simplejson
import client
import random
import unittest

class PushClientTest(unittest.TestCase):
    WRONG_SECRET = 'Winter in Siberia is warm'
    RIGHT_SECRET = 'Bears in Siberia do not walk on the sidewalks and do not drink vodka. Sssh, it is a secret!'

    def setUp(self):
        # configure spy object for replacement of requests.post
        self.old_client_requests_post = client.requests.post
        def post_test_spy(url, data, headers, verify): # http://habrahabr.ru/post/116372/
            post_test_spy.requests.append((url, data, headers))
            class StubResounse(object):
                ok = True
                def __init__(self, content):
                    self.content = simplejson.dumps(content)

            if headers['appSecret'] == self.WRONG_SECRET:
                return StubResounse(
                    {'results':
                        [{'regID': '', 'statusMsg': 'error of application authentication failed - header: 000000000, regId: 0000000000000000', 'requestID': '', 'statusCode': 3052}]
                    }
                )
            elif headers['appSecret'] == self.RIGHT_SECRET:
                return StubResounse(
                    {'results':
                        [{'regID': '', 'statusMsg': 'Success', 'requestID': simplejson.loads(data)['requestID'], 'statusCode': client.STATUS_CODE_SUCCESS}]
                    }
                )
            else:
                raise NotImplementedError()

        post_test_spy.requests = []
        client.requests.post = post_test_spy 

    def test_invalid_parameters(self):
        '''
        Parameters are invalid. The rest does not matter.
        '''
        def create_invalid_message():
            client.PushMessage(
                url='https://apnortheast.push.samsungosp.com:8088/spp/pns/api/push',
                app_id='app-id',
                app_secret=self.WRONG_SECRET,
                reg_id='reg-id',
                alert_message='Hello world!',
                app_data=simplejson.dumps({'message':'Test message'}),
                action='EATHOTDOG',
            )
        self.assertRaises(client.ParameterError, create_invalid_message)

    def test_wrong_secret(self):
        '''
        Secret is wrong. send() raises RequestError.
        '''
        message = client.PushMessage(
            url='https://apnortheast.push.samsungosp.com:8088/spp/pns/api/push',
            app_id='app-id',
            app_secret=self.WRONG_SECRET,
            reg_id='reg-id',
            alert_message='Hello world!',
            app_data=simplejson.dumps({'message':'Test message'}),
            verify_ssl=False
        )
        self.assertRaises(client.ServerResponseError, message.send)

    def test_right_secret(self):
        '''
        Input data are valid.
        '''
        message = client.PushMessage(
            url='https://apnortheast.push.samsungosp.com:8088/spp/pns/api/push',
            app_id='app-id',
            app_secret=self.RIGHT_SECRET,
            reg_id='reg-id',
            alert_message='Hello world!',
            app_data=simplejson.dumps({'message':'Test message'}),
            verify_ssl=False
        )
        self.assertEqual(message.send()['results'][0]['statusCode'], client.STATUS_CODE_SUCCESS)

    def tearDown(self):
        client.requests.post = self.old_client_requests_post 

        
if __name__ == '__main__':
    unittest.main()

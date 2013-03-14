python-samsung-bada-push-client
===============================

Python module for push messaging service for Samsung Bada.

Usage
-----

    import samsung_bada_push_client

    message = samsung_bada_push_client.send(
        url='https://apnortheast.push.samsungosp.com:8088/spp/pns/api/push',
        app_id='your-app-id',
        app_secret='your-app-secret',
        reg_id='registration-id',
        action='ALERT',
        alert_message='any-alert-message',
        app_data='any-data'
    )

    See doc comments for details.


Useful links
------------

Push Messaging Guide: http://developer.bada.com/article/push-messaging-guide
Error codes: http://developer.bada.com/article/push-messaging-guide#status_codes_messages

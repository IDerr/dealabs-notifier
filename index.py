from plyer import notification
from dealabs import Dealabs
import time


def main():
    dealabs_client = Dealabs()
    old = dealabs_client.get_deals_hot()
    old_time = int(time.time())
    notification_data={}
    while True:
        old = dealabs_client.get_deals_hot()
        for hot in old['data']:
            if hot['hot_date'] > old_time:
                notification_data['title'] = 'Hot Deal'
                notification_data['message'] = '{0} {1}'.format(hot['title'], hot['price'])
                notification.notify(**notification_data)
        old_time = int(time.time())
        time.sleep(20)

if __name__ == '__main__':
    main()

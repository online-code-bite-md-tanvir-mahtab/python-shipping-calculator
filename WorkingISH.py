import requests
import pandas as pd
import random
import time
import threading
import logging
from concurrent.futures import ThreadPoolExecutor
from user_agents import user_agents


class WebPageViewer:
    def __init__(self, proxy_file, min_view_duration, max_view_duration, min_new_instance_delay,
                 max_new_instance_delay, max_concurrent_instances):
        self.proxy_ips = self.load_proxies(proxy_file)
        self.min_view_duration = min_view_duration
        self.max_view_duration = max_view_duration
        self.min_new_instance_delay = min_new_instance_delay
        self.max_new_instance_delay = max_new_instance_delay
        self.max_concurrent_instances = max_concurrent_instances
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': self.get_random_user_agent()})
        self.lock = threading.Lock()
        self.working_proxies = []

    def load_proxies(self, proxy_file):
        proxies = pd.read_csv(proxy_file)
        return proxies['IP'].tolist()

    def get_random_user_agent(self):
        return random.choice(user_agents)

    def view_web_page(self):
        url = 'https://www.twitch.tv/stormtrooper345'  # Replace with your target URL

        with self.lock:
            if len(self.proxy_ips) == 0:
                return

            proxy = self.get_random_proxy()

        try:
            response = self.session.get(url, proxies=proxy, timeout=10)
            if response.ok or response.status_code == 201 or response.status_code == 202:
                with self.lock:
                    self.working_proxies.append(proxy)
                    print("Proxy worked:", proxy)
            else:
                logging.info(f'Instance received non-200 status code: {response.status_code}')
                print("Proxy did not work:", proxy)
        except requests.RequestException as e:
            logging.error(f'Error occurred during web page viewing: {str(e)}')

    def get_random_proxy(self):
        proxy_ip = random.choice(self.proxy_ips)
        proxies = {'http': f'http://{proxy_ip}', 'https': f'https://{proxy_ip}'}
        return proxies

    def run_instances(self):
        with ThreadPoolExecutor(max_workers=self.max_concurrent_instances) as executor:
            while len(self.working_proxies) < self.max_concurrent_instances:
                executor.submit(self.view_web_page)
                delay = random.uniform(self.min_new_instance_delay, self.max_new_instance_delay)
                time.sleep(delay)
                print("_____NEW____INSTANCE____EXECUTED_____")
                print("__NUMBER__OF__RUNNING__INSTANCES__")
                print(len(self.working_proxies))
                print("________________", len(self.working_proxies), "________________")


def main():
    logging.basicConfig(filename='web_page_viewer.log', level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] - %(message)s')

    proxy_file = 'E:\\Python\\Neo\\List\\workingProxies.csv'  # Replace with your proxy IP file path
    min_view_duration = 60  # Minimum view duration in seconds (1 minute)
    max_view_duration = 7200  # Maximum view duration in seconds (2 hours)
    min_new_instance_delay = 10  # Minimum delay between new instances in seconds
    max_new_instance_delay = 11  # Maximum delay between new instances in seconds (2 hours)
    max_concurrent_instances = 10  # Maximum number of concurrent instances

    web_page_viewer = WebPageViewer(proxy_file, min_view_duration, max_view_duration,
                                   min_new_instance_delay, max_new_instance_delay, max_concurrent_instances)
    web_page_viewer.run_instances()

    # Wait for some time or until a working proxy is found
    time.sleep(600)  # Adjust the sleep time as needed

    if len(web_page_viewer.working_proxies) > 0:
        working_proxies_output_file = 'workingProxies2.csv'  # Replace with the desired output file path for working proxies
        working_proxies_df = pd.DataFrame({'ip': web_page_viewer.working_proxies})
        working_proxies_df.to_csv(working_proxies_output_file, index=False)


if __name__ == '__main__':
    main()

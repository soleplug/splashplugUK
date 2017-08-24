from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import sys

fn = sys.argv[1]
try:
    proxy = sys.argv[2]


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    # Change the path below to point to your chromedriver
    driver = webdriver.Chrome(r"/Users/hasan/Downloads/chromedriver", chrome_options=chrome_options)

except:
    # Change the path below to point to your chromedriver
    driver = webdriver.Chrome(r"/Users/hasan/Downloads/chromedriver")
    
x = ""
driver.get('http://www.adidas.com/yeezy')
cookies = driver.get_cookies()
for cookie in cookies:

    if(cookie['name'] == 'RT'):
        s = list(cookie['value'])
        s[0] = "'"
        s[-1] = "'"
        x = x + (cookie['name'] + '=' + ''.join(s) + '; ') 
    else:
        x = x + (cookie['name'] + '=' + cookie['value'] + '; ') 
 
driver.quit()
x = x[:-2]
f= open(fn,"w")
f.write("""#!/bin/bash
args=("$@")
if [[ ${args[1]} == *"proxy"* ]]; then
    while true; do
        response=$(curl -x ${args[2]} -c ${args[0]} -s -k -i --compressed "http://www.adidas.com/uk/apps/yeezy/" -H "Host: www.adidas.co.uk" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Accept-Encoding: gzip, deflate, sdch" -H "Accept-Language: en-US,en;q=0.8" -H "Cookie: """ + x + """")
        if [[ $response == *"YEEZY"* ]]; then
            echo "Locate cookies in" $args[2]
            echo $args[2] >> 'result.txt'
            break
        fi
    done
else
    while true; do
        response=$(curl -c ${args[0]} -s -k -i --compressed "http://www.adidas.com/us/apps/yeezy/" -H "Host: www.adidas.com" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Accept-Encoding: gzip, deflate, sdch" -H "Accept-Language: en-US,en;q=0.8" -H "Cookie: """ + x + """")
        if [[ $response == *"YEEZY"* ]]; then
            echo "Locate cookies in" $args[2]
            echo $args[2] >> 'result.txt'
            break
        fi
    done
fi


""")
f.close()


    

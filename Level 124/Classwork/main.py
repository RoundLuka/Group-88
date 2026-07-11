from myData import nasa_key, weatherAPI_key, sms_key
import requests
import json
# import schedule
import time


# # NASA
# payload = {'api_key':nasa_key}
# url = 'https://api.nasa.gov/planetary/apod'
# r = requests.get(url, params=payload)
# res = r.json()
# print(json.dumps(res, indent=4))

# img_url = res['hdurl']
# img_resp = requests.get(img_url)
# print(img_resp)

# with open('nasa.jpg','wb') as f:
#     f.write(img_resp.content)



##https://api.weatherapi.com/ API
# 42°09'42.94"N 42°20'36.83"E

lat = 42.16192778
long = 42.343564167

# მიმდინარე - current
url = f'http://api.weatherapi.com/v1/current.json?key={weatherAPI_key}&q=Samtredia'
# პროგნოზი - forecast (უფასოდ 3 დღე)
url = f'http://api.weatherapi.com/v1/forecast.json?key={weatherAPI_key}&q=Samtredia'
# ისტორია - history, ჭირდება თარიღის მითითება dt (უფასოდ 7 დღე)
url = f'http://api.weatherapi.com/v1/history.json?key={weatherAPI_key}&q=Samtredia&dt=2026-07-11'


payload = {'q':str(lat)+','+str(long), 'key':weatherAPI_key}
# url = f'http://api.weatherapi.com/v1/current.json'


resp = requests.get(url)
# resp = requests.get(url, params=payload)
res = resp.json()
print(json.dumps(res, indent=4))



# მზის ამოსვლა/ჩასვლა - astronomy
# payload = {'q':str(lat)+','+str(long), 'key':weatherAPI_key, 'dt': '2024-06-20'}
# url = f'http://api.weatherapi.com/v1/astronomy.json'

# resp = requests.get(url, params=payload)
# res = resp.json()
# print(json.dumps(res, indent=4))



# aqi - yes - ჰაერის მდგომარეობა
# payload = {'q':str(lat)+','+str(long), 'key':weatherAPI_key, 'dt': '2024-06-20', 'aqi': 'yes'}
# url = f'http://api.weatherapi.com/v1/current.json'

# resp = requests.get(url, params=payload)
# res = resp.json()
# print(json.dumps(res, indent=4))





## schedule win10toast

# def job():
#     print("I'm working...")

# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


## notification

#1 pip install plyer
# from plyer import notification

# notification.notify(
#     title='სათაური',
#     message='ტექსტი',
#     timeout=10
# )

#2 pip install winotify
# from winotify import Notification

# toast = Notification(
#     app_id="ჩემი აპი",
#     title="სათაური",
#     msg="ტექსტი"
# )
# toast.show()





# def weather(city, key):
#     payload = {'q': city, 'key': key, 'aqi': 'yes'}
#     url = 'http://api.weatherapi.com/v1/current.json'

#     resp = requests.get(url, params=payload)
#     data = resp.json()
    
#     temp = data['current']['temp_c']
#     wind_speed = data['current']['wind_kph']
#     wind_dir = data['current']['wind_dir']
#     humidity = data['current']['humidity']
#     pressure = data['current']['pressure_mb']
#     cloud = data['current']['cloud']
#     air_quality = data['current']['air_quality']

#     fil_data = f'''ტემპერატურა: {temp}°C | ქარი: {wind_speed}კმ/სთ ({wind_dir}) | ტენიანობა: {humidity}%
# წნევა: {pressure} მბ | ღრუბლიანობა: {cloud}% | AQI (EPA): {air_quality['us-epa-index']}'''
#     return fil_data.strip()

# def weather_notification():
#     city = "Tbilisi"
#     key = weatherAPI_key 

#     toast = ToastNotifier()
#     weather_msg = weather(city, key)

#     toast.show_toast(
#         "ამინდის შეტყობინება",
#         weather_msg,
#         icon_path=None,
#         duration=15,
#         threaded=True
#     )

# schedule.every(5).seconds.do(weather_notification)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# ## სმს
# def send_message(number, msg):
#     payload  = {'key': sms_key,'destination': number,
#             'sender': 'anis', 'content': msg, 'showServiceTime':'true'}

#     r = requests.get('http://smsoffice.ge/api/v2/send', params=payload)



# if __name__ == '__main__':
#     number = '995XXXXXXXXX'
#     msg = weather('Tbilisi', weatherAPI_key)
#     send_message(number, msg)



### Gmail
# import smtplib
# from email.message import EmailMessage
# from myData import sender_password

# def send_email(subject, body, to_email):
#     sender_email = 'გამგზავნის@gmail.com'   
#     smtp_server = 'smtp.gmail.com'

#     message = EmailMessage()
#     message['From'] = sender_email
#     message['To'] = to_email
#     message['Subject'] = subject
#     message.set_content(body)

# ## sender_password ==> Manage your Google Account ==> App Password
#     with smtplib.SMTP_SSL(smtp_server, 465) as server:
#         server.login(sender_email, sender_password)
#         server.send_message(message)

# if __name__ == '__main__':
#     subject = 'სათაური'
#     body = f'მესიჯი'
#     to_email = 'მიმღების მეილი' 
#     send_email(subject, body, to_email)




### Parsing

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.lit.ge/index.php?page=books&send[shop.catalog][order]=1&send[shop.catalog][reset]=1'
#
# r = requests.get(url)
# print(r)
# print(r.headers['Content-Type'])
#print(r.text)
# content = r.text
#
# soup = BeautifulSoup(content, 'html.parser')
# section = soup.find('section', {'class':'list-holder'})
# books = section.find_all('article')
#
# for book in books:
#     t_bar = book.find('div', {'class':'title-bar'})
#     title = t_bar.a.text
#     author = t_bar.b.a.text
#     price = book.button.text.strip()
#
#     print(title,author,price)
#


####
# f = open('books.csv', 'w', encoding='utf-8_sig')
# f.write('სათაური,ავტორი,ფასი\n')

# h = {'user_agent': 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
#      }
# for i in range(1, 100):
#     url = f'https://www.lit.ge/index.php?page=books&send[shop.catalog][page]={i}'

#     r = requests.get(url, headers=h)
#     content = r.text

#     soup = BeautifulSoup(content, 'html.parser')
#     section = soup.find('section', {'class':'list-holder'})
#     books = section.find_all('article')

#     for book in books:
#         t_bar = book.find('div', {'class':'title-bar'})
#         title = t_bar.a.text.replace(',', '')
#         author = t_bar.b.a.text
#         price = book.button.text.strip()

#         f.write(title + ',' + author + ',' + price + '\n')


# ganatleba
# import requests
# from bs4 import BeautifulSoup
# import sqlite3
# import time

# # საიტზე მოთხოვნის გაგზავნისას ბრაუზერისგან მოთხოვნის გაგზავნის იმიტაცია
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/135.0.0.0 Safari/537.36'
# }

# BASE_URL = 'https://www.08.ge/organizations/filter/ganatleba-metsniereba?category=12&page={}'

# DB_NAME = 'organizations.db'


# def init_db():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS organizations (
#             id      INTEGER PRIMARY KEY AUTOINCREMENT,
#             name    TEXT NOT NULL,
#             phone   TEXT,
#             email   TEXT,
#             website TEXT
#         )
#     """)

#     conn.commit()
#     return conn


# def save_to_db(conn, org):
#     cursor = conn.cursor()

#     cursor.execute("""
#         INSERT INTO organizations (name, phone, email, website)
#         VALUES (:name, :phone, :email, :website)
#     """, org)

#     conn.commit()


# def get_max_page(soup):
#     pagination = soup.find('div', class_='pagination py-8 mb-10')

#     if pagination:
#         try:
#             return int(pagination.text.strip().split('\n')[-1])
#         except ValueError:
#             return 1

#     return 1


# def parse_card(card_url):
#     try:
#         resp = requests.get(card_url, headers=HEADERS, timeout=1)
#         resp.raise_for_status()
#     except requests.RequestException as e:
#         print(f'ვერ ჩაიტვირთა {card_url}: {e}')
#         return None

#     soup = BeautifulSoup(resp.text, 'html.parser')

#     # ორგანიზაციის სახელი
#     h1 = soup.find('h1', class_='title text-bold small text-white mb-2')
#     name = h1.text.strip() if h1 else 'უცნობი'

#     # ტელეფონის ნომერი
#     phone_tag = soup.find('a', class_='text medium text-success')
#     phone = phone_tag.text.strip() if phone_tag else None

#     # email და ვებ გვერდი ერთი და იმავე კლასშია
#     # ამიტომ find_all-ით ყველას ვიღებთ და href-ით ვარჩევთ
#     email, website = None, None
#     for a in soup.find_all('a', class_='text text-secondary'):
#         href = a.get('href', '')
#         span = a.find('span')
#         text = span.text.strip() if span else a.text.strip()

#         if href.startswith('mailto:'):
#             # mailto: პრეფიქსი email-ს ნიშნავს
#             email = text
#         elif href.startswith('http') or href.startswith('www'):
#             # http ან www პრეფიქსი ვებ მისამართს ნიშნავს
#             website = text

#     return {'name': name, 'phone': phone, 'email': email, 'website': website}


# def scrape(max_pages=None):
#     conn = init_db()
#     results = []

#     # პირველ გვერდს ტვირთავს მხოლოდ გვერდების რაოდენობის გასარკვევად
#     first_resp = requests.get(BASE_URL.format(1), headers=HEADERS, timeout=1)
#     first_soup = BeautifulSoup(first_resp.text, 'html.parser')
#     container = first_soup.find('div', class_='lg-9 md-9 sm-8 xs-12 py-6')
#     total_pages = get_max_page(container)

#     # თუ max_pages მითითებულია, იმ რაოდენობის გვერდის ინფორმაციას აიღებს
#     if max_pages:
#         total_pages = min(total_pages, max_pages)

#     print(f'სულ გვერდი: {total_pages}')

#     for page in range(1, total_pages + 1):
#         print(f'\n[გვერდი {page}/{total_pages}]')

#         # მიმდინარე გვერდს ტვირთავს
#         resp = requests.get(BASE_URL.format(page), headers=HEADERS, timeout=10)
#         soup = BeautifulSoup(resp.text, 'html.parser')

#         # მთავარ კონტეინერს პოულობს, სადაც ქარდებია განთავსებული
#         container = soup.find('div', class_='lg-9 md-9 sm-8 xs-12 py-6')
#         cards_div = container.find('div', class_='row pt-0')

#         for card in cards_div.find_all('div', class_='md-4'):
#             a_tag = card.find('a')

#             # სადაც ინფორმაცია არ მოიძებნება - გამოტოვოს
#             if not (a_tag and a_tag.get('href')):
#                 continue

#             # ქარდის URL-ზე გადადის და ინფორმაციას პარსავს
#             org = parse_card(a_tag['href'])

#             if org:
#                 save_to_db(conn, org)
#                 results.append(org)
#                 print(f"{org['name']} | {org['phone']} | {org['email']} | {org['website']}")

#             # სერვერზე დატვირთვის შესამცირებლად პაუზა თითო მოთხოვნას შორის
#             time.sleep(0.1)

#     conn.close()
#     return results


# if __name__ == '__main__':
#     orgs = scrape(max_pages=5)
#     print(f'\nსულ: {len(orgs)} ორგანიზაცია')
#     print(f'მონაცემები შენახულია: {DB_NAME}')
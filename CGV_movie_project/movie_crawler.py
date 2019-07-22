import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler


bot = telegram.Bot(token='803288229:AAF3jcyErpuDmvg2Ga9yDaZ9Djd0_9tv7vE')


def job_function():
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190718"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if (imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=705760272, text=title + "의 IMAX 예매가 열렸습니다.")
        sched.pause()


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()

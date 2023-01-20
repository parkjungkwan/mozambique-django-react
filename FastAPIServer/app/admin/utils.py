from datetime import datetime
import pytz


def current_time():
    return f"{datetime.now(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')}"

def utc_seoul():
    return datetime.now(pytz.timezone('Asia/Seoul'))


from datetime import datetime

from random import randrange
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def between_random_date():
    d1 = datetime.strptime('1988-1-1', '%Y-%m-%d')
    d2 = datetime.strptime('2005-12-31', '%Y-%m-%d')
    target = str(random_date(d1, d2))
    return target.split()[0]

def paging(page: int, row_cnt: int): # row_cnt = UserCrud(db).count_all_users()
    page_size = 10
    t = row_cnt // page_size
    t2 = row_cnt % page_size
    page_cnt = t if (t2 == 0) else t + 1
    t3 = page_cnt // page_size
    block_size = 10
    t4 = page_cnt % block_size
    block_cnt = t3 if (t4 == 0) else t3 + 1
    page_now = page
    row_start = page_size * (page_now - 1)
    block_now = page_now // block_size
    row_end = row_start + (page_size - 1) if page_now != page_cnt else row_cnt - 1
    page_start = block_now * block_size
    page_end = page_start + (block_size -1 ) if block_now != (block_cnt - 1) else page_cnt

    print("### 테스트 ### ")
    print(f"row_start ={row_start}")
    print(f"row_end ={row_end}")
    print(f"page_start ={page_start}")
    print(f"page_end ={page_end}")

if __name__ == '__main__':
    print(f"랜덤 생일 : {between_random_date()}")

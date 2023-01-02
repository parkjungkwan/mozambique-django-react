import warnings
warnings.filterwarnings("ignore")
import pandas_datareader.data as web
from pandas_datareader import data
import yfinance as yf
yf.pdr_override() # TypeError: string indices must be integers 해결법
path = "c:/Windows/Fonts/malgun.ttf"
import platform
from matplotlib import font_manager, rc, pyplot as plt

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
plt.rcParams['axes.unicode_minus'] = False
class AiTraderService(object):

    def __init__(self):
        global start_date, end_date, item_code
        start_date = "2018-1-4"
        end_date = '2021-9-30'
        item_code = '000270.KS'

    def hook(self):
        KIA = data.get_data_yahoo('000270.KS', "2018-1-4", '2021-9-30')
        print(f" KIA head: {KIA.head(3)}")
        print(f" KIA tail: {KIA.tail(3)}")

if __name__ == '__main__':
    ai = AiTraderService()
    ai.hook()


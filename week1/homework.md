# 作业汇总
# 作业任务：
完成一个最简天气查询程序，运行在命令行界面，实现以下功能：

输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
所用天气数据见 https://github.com/AIHackers/Py101-004/tree/master/Chap1/resource 中 weather_info.txt 文件。


# 大船:

整体思想：封装天气查询功能到一个类中。
```Python
import csv
from sys import exit

class WeatherSearcher(object):
    def __init__(self):
        self.data_init()
        self._history = ""

    def data_init(self):
        self._data = {}
        with open('../resource/weather_info.txt', 'r') as f:
            for line in f:
                tmp = line.strip().split(',')
                self._data[tmp[0]] = tmp[1]

    def get_weather(self, city_to_search):
        if city_to_search in self._data.keys():
            weather = self._data[city_to_search]
            self._history += city_to_search + " " + weather + "\n"
            return weather
        else:
            return None

    def get_help(self):
        help_info = '''
            输入城市名，查询该城市的天气数据；
            输入help或者h，获得帮助信息；
            输入history，显示查询历史；
            输入quit, 退出程序。
            '''
        return help_info

    def get_history(self):
        return self._history


def run():
    # 初始化城市天气搜索类
    weather_searcher = WeatherSearcher()
    while True:
        city_to_search = input("请输入指令和你要查询的城市名: ")
        # 输入矫正
        city_to_search = city_to_search.replace(" ", "")
        # 判断输入内容
        if city_to_search == "quit":
            print("再见！")
            exit()
        elif city_to_search in ["help", "h"]:
            print(weather_searcher.get_help())
        elif city_to_search == "history":
            print(weather_searcher.get_history())
        else:
            weather = weather_searcher.get_weather(city_to_search)
            if weather is not None:
                print("{city}的天气状况为{weather}".format(city=city_to_search,
                weather=weather))
            else:
                print("你要查找的城市没有找到，请重新输入!可以输入help或者h查看帮助信息。")


if __name__ == "__main__":
    run()



```

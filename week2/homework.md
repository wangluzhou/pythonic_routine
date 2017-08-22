# 大船

这次作业比较深刻的感受到自己程序框架的问题。想在周末进行一些改进。
- 应该把用户进行封装
- 将API连接部分进行完全模块化，应对API的变更
- 对命令进行封装

当前版本:

### Project tree
- api/
 - const_value.py
 - helper.py
- weather_search.py

```Python
from sys import exit
import requests
from api.const_value import API, KEY, UNIT, LANGUAGE, LOCATION
from api.helper import getLocation

class WeatherSearcher(object):
    def __init__(self):
        self._history = []

    def get_weather(self, city_to_search):
        import json
        result = requests.get(API, params={
            'key': KEY,
            'location': city_to_search,
            'language': LANGUAGE,
            'unit': UNIT
        }, timeout=1)
        try:

            data = (json.loads(result.text)) # data为dict类型
            if "status" in data:
                return None
            data = data["results"][0] # 获取主干信息，类型为字典
            response_info = data["location"]["name"] + " " + data["now"]["text"] +"\n" + data["last_update"]
            self._history.append(response_info)
            return response_info
        except BaseException as err:
            raise
            print("API查询异常!")
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
        try:
            city_to_search = input("请输入指令和你要查询的城市名: ")
        except BaseException as err:
            print("你的输入导致系统报错，gg")
            exit(0)
        # 输入矫正
        city_to_search = city_to_search.replace(" ", "")
        # 判断输入内容
        if city_to_search == "quit":
            print("再见！")
            exit(0)
        elif city_to_search in ["help", "h"]:
            print(weather_searcher.get_help())
        elif city_to_search == "history":
            print(weather_searcher.get_history())
        else:
            response_info = weather_searcher.get_weather(city_to_search)
            if response_info is not None:
                print(response_info)
            else:
                print("你要查找的城市没有找到，或者API异常，请重新输入!可以输入help或者h查看帮助信息。")


if __name__ == "__main__":
    run()

```

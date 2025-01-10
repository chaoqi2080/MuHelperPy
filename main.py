import logging
import random
import time
import pyautogui

from auto_kill_monster import kill_monster
from auto_recycle import auto_recycle
from config import read_config_from_file


def do_auto_kill_monster(g_config_pos):
    kill_boss_time = time.time()
    internal_time = g_config_pos['boss'][4] * 60

    while True:
        for golden in g_config_pos['golden']:
            kill_monster(
                [golden[0], golden[1]],
                golden[2],
                golden[3],
                g_config_pos
            )

            if (time.time() - kill_boss_time) > internal_time:
                kill_monster(
                    [g_config_pos['boss'][0], g_config_pos['boss'][1]],
                    g_config_pos['boss'][2],
                    g_config_pos['boss'][3],
                    g_config_pos
                )
                kill_boss_time = time.time()

            if random.randint(0, 100) >= 50:
                auto_recycle(g_config_pos)


def get_frame_pos():
    tips_array = [
        "<最左边位置>的坐标",
        "<最右上的小地图>坐标",
        "<自动杀怪>坐标",
        "<背包>坐标",
        "<整理>坐标",
        "<回收>坐标",
        "<确认回收>坐标",
    ]

    while True:
        for tip in tips_array:
            logging.info("开始校准 ========= %s =========", tip)
            for _ in range(10):
                x, y = pyautogui.position()
                logging.info("%s => x = %d, y = %d", tip, x, y)
                time.sleep(0.5)
            time.sleep(2)


def main():
    logging.basicConfig(level=logging.INFO)
    g_config_pos = read_config_from_file("config.json")

    if not g_config_pos:
        logging.error("读取坐标配置文件失败")
        return

    time.sleep(3)

    if g_config_pos.get('is_get_pos', False):
        get_frame_pos()
        return

    do_auto_kill_monster(g_config_pos)


# 检查是否是主模块运行
if __name__ == "__main__":
    main()

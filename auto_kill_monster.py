import logging
import time

from mouse import move_to_position, signal_left_click, double_left_click


def op_map(msg, g_config_pos):
    move_to_position(
        [
            g_config_pos['recycle'][0][0], g_config_pos['recycle'][0][1] - 150
        ],
        msg
    )
    signal_left_click()


def open_big_map(g_config_pos):
    op_map("点小地图--打开大地图", g_config_pos)


def close_big_map(g_config_pos):
    op_map("点小地图--关闭大地图", g_config_pos)


def click_golden_monster_pos_in_big_map(golden_monster_pos, move_time_between_monster, g_config_pos):
    move_to_position(
        [golden_monster_pos[0], golden_monster_pos[1]],
        f"在大地图中点黄金怪坐标, 耗时 = {move_time_between_monster}"
    )
    double_left_click()
    close_big_map(g_config_pos)
    logging.info(
        "玩家需要移动到 = [%d, %d], 耗时 = %d 秒",
        golden_monster_pos[0], golden_monster_pos[1], move_time_between_monster
    )
    time.sleep(move_time_between_monster)


def click_auto_button(time_left_for_kill_monster, g_config_pos):
    move_to_position(
        [g_config_pos['auto'][0], g_config_pos['auto'][1]],
        "点自动打怪"
    )
    signal_left_click()
    logging.info("玩家开始自动杀怪, 预计耗时 = %d 秒", time_left_for_kill_monster)
    time.sleep(time_left_for_kill_monster)


def kill_monster(golden_monster_pos, time_left_for_kill_monster, move_time_between_monster, g_config_pos):
    if len(golden_monster_pos) != 2:
        logging.error("传入的黄金怪坐标数据有问题")
        return

    open_big_map(g_config_pos)
    click_golden_monster_pos_in_big_map(golden_monster_pos, move_time_between_monster, g_config_pos)
    click_auto_button(time_left_for_kill_monster, g_config_pos)
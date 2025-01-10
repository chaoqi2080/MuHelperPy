from mouse import move_to_position, signal_left_click, double_left_click

recycle_str_array = [
    "背包", "整理", "回收", "确认回收",
]


def auto_recycle(g_config_pos):
    for i in range(len(recycle_str_array)):
        move_to_position(
            [
                g_config_pos['recycle'][i][0], g_config_pos['recycle'][i][1]
            ],
            f"回收--{recycle_str_array[i]}"
        )
        signal_left_click()

    # 点击关闭按钮
    move_to_position(
        [
            g_config_pos['recycle'][0][0] - 900, g_config_pos['recycle'][0][1]
        ],
        "回收--点关闭按钮"
    )
    double_left_click()




import json
import logging


def read_config_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as config_file:
            data = json.load(config_file)
            logging.info("读取文件成功 %s", data)
            return data
    except FileNotFoundError as e:
        logging.error("打开配置文件错误 %s", str(e))
        return None
    except json.JSONDecodeError as e:
        logging.error("解析 json 文件失败 %s", str(e))
        return None
    except Exception as e:
        logging.error("读取配置文件数据失败 %s", str(e))
        return None

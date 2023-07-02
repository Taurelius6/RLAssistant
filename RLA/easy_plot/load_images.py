# Created by xionghuichen at 2023/7/2
# Email: chenxh@lamda.nju.edu.cn

from typing import Dict, List, Tuple, Type, Union, Optional, Callable


def load_saved_images(data_root:str, task_table_name:str, regs:list, img_names:list, hp_filter_dict: Optional[dict] = None):
    """

    :param data_root:
    :type data_root:
    :param task_table_name:
    :type task_table_name:
    :param regs:
    :type regs:
    :param hp_filter_dict: a dict to filter your log.
    e.g., hp_filter_dict= {'learning_rate': [0.001, 0.01, 0.1]} will select the logs where the learning rate is 0.001, 0.01, or 0.1.
    :return:
    :rtype:
    """

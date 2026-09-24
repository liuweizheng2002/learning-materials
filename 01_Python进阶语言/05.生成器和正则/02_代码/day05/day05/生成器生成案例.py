
"""
案例: 基于传入的数值(每批次的歌词条数), 创建 生成器, 生成批次歌词.
"""
import math, time

# 需求： 基于文件中周杰伦的歌词，创建生成器

def dataset_loader(batch_size):
    # 读取文件数据
    # while True:
        with open('./data/jaychou_lyrics.txt', 'r', encoding='utf-8') as src_f:
            # 一次性读取全部行
            lines = [line.strip() for line in src_f.readlines()]
            # lines = src_f.readlines()

            # 计算批次总数  batch_size = 8,是你设定的读取行数，这里是总数 % 8 等于批次数
            total_batch = math.ceil(len(lines) / batch_size)
            # math.ceil 向上取整，这里处理的是尾部

            for idx in range(total_batch):
                # idx = 0, 1, 2, 3, 4, 5, 6, 7, 8
                # 第1批歌词，批次索引(idx=0)，歌词为：第1条 ~ 第8条，索引为：0 ~ 7
                yield lines[idx * batch_size: idx * batch_size + batch_size]


if __name__ == '__main__':
    dl = dataset_loader(10)
    # print(next(dl))
    # 实现效果：一次取一批，一批有8行歌词

    for batch_data in dl:
        time.sleep(0.3)
        print(batch_data)
    # 循环便利全部批次 的全部行歌词








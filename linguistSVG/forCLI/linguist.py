from decimal import Decimal, ROUND_HALF_UP

from linguistSVG.common.du import get_sizes_per_lang
from linguistSVG.common.config import settings

def round(f: float, precision: str):
    return float(Decimal(str(f)).quantize(Decimal(precision), rounding=ROUND_HALF_UP))

path = settings.get('path', None)
if path is None:
    print('Error. "confing.py / settings / path" not found')
    exit()

width = 100

sizes_dict = get_sizes_per_lang(path)
size_sum = sum(size for size in sizes_dict.values()) # 容量の合計
# print(sizes_list) # debug
for lang, size in sizes_dict.items(): # 割合(四捨五入したもの)に変換
    sizes_dict[lang] = round(size / size_sum * width, '0.1')

sizes_list = sorted(sizes_dict.items(), key=lambda x:x[1], reverse=True) # 降順ソートしてリスト化
# グラフを表示
for lang, size in sizes_list:
    # print(lang[0] * int(round(size, '0')), end='')
    r, g, b = settings['langs'][lang][0] # todo 例外処理すべき
    print(f'\033[48;2;{r};{g};{b}m' + ' ' * int(round(size, '0')) + '\033[0m', end='')
print()
# 言語とその割合を表示
for lang, size in sizes_list:
    if size != 0:
        r, g, b = settings['langs'][lang][0] # todo 例外処理すべき
        print(f'\033[38;2;{r};{g};{b}m●\033[0m {lang} {size}%')
print()

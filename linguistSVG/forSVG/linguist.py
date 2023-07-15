from decimal import Decimal, ROUND_HALF_UP

from linguistSVG.common.du import get_sizes_per_lang
from linguistSVG.common.config import settings
from .mylib.SVG4Python.svg4py.svg import SVG, RGB

def round(f: float, precision: str):
    return float(Decimal(str(f)).quantize(Decimal(precision), rounding=ROUND_HALF_UP))

path = settings.get('path', None)
if path is None:
    print('Error. "confing.py / settings / path" not found')
    exit()

sizes_dict = get_sizes_per_lang(path)
size_sum = sum(size for size in sizes_dict.values()) # 容量の合計
# print(sizes_list) # debug
for lang, size in sizes_dict.items(): # 割合(四捨五入したもの)に変換
    sizes_dict[lang] = size / size_sum

sizes_list = sorted(sizes_dict.items(), key=lambda x:x[1], reverse=True) # 降順ソートしてリスト化

# SVGファイルの生成
width = 1000
char_size = 10
bar_height = char_size
background_color = RGB(0, 0, 0)
svg = SVG('linguist.svg', 0, 0, width, bar_height + char_size * sizes_list.__len__(), unit='px')
svg.rect(0, 0, '100%', '100%', background_color, stroke_width=0)
# グラフを表示
pen_x = 0
for lang, size in sizes_list:
    r, g, b = settings['langs'][lang][0] # todo 例外処理すべき
    # print(f'\033[48;2;{r};{g};{b}m' + ' ' * int(round(size, '0')) + '\033[0m', end='')
    svg.line(pen_x, char_size / 2, pen_x + size * width, char_size / 2, RGB(r, g, b), width=char_size)
    pen_x += size * width
print()
# 言語とその割合を表示
for i, (lang, size) in enumerate(sizes_list):
    if size != 0:
        r, g, b = settings['langs'][lang][0] # todo 例外処理すべき
        print(f'\033[38;2;{r};{g};{b}m●\033[0m {lang} {size}%')
        svg.circle(char_size / 2, bar_height + char_size * i + char_size / 2, char_size / 2, RGB(r, g, b), stroke_width=0)
        svg.text(char_size, bar_height + char_size * i + char_size, f"{lang} {round(size * 100, '0.1')}%", font_size=char_size, fill_color=RGB(255, 255, 255), stroke_width=0)
print()


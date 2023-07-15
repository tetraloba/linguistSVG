import subprocess
from os import chdir, getcwd

from .config import settings
from .suffix import func

def get_sizes_per_lang(path: str) -> dict:

    # カレントディレクトリの操作と表示
    # print('now directory is ' + getcwd()) # debug
    chdir(path)
    # print('now directory is ' + getcwd()) # debug

    # 各言語の容量を計測 (find -name "*.EXT" | xargs du -c | tail -n 1 | cut -f1)
    sizes = dict() # 言語:容量
    for lang, prop in settings['langs'].items():
        for ext in prop[1]:
            cp = subprocess.run(['find', '-name', f'*.{ext}'], capture_output=True, text=True)
            # print(cp.stdout) # debug
            if cp.stdout == '': # 該当するファイルが見つからない場合は容量0
                size = 0
                break
            cp = subprocess.run(['xargs', 'du', '-ch', '--apparent-size'], input=cp.stdout, capture_output=True, text=True)
            # print(cp.stdout) # debug
            cp = subprocess.run(['tail', '-n 1'], input=cp.stdout, capture_output=True, text=True) # 最終行を取り出す
            # print(cp.stdout) # debug
            cp = subprocess.run(['cut', '-f1'], input=cp.stdout, capture_output=True, text=True)
            # print(lang, cp.stdout) # debug
            size = func(cp.stdout.strip()) # コマンドの結果(接尾辞付きの文字列)を 接尾辞なしのfloat型に変換
            sizes[lang] = size + sizes.get(lang, 0)
    # for key, value in sizes.items():
    #     print(key, value) # debug
    return sizes

if __name__ == '__main__':
    get_sizes_per_lang()

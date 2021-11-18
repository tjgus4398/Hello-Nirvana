import os
import time
from typewriter import typewriter
import pyautogui

def run():
    os.system("clear")
    typewriter('Enter "Hello Nirvana":')
    user_input = input()

    if user_input == "Hello Nirvana":
        time.sleep(0.5)
        typewriter(". . . " + user_input)
        typewriter("\n관세음보살님! 감사합니다!" * 3)
        typewriter("\n시방세계에 충만하신 관세음보살님이시여, 세세생생 지은 죄업을 모두 참회드리옵니다. 이제 이 경을 읽는 공덕을 선망조상과 일체중생의 행복을 위해 바칩니다. 아울러 저희 가족 모두가 건강하옵고, 하는 일이 다 순탄하여지이다." * 3)
        typewriter("\n옴 아라남 아라다" * 3)
        typewriter("\n나무실상묘법연화경 관세음보살보문품" * 3)
        return

    else:
        typewriter('Enter "Hello Nirvana" correctly.')
        time.sleep(0.5)
        os.system("clear")
        run()

run()

# tmux 진입 - coin.py 실행
os.system("clear")
os.system('tmux attach -t 0 \; send-keys "python3 hello_nirvana.py" Enter')

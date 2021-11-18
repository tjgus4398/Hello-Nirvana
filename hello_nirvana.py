from hashlib import sha256    
from typewriter import typewriter
import time, os
import pyautogui

scripture = '이시 무진의보살 즉종좌기 편단우견 합장향불 이작시언. “세존, 관세음보살 이하인연 명관세음”\n\
불고 무진의보살.\n\
“선남자, 약유무량백천만억중생 수제고뇌 문시관세음보살 일심칭명 관세음보살 즉시 관기음성 개득해탈.\n\
약유지시관세음보살명자 설입대화 화불능소 유시보살 위신력고, 약유대수소표 칭기명호 즉득천처,\n\
약유백천만억중생 위구금은 유리 자거 마노 산호 호박 진주 등보 입류대해 가사흑풍 취기선방 표타나찰귀국\n\
기중 약유재지일인 칭관세음보살명호 시제인등 개득해탈 나찰지난 이시인연 관세음.\n\
약부유인 임당피해 칭관세음보살명자 피소집도장 심단단괴 이득해탈,\n\
약삼천대천국토 만중 야차나찰 욕래뇌인 문기칭관세음보살명자 시제악귀 상불능이악안시지 황부가해.\n\
설부유인 약유죄 약무죄 추계가쇄 검계기신 칭관세음보살명자 대실단괴 즉득해탈.\n\
약삼천대천국토 만중원적 유일상주 장제상인 재지중보 경과험로 기중일인 작시창언,\n\
“제선남자, 물득공포 여등 응당일심 칭관세음보살명호.\n\
시보살 능이무외 시어중생, 여등 약칭명자 어차원적 당득해탈.”\n\
중상인 문 구발성언 ‘나무관세음보살’ 칭기명고 즉득해탈. 무진의, 관세음보살마하살 위신지력 외외여시.\n\
약유중생 다어음욕 상념공경 관세음보살 변득이욕.\n\
약다진에 상념공경 관세음보살 변득이욕 약다우치 상념공경 관세음보살 변득이치.\n\
무진의, 관세음보살 유여시등대위신력 다소요익, 시고 중생 상응심념.\n\
\n\
약유여인 설욕구남 예배공양 관세음보살 변생복덕지혜지남, 설욕구녀 변생단정유상지녀 숙식덕본 중인 애경.\n\
무진의, 관세음보살 유여시력.\n\
약유중생 공경예배 관세음보살 복불당연 시고 중생 개응수지 관세음보살명호.\n\
무진의, 약유인 수지 육십이억항하사 보살명자,\n\
부진형 공양음식의복와구의약 어여의운하. 시선남자선녀인 공덕 다부”\n\
무진의언. “심다 세존”\n\
불언. “약부유인 수지관세음보살명호 내지 일념 예배공양 시이인 복 정등무이 어백천만억겁 불가궁진.\n\
무진의, 수지관세음보살명호 득여시무량무변복덕지리.”\n\
\n\
무진의보살 백불언. “세존, 관세음보살 운하유차사바세계 운하이위중생설법 방편지력 기사운하”\n\
불고 무진의보살. “선남자, 약유국토중생 응이불신 득도자 관세음보살 즉현불신 이위설법,\n\
응이벽지불신 득도자 즉현벽지불신 이위설법, 응이성문신 득도자 즉현성문신 이위설법,\n\
응이범왕신 득도자 즉현범왕신 이위설법, 응이제석신 득도자 즉현제석신 이위설법,\n\
응이자재천신 득도자 즉현자재천신 이위설법, 응이대자재천신 득도자 즉현대자재천신 이위설법,\n\
응이천대장군신 득도자 즉현천대장군신 이위설법, 응이비사문신 득도자 즉현비사문신 이위설법,\n\
응이소왕신 득도자 즉현소왕신 이위설법, 응이장자신 득도자 즉현장자신 이위설법,\n\
응이거사신 득도자 즉현거사신 이위설법, 응이재관신 득도자 즉현재관신 이위설법,\n\
응이 바라문신 득도자 즉현바라문신 이위설법,\n\
응이비구비구니 우바새 우바이신 득도자 즉현비구비구니 우바새 우바이신 이위설법,\n\
응이장자 거사 재관바라문 부녀신 득도자 즉현부녀신 이위설법,\n\
응이동남동녀신 득도자 즉현동남동녀신 이위설법,\n\
응이천룡야차 건달바 아수라 가루라 긴나라 마후라가 인비인등신 득도자 즉개현지 이위설법,\n\
응이집금강신 득도자 즉현집금강신 이위설법\n\
무진의, 시관세음보살 성취여시공덕 이종종형 유제국토 도탈중생. 시고 여등 응당일심 공양관세음보살.\n\
시관세음보살마하살 어포외급난지중 능시무외, 시고 차사바세계개호지 <위시무외자>."\n\
무진의보살 백불언. “세존, 아금 당공양관세음보살” 즉해경중보주영락가치백천양금 이이여지 작시언.\n\
“인자, 수차법시진보영악” 시 관세음보살 불긍수지, 무진의 부차 관세음보살언.\n\
“인자, 민아등고 수차영락” 이시 불고 관세음보살.\n\
“당민차 무진의보살 급사중천룡 야차 건달바 아수라 가루라 긴나라 마후라가 인비인등고 수지영락.”\n\
즉시 관세음보살 민제사중 급어천룡 인비인등 수기영락 분작이분 일분 봉석가모니불 일분 봉다보불탑.\n\
“무진의, 관세음보살 유여시자재신력 유어사바세계."\n\
\n\
이시 무진의보살 이게문왈. “세존묘상구 아금중문피 불자하인연 명위관세음\n\
구족묘상존 게답무진의.\n\
“여청관음행 선응제방소. 홍서심여해 역겁불사의 시다천억불 발대청정원.\n\
아위여약설 문명급견신 심념불공과 능멸제유고.\n\
가사홍해의 추락대화갱 염피관음력 화갱변성지. 혹표류거해 용어제귀난 염피관음력 파랑불능몰.\n\
혹재수미봉 위인소추타 염피관음력 여일허공주. 혹피악인축 타락금강산 염피관음력 불능손일모.\n\
혹치원적요 각집도가해 염피관음력 함즉기자심. 혹조왕난고 임형욕수종 염피관음력 도심단단괴.\n\
혹수금가죄 수족피추계 염피관음력 석연득해탈. 주저제독약 소욕해신자 염피관음력 환착어본인.\n\
혹우악나찰 독룡제귀등 염피관음력 시실불감해. 약악수위요 이아조가포 염피관음력 질주무변방.\n\
완사급복갈 기독연화연 염피관음력 심성자회거. 운뢰고철전 강박주대우 염피관음력 응시득소산.\n\
중생피곤액 무량고핍신 관음묘지력 능구세간고. 구족신통력 광수지방편 시방제국토 무찰불현신.\n\
종종제악취 지옥귀축생 생로병사고 이점실영멸. 진관청정관 광대지혜관 비관급자관 상원상첨앙.\n\
부구청정광 혜일파제암 능복재풍화 보명조세간. 비체계뇌진 자의묘대운 주감로법우 멸제번뇌염.\n\
쟁송경관처 포외군진중 염피관음력 중원실퇴산. 묘음관세음 범음해조음 승피세간음 시고수상념.\n\
염념물생의 관세음정성 어고뇌사액 능위작의호. 구일체공덕 자안시중생 복취해무량 시고응정례.”\n\
이시 지지보살 즉종좌기 전백불언\n\
“세존, 약유중생 문시관세음보문품 자재지업 보문시현 신통력자 당지시인 공덕불소."\n\
불설시보문품시 중중 팔만사천중생 개발무등등아뇩다라삼먁삼보리심.\n'
scripture_word = list(scripture)

blockchain = []

############################
# difficulty 몇 번 실행했는지로 멈추기
# total_time 걸린 시간의 총합으로 멈추기
############################

start_time = time.time()

def add_genesis_block():
    for word in scripture_word:
        data = word
        prev_hash = ''
        nonce, current_hash = make_hash(data, prev_hash, difficulty)
        add_block(data, prev_hash, difficulty, nonce, current_hash)
    show_blockchain()


def make_hash(data: str, prev_hash: str, difficulty_: int) -> (int, str):
    new_hash = ' ' * difficulty_
    checker = '0' * difficulty_
    nonce = 0
    while new_hash[:difficulty_] != checker:
        new_hash = sha256((data + str(nonce) + prev_hash).encode()).hexdigest()
        nonce += 1
    return nonce, new_hash


def add_block(data, prev_hash, difficulty_, nonce, current_hash):
    blockchain.append((data, prev_hash, difficulty_, nonce, current_hash))


def add_normal_block():
    if difficulty > 1: 
        return
    for word in scripture_word:
        data = word
        _, _, _, _, prev_hash = blockchain[-1]
        nonce, current_hash = make_hash(data, prev_hash, difficulty)
        add_block(data, prev_hash, difficulty, nonce, current_hash)
    show_blockchain()
    add_normal_block() 


def show_blockchain():
    print('-' * 50 + '\n')
    if len(blockchain) > len(scripture):
        del blockchain[:len(scripture)]
    for i, (data, prev_hash, difficulty_, nonce, current_hash) in enumerate(blockchain):
        if prev_hash == '':
            blockn = i
        else:
            blockn = i + len(scripture) * (difficulty_-1) 
        typewriter(f'Block {blockn}\n'
            # f'{data}, {difficulty_}\n' 
            # f'{prev_hash}\n'
            f'Word of God: {current_hash}\n' 
            f'Revelation: {nonce}\n'
            f'Chanting took {time.time() - start_time}s!\n')

    show_blockchain.counter += 1
    ### difficulty == loop_counter ###
    global difficulty
    difficulty = show_blockchain.counter

os.system("clear")

show_blockchain.counter = 0
show_blockchain()
typewriter('Prayer Start')

pyautogui.hotkey("ctrl", "b")
pyautogui.press("%")
os.system('tmux send-keys "python3 chanting.py" Enter')

add_genesis_block() 
add_normal_block() 

end_time = time.time()
typewriter(f'Total praying took {end_time - start_time}s!\n')
time.sleep(1.5)
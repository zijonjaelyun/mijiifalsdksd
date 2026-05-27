import streamlit as st
import time

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 과몰입 팩폭기", page_icon="🔮", layout="centered")

# --- MBTI 데이터 사전 (팩폭 & 궁합) ---
mbti_data = {
    "INTJ": {"name": "용의주도한 전략가", "fact": "남한테 관심 없음. 효율성 집착광공. '왜?'라는 말 달고 삼.", "best": "ENFP", "worst": "ESFJ"},
    "INTP": {"name": "논리적인 사색가", "fact": "귀찮음이 사람으로 태어나면 INTP. 지적 호기심은 높은데 실행력은 0.", "best": "ENTJ", "worst": "ESFJ"},
    "ENTJ": {"name": "대담한 통솔자", "fact": "타고난 꼰대력(좋은 의미로). 목표 달성 못하면 스스로 스트레스 오지게 받음.", "best": "INTP", "worst": "ISFP"},
    "ENTP": {"name": "뜨거운 논쟁을 즐기는 변론가", "fact": "말싸움 지는 거 못 참음. 관심사 수시로 바뀜. '아 근데~'가 입버릇.", "best": "INFJ", "worst": "ISFJ"},
    "INFJ": {"name": "선의의 옹호자", "fact": "속마음 절대 다 안 보여줌. 겉으로는 웃고 있는데 속으로 사람 급 나누고 있음.", "best": "ENFP", "worst": "ESTP"},
    "INFP": {"name": "열정적인 중재자", "fact": "망상 장인. 멘탈 개복치. 오늘 할 일 내일로 미루기의 달인.", "best": "ENFJ", "worst": "ESTJ"},
    "ENFJ": {"name": "정의로운 사회운동가", "fact": "인류애 넘치는데 상처도 잘 받음. 남 챙기느라 내 실속 못 챙김.", "best": "INFP", "worst": "ISTP"},
    "ENFP": {"name": "재기발랄한 활동가", "fact": "새로운 거 시작만 잘함. 금사빠 금사식. 리액션 봇.", "best": "INTJ", "worst": "ISTJ"},
    "ISTJ": {"name": "청렴결백한 논리주의자", "fact": "원칙주의자. 갑작스러운 약속 취소 개좋아함. 기억력 쓸데없이 좋음.", "best": "ESFP", "worst": "ENFP"},
    "ISFJ": {"name": "용감한 수호자", "fact": "착한 아이 증후군. 남 눈치 엄청 봄. 속앓이 혼자 다 함.", "best": "ESTP", "worst": "ENTP"},
    "ESTJ": {"name": "엄격한 관리자", "fact": "호불호 확실함. 융통성 제로. 일 못하는 사람 보면 속에서 천불 남.", "best": "INTP", "worst": "INFP"},
    "ESFJ": {"name": "사교적인 외교관", "fact": "오지랖 태평양. 남 이야기 듣는 거 좋아함. 인정 욕구 덩어리.", "best": "ISFP", "worst": "INTJ"},
    "ISTP": {"name": "만능 재주꾼", "fact": "마이웨이 끝판왕. 카톡 읽씹 잘함. 효율 따져서 최소한의 노력만 함.", "best": "ESFJ", "worst": "ENFJ"},
    "ISFP": {"name": "호기심 많은 예술가", "fact": "누워 있는 게 제일 좋음. 갈등 생기는 거 극혐해서 그냥 내가 참음.", "best": "ESTJ", "worst": "ENTJ"},
    "ESTP": {"name": "모험을 즐기는 사업가", "fact": "관종. 환불 원정대 1선발. 내일 일은 내일 생각함.", "best": "ISFJ", "worst": "INFJ"},
    "ESFP": {"name": "자유로운 영혼의 연예인", "fact": "우주 최강 핵인싸. 정적 흐르는 거 못 참음. 텐션 항상 하이.", "best": "ISTJ", "worst": "INTJ"},
}

mbti_list = list(mbti_data.keys())

# --- UI 시작 ---
st.title("🔮 MBTI 과몰입 팩폭 & 궁합 테스트")
st.markdown("당신의 MBTI를 선택하고 **뼈 때리는 팩폭**과 **환상의 짝꿍**을 찾아보세요! 🚀")

st.divider()

# 사이드바에서 내 MBTI 선택
with st.sidebar:
    st.header("🧠 내 MBTI 선택")
    my_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", mbti_list)
    st.success(f"현재 선택된 MBTI: **{my_mbti}**")

# 메인 화면 탭 구성
tab1, tab2 = st.tabs(["🔥 뼈때리는 팩폭", "💖 환상의 궁합 & 최악의 상극"])

# --- TAB 1: 팩폭 ---
with tab1:
    st.subheader(f"[{my_mbti}] {mbti_data[my_mbti]['name']}")
    
    # 재미를 위한 로딩 효과
    with st.spinner('당신의 영혼을 탈곡하는 중... 🌾'):
        time.sleep(1)
        
    st.info(f"**팩폭 날아갑니다 💣**\n\n{mbti_data[my_mbti]['fact']}")

# --- TAB 2: 궁합 ---
with tab2:
    st.subheader("나와 찰떡인 MBTI는 누굴까?")
    
    col1, col2 = st.columns(2)
    
    best_match = mbti_data[my_mbti]['best']
    worst_match = mbti_data[my_mbti]['worst']
    
    with col1:
        st.markdown(f"### 👼 천생연분: {best_match}")
        st.write(f"[{best_match}] {mbti_data[best_match]['name']}")
        if st.button("천생연분 궁합 보기"):
            st.balloons()
            st.success(f"{my_mbti}와(과) {best_match}은(는) 서로의 단점을 완벽히 보완해주는 최고의 파트너입니다! 🎉")
            
    with col2:
        st.markdown(f"### 😈 파국: {worst_match}")
        st.write(f"[{worst_match}] {mbti_data[worst_match]['name']}")
        if st.button("파국 궁합 보기"):
            st.error(f"{my_mbti}와(과) {worst_match}은(는)... 말을 아끼겠습니다. 서로 많은 노력이 필요해요! 😱")

st.divider()
st.caption("※ 본 앱은 재미를 위한 과몰입용입니다. 현실의 인간관계는 MBTI보다 대화가 중요합니다. 😉")

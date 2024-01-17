import streamlit as st
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'done!!!!'



left_column, right_column = st.columns(2)
button = left_column.button('右からむに文字を表示')

if button:
    right_column.write('ここは右カラムです。')

expander = st.expander('についての問い合わせ回答')
expander.write('ｄふぁｌ；ｄｊｓｌ；ｊｌ；ｆｊｓｌｆｊ'
               'ｊｌｓｆｄじゃ；ｓｆｊｋｓｌｆｄｖｆｓｊｄｓｌｆｓｆｓｊｌｆｊｋ'
               'ｊｆｄｌさｆｓぁ；ｄｋｊｓｊｆｓ；ｆ'
               'ｄｊｆｋぁ；ｆｊｓｌｆｊ')

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味:', text,
#
# condition = st.slider('あなたの今の調子は？',0, 100 , 50)
# 'コンディション：',condition



# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

#'あなたの好きな数字は', option, 'です。'
# check_box = st.checkbox('Show Image', True)
# if check_box:
#     img = Image.open('kikunoya.jpg')
#     st.image(img, caption='菊乃家外観', use_column_width=True)





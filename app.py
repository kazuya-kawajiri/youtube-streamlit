import streamlit as st

st.title('菊乃家アプリ')

st.caption('練習中')

btn = st.button('送信')

if btn:
    print(f'ボタンが押されたよ（ターミナル）：{btn}')
    st.write(f'ボタンが押されたよ（ディスプレイ）{btn}')
else:
    st.write(f'no（ディスプレイ）{btn}')
    print(btn)
# softmax function
import streamlit as st
import numpy as np

# ソフトマックス関数の実装
def softmax_function(a):
    exp_a = np.exp(a) # 分子
    sum_exp_a = np.sum(exp_a) # 分母
    y = exp_a / sum_exp_a 
    return y

st.title('softmax関数の体験')

st.write()

softmax = r'$${y_i} = \frac{e^{x_{i}}}{e^{x_1} + e^{x_2} + \dots + e^{x_n}} \ \ \ for\ i=1,2,\dots,n$$'

st.markdown(softmax)

st.write()

st.write('値を入力して実行をクリックしてください')

# ３つのカラムを作成
col1, col2, col3 = st.columns(3)
with col1:
    input1 = st.text_input('input1', '0.0')
    st.session_state.input1 = float(input1)
with col2:
    input2 = st.text_input('input2', '0.0')
    st.session_state.input2 = float(input2)
with col3:
    input3 = st.text_input('input3', '0.0')
    st.session_state.input3 = float(input3)

if st.button("実行"):
    
    a = np.array([st.session_state.input1, st.session_state.input2, st.session_state.input3])
    y = softmax_function(a)

    # 入力内容を取得
    col1_output, col2_output, col3_output = st.columns(3)
    with col1_output:
        st.write('{:0.3f}'.format(y[0]))
    with col2_output:
        st.write('{:0.3f}'.format(y[1]))
    with col3_output:
        st.write('{:0.3f}'.format(y[2]))

import streamlit as st 


def main():
    st.write('hello')
    with st.expand('expand'):
        st.write('ini expand')

if __name__ == '__main__':
    main()
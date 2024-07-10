import streamlit as st
from ollama import chat


def generate_code(input_text):
    response = chat(
        model='gemma:2b',
        messages=[
            {
                'role': 'user',
                'content': f'{input_text}',
            },
        ],
    )
    return response['message']['content']


def main():
    if 'chat' not in st.session_state:
        st.session_state['chat'] = []

    prompt = st.chat_input('Ask something')

    if prompt:
        st.session_state.chat.append('user: ' + prompt)
        output = generate_code(prompt)

        if output:
            st.session_state.chat.append('model: ' + output)

    if st.session_state.chat:
        for text in st.session_state.chat:
            if text.startswith('user:'):
                text = text.replace('user:', '')
                max_width = min(len(text) * 10, 600)
                st.markdown(
                    f"""
                    <div style='max-width: {max_width}px; margin-left: auto; margin-bottom: 10px; margin-right: 10px; background-color: #DCF8C6; border-radius: 10px; padding: 10px; text-align: right;'>
                        <p style='font-size: 14px; color: #333333;'>{text}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif text.startswith('model:'):
                text = text.replace('model:', '')
                max_width = min(len(text) * 10, 600)
                st.markdown(
                    f"""
                    <div style='max-width: {max_width}px; margin-right: auto; margin-bottom: 10px; margin-left: 10px; background-color: #F0F0F0; border-radius: 10px; padding: 10px; text-align: left;'>
                        <p style='font-size: 14px; color: #000000;'>{text}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


if __name__ == '__main__':
    main()

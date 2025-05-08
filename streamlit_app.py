import streamlit as st
from gemini_wrapper import GeminiWrapper
from prompts import *

def orchestration_page():
    st.title("Kai Orchestration Simulation")
    st.write("This is the Simulation page for Kai Engine / Agent orchestration")
    # Add your orchestration logic here
    wrapper = GeminiWrapper(temp=1)
    if "model" not in st.session_state:
        st.session_state["model"] = "gemini-flash"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                message_placeholder = st.empty()
                with st.status("Thinking...",state="running",expanded=True) as status:
                    for html_chunk in wrapper.get_results_markdown(SYS_ORCHESTRATION_PROMPT,prompt):
                        full_response = html_chunk
                        message_placeholder.markdown(full_response, unsafe_allow_html=True)
                    status.update(label="Complete", state="complete", expanded=False)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                # Export Button and PDF Conversion
                if full_response:
                    if st.download_button(
                        label="Export Markdown",
                        data=full_response.encode("utf-8"),
                        file_name=f"thinking_model_response.md",
                        mime="text/markdown",
                    ):
                        st.success("Markdown exported!")
            except Exception as e:
                st.markdown(f"Error in processing response :{e}")


def thinking_agent_page():
    st.title("Thinking Agent")
    # Add your Thinking Agent logic here
    wrapper = GeminiWrapper(temp=1)
    if "model" not in st.session_state:
        st.session_state["model"] = "gemini-flash"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                message_placeholder = st.empty()
                with st.status("Thinking...",state="running",expanded=True) as status:
                    for html_chunk in wrapper.get_thinking_model_data(SYS_THINKING_PROMPT,prompt):
                        full_response = html_chunk
                        message_placeholder.markdown(full_response, unsafe_allow_html=True)
                    status.update(label="Complete", state="complete", expanded=False)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                # Export Button and PDF Conversion
                if full_response:
                    if st.download_button(
                        label="Export Markdown",
                        data=full_response.encode("utf-8"),
                        file_name=f"thinking_model_response.md",
                        mime="text/markdown",
                    ):
                        st.success("Markdown exported!")
            except Exception as e:
                st.markdown(f"Error in processing response :{e}")


def process_thinking_agent(input_text):
    #Replace with your actual agent logic.
    return f"Processed: {input_text}"

def duet_search_page():
    st.title("DuetSearch")
    st.write("This is the DuetSearch page.")
    # Add your DuetSearch logic here
   

def impac_call():
    st.title("IMPAC Agent")
    st.html('<widget-app token="k-ig0wJiomp1DIHSwwX1OJ8Ch5f3VWQldzVKQEVYBGU" id="494"></widget-app><script src="https://widget-agent-prod.s3.ap-south-1.amazonaws.com/widget.js"></script>')

def process_prompt(prompt_text):
    #Replace with your actual prompt processing logic.
    return f"Processed prompt: {prompt_text}"

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Orchestration", "Thinking Agent", "DuetSearch", "IMPAC Agent"))

    if page == "Orchestration":
        orchestration_page()
    elif page == "Thinking Agent":
        thinking_agent_page()
    elif page == "DuetSearch":
        duet_search_page()
    elif page == "IMPAC Agent":
        impac_call()

if __name__ == "__main__":
    main()

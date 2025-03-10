import streamlit as st
from JobBot import JobBot

print("Hello, World!")
jb = JobBot.JobBot()

with st.sidebar:
    if st.button("Find Job"):
        jb.find_job_button()
        thread = {
            "configurable": {
                "thread_id": "1",
                "checkpoint_ns": "jobbot",
                "checkpoint_id": "session_1"
            }
        }
        print(jb.graph.get_state(thread))

# Initialize message history
if "messages" not in st.session_state:
   st.session_state.messages = [
       {
           "role": "assistant",
           "content": "Hello! Ask me what kind of job you are looking for.",
       }
   ]

# Display chat history
for message in st.session_state.messages:
   with st.chat_message(message["role"]):
       st.markdown(message["content"])

if prompt := st.chat_input("Your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        print(prompt)

    with st.spinner("Thinking..."):
        response = jb.invoke(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

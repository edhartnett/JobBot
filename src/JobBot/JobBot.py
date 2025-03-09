import streamlit as st
from langchain.chat_models import init_chat_model
from langgraph.graph import START, END, StateGraph
from JobBot.JobState import JobState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from JobBot.JobModel import JobModel
from langgraph.checkpoint.memory import MemorySaver


@st.cache_resource
def init_model():
    print("Model initialized")
    model = init_chat_model("anthropic:claude-3-5-haiku-latest", temperature=0)
    return model

class JobBot:
    def __init__(self):
        self.model_initialized = False

    # def invoke(self, prompt: str):
    #     if not self.model_initialized:
    #         self.init_job_bot()
    #     self.model.invoke(prompt)

    def init_job_bot(self):
        self.build_find_graph()
        self.model = init_model()
        self.model_initialized = True

    def human_feedback(self, state: JobState):
        """ No-op node that should be interrupted on """
        pass

    def find_job_button(self):
        print("Find job pushed")
        if not self.model_initialized:
            self.init_job_bot()
        thread = {
            "configurable": {
                "thread_id": "1",
                "checkpoint_ns": "jobbot",
                "checkpoint_id": "session_1"
            }
        }

        initial_state = {"messages": [], "job_feedback": None}
        for event in self.graph.stream(initial_state, thread):
            print("Event:", event)


    def find_job(self, state: JobState):
        """ Node to find a job """
        if not self.model_initialized:
            self.init_job_bot()
            
        with open('src/job_ad_1.txt', 'r') as file:
            content = file.read()
            #print(content)

        print(state)
        job_feedback = state.get("job_feedback")

        parse_instructions = """You are an analyst tasked with learning about a specific job opening. 
        Find the hiring company, job title, required skills, and location. {job_feedback}
        """
        structured_llm = self.model.with_structured_output(JobModel)
        system_message = parse_instructions.format(job_feedback=job_feedback)
        print("invoking...")
        #result = structured_llm.invoke([SystemMessage(content=system_message)]+[content])
        #print(result)

        # Write messages to state
        return {"messages": structured_llm.invoke([SystemMessage(content=system_message)]+[content]), "job_feedback": job_feedback}
     
       
    def query_graph(self, query):
        if not self.model_initialized:
            self.model = init_model()
            self.model_initialized = True
        return self.model.invoke(query).content

    def build_find_graph(self):
        # Add nodes and edges 
        jobbot_graph = StateGraph(JobState)
        jobbot_graph.add_node("find_job", self.find_job)
        jobbot_graph.add_node("human_feedback", self.human_feedback)

        # Flow
        jobbot_graph.add_edge(START, "find_job")
        jobbot_graph.add_edge("find_job", "human_feedback")
        jobbot_graph.add_conditional_edges("human_feedback", self.find_job, ["find_job", END])

        memory = MemorySaver()
        self.graph = jobbot_graph.compile(interrupt_before=['human_feedback'], checkpointer=memory)

        # topic = "Find a job"
        # thread = {"configurable", {"thread_id": "1"}}
        # for event in self.graph.stream({"topic":topic}, thread, self.stream_mode=="values"):
        #     print("review")

        # further_feedback = input("Feedback?")
        # if (further_feedback =="no"):
        #     further_feedback = None

        # graph.update_state(thread, {"job_feedback": further_feedback}, as_node="human_feedback")

        # for event in graph.stream(None, thread, stream_mode="updates"):
        #     print(next(iter(event.keys())))

        # final_state = graph.get_state(thread)
        # #report = final_state.values.get('final_report')
        #print(report)
        return True
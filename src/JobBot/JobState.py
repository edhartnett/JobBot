from langgraph.graph import MessagesState

class JobState(MessagesState):
    source: str
    description: str
    cover_letter: str
    resume: str
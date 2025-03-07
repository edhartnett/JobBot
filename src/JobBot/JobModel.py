from pydantic import BaseModel, Field
from typing import List

class JobModel(BaseModel):
    title: str = Field(None, description="Job title")
    brief_description: str = Field(None, description="Brief description of job")
    salary_range: str = Field(None, description="Salary range")
    remote: str = Field(None, description="Remote work is an option")
    hybrid: str = Field(None, description="Hybrid work is an option")
    location: str = Field(None, description="Location of job")
    required_skills: List[str] = Field(None, description="Required skills")
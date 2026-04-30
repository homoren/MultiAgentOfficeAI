from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from agents.email_agent import format_emails
from agents.calendar_agent import format_calendar
from agents.task_agent import format_tasks
from config import OPENAI_API_KEY
import os

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

def generate_daily_plan():
    llm = OpenAI(temperature=0)
    prompt = PromptTemplate(
        input_variables=['emails_info', 'calendar_info', 'tasks_info'],
        template="""
你是智能办公助理。根据以下信息生成今天的行动计划，按照优先级排序，并提醒重要任务：
Emails:
{emails_info}

Calendar:
{calendar_info}

Tasks:
{tasks_info}

请生成每日行动计划：
"""
    )
    input_text = prompt.format(
        emails_info=format_emails(),
        calendar_info=format_calendar(),
        tasks_info=format_tasks()
    )
    plan = llm(input_text)
    return plan

from agents.plan_agent import generate_daily_plan

if __name__ == '__main__':
    print('=== 今日智能办公助理行动计划 ===')
    plan = generate_daily_plan()
    print(plan)

from llms import *
from tools.tools import *
from tools.tools_desc import *

def responses(llm: LLM, tools=None) -> list:
    import json
    questions = [
        "今天是几月几日，现在是几点几分？", # 外部世界交互
        "9264857101的因子有哪些？", # 大数计算
        "查询本地的root用户（密码是123456）的所有数据库。", # 私有知识库查询
        "2024年10月21号至2024年10月25号之间，微软公司的最高股票价格是多少？" # 金融数据查询
    ]
    all_response = []
    if tools is None:
        for q in questions:
            all_response.append(llm(prompt=q))
    else:
        for q in questions:
            response = llm(prompt=q, tools=tools)
            print(response)
            tool_call = response.choices[0].message.tool_calls[0]
            # print(tool_call)

            function_call_result_message = get_function_result(tool_call)

            tmp = llm(prompt=[
                {"role": "user", "content": q},
                response.choices[0].message,
                function_call_result_message
            ])
            all_response.append(tmp)
    return all_response


def test_all_llm_api():
    llm = GPT('gpt-4o-mini')
    print(f"gpt-4o-mini: {responses(llm=llm)}")

    llm = CLAUDE('claude-3-5-sonnet-20240620')
    print(f"claude-3-5-sonnet: {responses(llm=llm)}")

    llm = GEMINI('gemini-1.5-flash-002')
    print(f"gemini-1.5-flash: {responses(llm=llm)}")

    llm = DeepSeek('deepseek-chat')
    print(f"deepseek-chat: {responses(llm=llm)}")

    llm = Qwen('Qwen2.5-72B-Instruct')
    print(f"qwen2.5-72b-instruct: {responses(llm=llm)}")


def test_gpt_api():
    llm = GPT('gpt-4o-mini')
    print(f"{'*'*20} gpt-4o-mini without Tools {'*'*20}")
    print(f": {responses(llm=llm)}")


def test_gpt_api_tools():
    llm = GPT('gpt-4o-mini', temperature=0.7)
    print(f"{'*'*20} gpt-4o-mini with Tools {'*'*20}")
    print(f": {responses(llm=llm, tools=all_tools)}")

'''
response.choices[0].message
[
    ChatCompletionMessage(
        content=None, 
        refusal=None, 
        role='assistant', 
        audio=None, 
        function_call=None, 
        tool_calls=[
            ChatCompletionMessageToolCall(
                id='call_NDWcBLzseRbW7VpHycTWDuRP', 
                function=Function(arguments='{}', name='get_current_datetime'), 
                type='function'
            )
        ]
    )
]
'''

if __name__ == "__main__":
    # test_all_llm_api()
    test_gpt_api()
    test_gpt_api_tools()

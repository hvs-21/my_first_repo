import dashscope
from dashscope import Generation
dashscope.api_key =""
while True:
    user_input=input("\n🦹 那我问你：")
    if user_input == "退下吧" or user_input =="exit":
        break

    if not user_input.strip():
        continue
    dynamic_prompt = f"""
    你是一个严谨的《三国演义》智能问答军师。
    请用文言文风格，回答主公的这个问题：{user_input}
    """

    messages =[{'role': 'user','content': dynamic_prompt}]

    response = Generation.call(
        model='qwen-turbo',
        messages=messages,
        result_format='message'
    )

    if response.status_code ==200:
        answer = response.output.choices[0]['message']['content']
        print(f"\n摸金校尉/军事：{answer}")
    
class LLM:
    def __init__(self) -> None:
        pass

    def __call__(self, prompt) -> str:
        if isinstance(prompt, str):
            self.prompt = [{"role": "user", "content": prompt}]
        else:
            self.prompt = prompt


class CLAUDE(LLM):
    def __init__(self, engine, temperature=0, max_tokens=1024) -> None:
        import os
        import anthropic

        self.client = anthropic.Anthropic(
            base_url=os.getenv("OPENAI_BASE_URL").replace('v1','anthropic'),
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens

    def __call__(self, prompt) -> str:
        super().__call__(prompt)
        response = self.client.messages.create(
            model=self.engine,
            messages=self.prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response.content[0].text


class GEMINI(LLM):
    def __init__(self, engine, temperature=0, max_tokens=1024) -> None:
        import os
        import google.generativeai as genai

        self.client = genai.GenerativeModel(engine)
        genai.configure(
            api_key=os.getenv("OPENAI_API_KEY"),
            transport="rest",
            client_options={
                "api_endpoint": os.getenv("OPENAI_BASE_URL").replace('v1','google')
            },
        )
        self.generation_config = genai.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
        )

    def __call__(self, prompt) -> str:
        # super().__call__(prompt)
        response = self.client.generate_content(
            contents=prompt, generation_config=self.generation_config
        )
        return response.text


class GPT(LLM):
    def __init__(self, engine, temperature=0, max_tokens=1024) -> None:
        import os
        from openai import OpenAI
        self.client = OpenAI(
            base_url=os.getenv("OPENAI_BASE_URL"),
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens

    def __call__(self, prompt, tools=None) -> str:
        super().__call__(prompt)
        if tools is None:
            if "gpt" in self.engine.lower():
                response = self.client.chat.completions.create(
                    model=self.engine,
                    messages=self.prompt,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
                return response.choices[0].message.content
            elif "o1" in self.engine.lower():
                response = self.client.chat.completions.create(
                    model=self.engine,
                    messages=self.prompt,
                    temperature=1,
                    max_completion_tokens=65536,
                )
                return response.choices[0].message.content
            else:
                raise ValueError(f"Invalid engine name: {self.engine}")
        else:
            if "gpt" in self.engine.lower():
                response = self.client.chat.completions.create(
                    model=self.engine,
                    messages=self.prompt,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    tools=tools
                )
                return response
            else:
                raise ValueError(f"Invalid engine name: {self.engine}")


class Qwen(LLM):
    def __init__(self, engine, temperature=0, max_tokens=1024) -> None:
        from openai import OpenAI
        import os

        if engine == "Qwen1.5-72B-Chat":
            self.client = OpenAI(base_url=os.getenv("QWEN_BASE"), api_key="XXX")
        elif engine == "Qwen2-72B-Instruct":
            self.client = OpenAI(
                base_url=os.getenv("QWEN2_BASE"), api_key=os.getenv("QWEN2_KEY")
            )
        elif engine == "Qwen2.5-72B-Instruct":
            self.client = OpenAI(
                base_url=os.getenv("QWEN2_BASE"), api_key=os.getenv("QWEN2_KEY")
            )
        else:
            raise ValueError("Error: wrong engine name")
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens

    def __call__(self, prompt) -> str:
        super().__call__(prompt)
        response = self.client.chat.completions.create(
            model=self.engine,
            messages=self.prompt,
            temperature=self.temperature,
        )
        return response.choices[0].message.content


class DeepSeek(LLM):
    def __init__(self, engine, temperature=0, max_tokens=1024) -> None:
        from openai import OpenAI
        import os

        self.client = OpenAI(
            base_url=os.getenv("DEEPSEEK_API_BASE"), 
            api_key=os.getenv("DEEPSEEK_API_KEY")
        )

        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens

    def __call__(self, prompt) -> str:
        super().__call__(prompt)
        response = self.client.chat.completions.create(
            model=self.engine,
            messages=self.prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=False,
        )
        return response.choices[0].message.content

from PyKakao import KoGPT
api = KoGPT(service_key = "ccc280dbcb6fa3d2bbbf62aa3e763705")

class KakaoChatbot:
    def __init__(self):
        pass

    def exec_1(self):
        # 필수 파라미터
        prompt = "인간처럼 생각하고, 행동하는 '지능'을 통해 인류가 이제까지 풀지 못했던"
        max_tokens = 64

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.7, top_p=0.8)
        print(result)

    def exec_2(self):
        # 필수 파라미터
        prompt = """상품 후기를 긍정 또는 부정으로 분류합니다.
        가격대비좀 부족한게많은듯=부정
        재구매 친구들이 좋은 향 난다고 해요=긍정
        ㅠㅠ약간 후회가 됩니다..=부정
        이전에 먹고 만족해서 재구매합니다=긍정
        튼튼하고 잘 쓸수 있을 것 같습니다. 이 가격에 이 퀄리티면 훌륭하죠="""
        max_tokens = 1

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.4)
        # 결과가 “긍정” 또는 “부정”이어야 하므로 max_tokens은 1로 지정해 요청합니다.
        print(result)

    def exec_3(self):
        # 필수 파라미터
        prompt = """상품 후기를 긍정 또는 부정으로 분류합니다.
        가격대비좀 부족한게많은듯=부정
        재구매 친구들이 좋은 향 난다고 해요=긍정
        ㅠㅠ약간 후회가 됩니다..=부정
        이전에 먹고 만족해서 재구매합니다=긍정
        튼튼하고 잘 쓸수 있을 것 같습니다. 이 가격에 이 퀄리티면 훌륭하죠="""
        max_tokens = 1

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.4)
        print(result)


if __name__ == '__main__':
    KakaoChatbot().exec_3()


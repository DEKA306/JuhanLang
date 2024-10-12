# Leejuhan.py
class SimpleLang:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        code = code.replace("응디", "print")
        code = code.replace("운지", "if")
        code = code.replace("지운", "else")
        code = code.replace("뭐했노", "input")
        code = code.replace("야", "while")
        code = code.replace("딱", "for")
        code = code.replace("국정원", "range")
        code = code.replace("참모총장", "and")
        code = code.replace("국방부장관", "or")
        code = code.replace("바위", "not")
        code = code.replace("좋다", ":")
        code = code.replace("노무현은살아있다", "True")
        code = code.replace("노무현은죽었다", "False")
        code = code.replace("피아제", "#")
        code = code.replace("대한민국군대들", "def")
        code = code.replace("이기", "in")
        code = code.replace("라면", "int")
        code = code.replace("방독면", "str")

        exec(code, self.variables)

def 떨어졌다(a):
    user_code = a

    interpreter = SimpleLang()

    interpreter.execute(user_code)

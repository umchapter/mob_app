"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        # Pack은 CSS처럼 활용됨. COLUMN은 모든 width 사용하고, 컨텐츠에 따라
        # 높이 확장됨, 하지만 가능한 한 짧은 길이가 되도록 행동.
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # 5px 패딩 좌우로 설정됨. 위 아래는 없음. TextInput의 경우는
        # 유연하게 설정됨 : 레이아웃 축에서 가용한 공간 모두 사용함. 
        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        # name_box는 main_box와 같음, 하지만 행(ROW) 박스임.
        # 행으로 추가됨. 너비를 가능한 한 좁게 되도록 행동.
        # 모든 방향으로 padding 5px 주었음.
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        # 모든 방향으로 5px 패딩, handler 정의 - 버튼이 눌리면 작동하는 메소드
        button = toga.Button(
            "Say Hello!",
            on_press = self.say_hello, # say_hello 메소드 아래서 정의
            style = Pack(padding=5)
        )

        # name_box와 button을 main_box에 추가함
        main_box.add(name_box)
        main_box.add(button)

        # 레이아웃 설정 끝남. startup 메소드의 나머지는 그 이전과 같음.
        # 메인윈도우를 정의하고, main_box를 윈도우의 컨텐츠로 설정함.
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # handler 메소드를 정의함. # 업데이트
    def say_hello(self, widget) :
        self.main_window.info_dialog(
            f"Hello, {self.name_input.value}",
            "Hi there!"
        )

# helloworld 폴더에서 cmd : briefcase dev
def main():
    return HelloWorld()

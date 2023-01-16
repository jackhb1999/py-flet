# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from time import sleep

import flet as ft

# 第一个例子
# def main(page: ft.Page):
#     t = ft.Text(value="hello,word!",color="green")
#     page.controls.append(t)
#     page.update()

# 第二个例子
# def main(page: ft.Page):
#     t = ft.Text()
#     page.add(t)
#
#     for i in range(10):
#         t.value = f"Step {i}"
#         page.update()
#         sleep(1)

# 第三个例子
# def main(page: ft.Page):
#     page.add(
#         ft.Row(controls=[
#             ft.Text("A"),
#             ft.Text("B"),
#             ft.Text("C")
#         ])
#     )

# 第四个例子
# def main(page: ft.Page):
#     page.add(
#         ft.Row(controls=[
#             ft.TextField(label="Your name"),
#             ft.ElevatedButton(text="Say my name!")
#         ])
#     )

# 第五个例子
# def main(page: ft.Page):
#     for i in range(10):
#         page.controls.append(ft.Text(f"Line {i}"))
#         if i > 4:
#             page.controls.pop(0)
#         page.update()
#         sleep(0.3)

# 第六个例子
# def main(page: ft.Page):
#     def button_clicked(e):
#         page.add(ft.Text("Clicked!"))
#     page.add(ft.ElevatedButton(text="Click me",on_click=button_clicked))

# 第七个例子
# def main(page: ft.Page):
#     def add_clicked(e):
#         page.add(ft.Checkbox(label=new_task.value))
#
#     new_task = ft.TextField(hint_text="Whats needs to be done?",width=300)
#     page.add(ft.Row([new_task,ft.ElevatedButton("Add",on_click=add_clicked)]))

# 第八个例子
# def main(page: ft.Page):
#     first_name = ft.TextField()
#     last_name = ft.TextField()
#     first_name.disabled = True
#     last_name.disabled = False
#     page.add(first_name,last_name)

# 第九个例子
# def main(page: ft.Page):
#     first_name = ft.TextField()
#     last_name = ft.TextField()
#     c = ft.Column(controls=[
#         first_name,
#         last_name
#     ])
#     c.disabled = True
#     last_name.visible = False
#     page.add(c)

# 第十个例子
# def main(page: ft.Page):
#     first_name = ft.TextField(label="First name",autofocus=True)
#     last_name = ft.TextField(label="Last name")
#     greetings = ft.Column()
#
#     def btn_click(e):
#         greetings.controls.append(ft.Text(f"Hello,{first_name.value} {last_name.value}!"))
#         first_name.value = ""
#         last_name.value = ""
#         page.update()
#         first_name.focus()
#
#     page.add(
#         first_name,
#         last_name,
#         ft.ElevatedButton("Say hello!",on_click=btn_click),
#         greetings,
#     )

# 第十一个例子
# def main(page: ft.Page):
#     first_name = ft.Ref[ft.TextField]()
#     last_name = ft.Ref[ft.TextField]()
#     greetings = ft.Ref[ft.TextField]()
#
#     def btn_click(e):
#         greetings.current.controls.append(ft.Text(f"Hello,{first_name.current.value} {last_name.current.value}!"))
#         first_name.current.value = ""
#         last_name.current.value = ""
#         page.update()
#         first_name.current.focus()
#
#     page.add(
#         ft.TextField(ref=first_name,label="First name",autofocus=True),
#         ft.TextField(ref=last_name,label="Lst name"),
#         ft.ElevatedButton("Say hello!",on_click=btn_click),
#         ft.Column(ref=greetings)
#     )

# 按钮
# def main(page: ft.Page):
#     btn = ft.ElevatedButton("Click me !")
#     page.add(btn)

# 事件处理程序
# def main(page: ft.Page):
#     page.title = "Flet counter example —— 数字增减"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#
#     txt_number = ft.TextField(value="0",text_align="right",width=100)
#
#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()
#
#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()
#
#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.icons.REMOVE,on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.icons.ADD,on_click=plus_click)
#             ],
#             alignment=ft.MainAxisAlignment.CENTER
#         )
#     )

# 文本框
# def main(page: ft.Page):
#     def btn_click(e):
#         if not txt_name.value:
#             txt_name.error_text = "Please enter your name"
#             page.update()
#         else:
#             name = txt_name.value
#             page.clean()
#             page.add(ft.Text(f"Hello,{name}!"))
#
#     txt_name = ft.TextField(label="Your name")
#
#     page.add(txt_name,ft.ElevatedButton("Say hello!",on_click=btn_click))

# 复选框
# def main(page: ft.Page):
#     def checkbox_changed(e):
#         output_text.value = (
#             f"You have learned how to ski : {todo_check.value}."
#         )
#         page.update()
#
#     output_text = ft.Text()
#     todo_check = ft.Checkbox(label="Todo: Leaen how to use ski",value=False,on_change=checkbox_changed)
#     page.add(todo_check,output_text)

# 下拉列表
# def main(page: ft.Page):
#     def button_clicked(e):
#         output_text.value = f"Dropdown value is : {color_dropdown.value}"
#         page.update()
#
#     output_text = ft.Text()
#     submit_btn = ft.ElevatedButton(text="submit",on_click=button_clicked)
#     color_dropdown = ft.Dropdown(
#         width=100,
#         options=[
#             ft.dropdown.Option("Red"),
#             ft.dropdown.Option("Green"),
#             ft.dropdown.Option("Blue")
#         ]
#     )
#     page.add(color_dropdown,submit_btn,output_text)

# 键盘快捷键
# def main(page: ft.Page):
#     def on_keyboard(e: ft.KeyboardEvent):
#         page.add(
#             ft.Text(
#                 "123123"
#             ),
#             ft.Text(
#                 f"Key:{e.key},Shift:{e.shift},Control:{e.ctrl},Alt:{e.alt},Meta: {e.meta}"
#             )
#         )
#         page.update()
#
#     page.on_keyboard_event = on_keyboard
#     page.add(
#         ft.Text("Press any key with a combination of CTRL,ALT,SHIFT and META keys...")
#     )
#
#


# 加强键盘输入
# from flet import Container, Page, Row, Text, border, colors, KeyboardEvent
# class ButtonControl(Container):
#     def __init__(self, text):
#         super().__init__()
#         self.content = Text(text)
#         self.border = border.all(1, colors.BLACK54)
#         self.border_radius = 3
#         self.bgcolor = "0x09000000"
#         self.padding = 10
#         self.visible = False
#
# def main(page: Page):
#     def on_keyboard(e: KeyboardEvent):
#         key.content.value = e.key
#         key.visible = True
#         shift.visible = e.shift
#         ctrl.visible = e.ctrl
#         alt.visible = e.alt
#         meta.visible = e.meta
#         page.update()
#
#     page.on_keyboard_event = on_keyboard
#
#     key = ButtonControl("")
#     shift = ButtonControl("Shift")
#     ctrl = ButtonControl("Control")
#     alt = ButtonControl("Alt")
#     meta = ButtonControl("Meta")
#
#     page.spacing = 50
#     page.vertical_alignment = "center"
#     page.horizontal_alignment = "center"
#     page.add(
#         Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys..."),
#         Row([key, shift, ctrl, alt, meta], alignment="center"),
#     )

# 大型列表
# def main(page:ft.Page):
#     for i in range(5000):
#         page.controls.append(ft.Text(f"Line {i}"))
#     page.scroll = "always"
#     page.update()

import os

# WebSocket 消息的最大大小（以字节为单位）
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
# 网格视图
# def main(page:ft.Page):
#     r = ft.Row(wrap=True,scroll="always",expand=True)
#     page.add(r)
#
#     for i in range(5000):
#         r.controls.append(
#             ft.Container(
#                 ft.Text(f"Item {i}"),
#                 width=100,
#                 height=100,
#                 alignment=ft.alignment.center,
#                 bgcolor=ft.colors.AMBER_100,
#                 border=ft.border.all(1,ft.colors.AMBER_400),
#                 border_radius=ft.border_radius.all(5),
#             )
#         )
#     page.update()

# 网格视图
# def main(page:ft.Page):
#     gv = ft.GridView(expand=True,max_extent=150,child_aspect_ratio=1)
#     page.add(gv)
#
#     for i in range(5000):
#         gv.controls.append(
#             ft.Container(
#                 ft.Text(f"Item{i}"),
#                 alignment=ft.alignment.center,
#                 bgcolor=ft.colors.AMBER_100,
#                 border=ft.border.all(1,ft.colors.AMBER_400),
#                 border_radius=ft.border_radius.all(5)
#             )
#         )
#     page.update()

# 批量更新
# def main(page:ft.Page):
#     lv = ft.ListView(expand=1,spacing=10,item_extent=50)
#     page.add(lv)
#
#     for i in range(5100):
#         lv.controls.append(ft.Text(f"Line{i}"))
#         if i % 500 == 0:
#             page.update()
#     page.update()

# 拖放
# def main(page:ft.Page):
#     page.title = "Drag and Drop example"
#
#     def drag_accept(e):
#         src = page.get_control(e.src_id)
#         src.content.content.value = "0"
#         src.group = ""
#         e.control.content.content.value = "1"
#         e.control.content.border = None
#         page.update()
#
#     def drag_will_accept(e):
#         e.control.content.border = ft.border.all(
#             2,ft.colors.BLACK45 if e.data == "true" else ft.colors.RED
#         )
#         e.control.update()
#
#     def drag_leave(e):
#         e.control.content.border = None
#         e.control.update()
#
#     page.add(
#         ft.Row(
#             [
#                 ft.Draggable(
#                     group="number",
#                     content=ft.Container(
#                         width=50,
#                         height=50,
#                         bgcolor=ft.colors.CYAN_200,
#                         border_radius=5,
#                         content=ft.Text("1",size=20),
#                         alignment=ft.alignment.center,
#                     ),
#                     content_when_dragging=ft.Container(
#                         width=50,
#                         height=50,
#                         bgcolor=ft.colors.BLUE_GREY_200,
#                         border_radius=5,
#                     ),
#                     content_feedback=ft.Text("1")
#                 ),
#                 ft.Container(width=100),
#                 ft.DragTarget(
#                     group="number",
#                     content=ft.Container(
#                         width=50,
#                         height=50,
#                         bgcolor=ft.colors.PINK_200,
#                         border_radius=5,
#                         content=ft.Text("0",size=20),
#                         alignment=ft.alignment.center,
#                     ),
#                     on_accept=drag_accept,
#                     on_will_accept=drag_will_accept,
#                     on_leave=drag_leave,
#                 )
#             ]
#         )
#     )

# 获取路由
# def main(page:ft.Page):
#     page.add(ft.Text(f"Initial route:{page.route}"))
#
#     def route_change(route):
#         page.add(ft.Text(f"New route:{route}"))
#
#     page.on_route_change = route_change
#     page.update()

# 通过更新属性更改路由
# def main(page:ft.Page):
#     page.add(ft.Text(f"Initial route:{page.route}"))
#
#     def route_change(route):
#         page.add(ft.Text(f"New route:{route}"))
#
#     def go_store(e):
#         page.route = "/store"
#         page.update()
#
#     page.on_route_change = route_change
#     page.add(ft.ElevatedButton("Go to Store",on_click=go_store))

# 路由更改视图
# def main(page:ft.Page):
#     page.title = "Routes Example"
#
#     def route_change(route):
#         page.views.clear()
#         page.views.append(
#             ft.View(
#                 "/",
#                 [
#                     ft.AppBar(title=ft.Text("Flet app"),bgcolor=ft.colors.SURFACE_VARIANT),
#                     ft.ElevatedButton("Visit Store",on_click=lambda _:page.go("/store"))
#                 ]
#             )
#         )
#         if page.route == "/store":
#             page.views.append(
#                 ft.View(
#                     "/store",
#                     [
#                         ft.AppBar(title=ft.Text("Store"),bgcolor=ft.colors.SURFACE_VARIANT),
#                         ft.ElevatedButton("Go Home",on_click=lambda _: page.go("/"))
#                     ]
#                 )
#             )
#         page.update()
#
#     def view_pop(view):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)
#
#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
#     page.go(page.route)

# 不透明度动画
# def main(page:ft.Page):
#     c = ft.Container(
#         width=150,
#         height=150,
#         bgcolor="blue",
#         border_radius=10,
#         animate_opacity=300,
#     )
#
#     def animate_opacity(e):
#         c.opacity = 0 if c.opacity == 1 else 1
#         c.update()
#
#     page.add(
#         c,
#         ft.ElevatedButton(
#             "Animate opacity",
#             on_click=animate_opacity,
#         )
#     )

# 旋转动画
# from math import pi
# def main(page:ft.Page):
#     c = ft.Container(
#         width=100,
#         height=70,
#         bgcolor="blue",
#         border_radius=5,
#         rotate=ft.transform.Rotate(0,alignment=ft.alignment.center),
#         animate_rotation=ft.animation.Animation(300,ft.AnimationCurve.BOUNCE_OUT)
#     )
#
#     def animate(e):
#         c.rotate.angle += pi /2
#         page.update()
#
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.spacing = 30
#     page.add(
#         c,ft.ElevatedButton("Animate!",on_click=animate)
#     )

# 缩放动画
# def main(page:ft.Page):
#     c = ft.Container(
#         width=100,
#         height=100,
#         bgcolor="blue",
#         border_radius=5,
#         scale=ft.transform.Scale(scale=1),
#         animate_scale=ft.animation.Animation(600,ft.AnimationCurve.BOUNCE_OUT)
#     )
#
#     def animate(e):
#         c.scale = 2
#         page.update()
#
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.spacing = 30
#     page.add(
#         c,ft.ElevatedButton("Animate!",on_click=animate)
#     )

# 偏移动画
# def main(page:ft.Page):
#     c = ft.Container(
#         width=150,
#         height=150,
#         bgcolor="blue",
#         border_radius=10,
#         offset=ft.transform.Offset(-2,0),
#         animate_offset=ft.animation.Animation(1000)
#     )
#
#     def animate(e):
#         c.offset = ft.transform.Offset(0,0)
#         c.update()
#
#     page.add(c,ft.ElevatedButton("Reveal!",on_click=animate))

# 位置动画
# def main(page:ft.Page):
#     c1 = ft.Container(width=50,height=50,bgcolor="red",animate_position=1000)
#
#     c2 = ft.Container(width=50,height=50,bgcolor="green",top=60,left=0,animate_position=500)
#
#     c3 = ft.Container(width=50,height=50,bgcolor="blue",top=120,left=0,animate_position=1000)
#
#     def animate_container(e):
#         c1.top = 20
#         c1.left = 200
#         c2.top = 100
#         c2.left = 40
#         c3.top = 180
#         c3.left = 100
#         page.update()
#
#     page.add(
#         ft.Stack([c1,c2,c3],height=250),
#         ft.ElevatedButton("Animate!",on_click=animate_container)
#     )

# 动画容器
# def main(page:ft.Page):
#     c = ft.Container(
#         width=150,
#         height=150,
#         bgcolor="red",
#         animate=ft.animation.Animation(1000,ft.AnimationCurve.BOUNCE_OUT)
#     )
#
#     def animate_container(e):
#         c.width = 100 if c.width == 150 else 150
#         c.height = 50 if c.height == 150 else 150
#         c.bgcolor = "blue" if c.bgcolor == "red" else "red"
#         c.update()
#
#     page.add(c,ft.ElevatedButton("Animate container",on_click=animate_container))

# 动画容器
import time
# def main(page:ft.Page):
#     i = ft.Image(src="https://picsum.photos/150/150",width=150,height=150)
#
#     sw = ft.AnimatedSwitcher(
#         i,
#         transition=ft.AnimatedSwitcherTransition.SCALE,
#         duration=500,
#         switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
#         switch_out_curve=ft.AnimationCurve.BOUNCE_IN
#     )
#
#     def animate(e):
#         sw.content = ft.Image(
#             src=f"https://picsum.photos/150/150?{time.time()}",width=150,height=150
#         )
#         page.update()
#
#     page.add(sw,ft.ElevatedButton("Animate!",on_click=animate))

# PubSub
# def main(page:ft.Page):
#     page.title = "Flet Chat"
#     messages = ft.Column()
#     user = ft.TextField(hint_text="Your name",width=150)
#     message = ft.TextField(hint_text="Your message...",expand=True)
#
#
#     def on_message(msg):
#         messages.controls.append(ft.Text(msg))
#         page.update()
#
#     page.pubsub.subscribe(on_message)
#
#     def send_click(e):
#         page.pubsub.send_all(f"{user.value}:{message.value}")
#         message.value = ""
#         page.update()
#
#     send = ft.ElevatedButton("Send", on_click=send_click)
#
#     page.add(messages,ft.Row(controls=[user,message,send]))

# 用户控件
# class GreeterControl(ft.UserControl):
#     def build(self):
#         return ft.Text("Hello!")
# def main(page:ft.Page):
#     page.add(GreeterControl())

# 用户控件
# class GreeterControl(ft.UserControl):
#     def build(self):
#         return ft.Column([
#             ft.TextField(label="Your name"),
#             ft.ElevatedButton("Login")
#         ])
#
# def main(page:ft.Page):
#     page.add(GreeterControl())

# 用户控件
# class Counter(ft.UserControl):
#     def add_click(self,e):
#         self.counter += 1
#         self.text.value = str(self.counter)
#         self.update()
#
#     def build(self):
#         self.counter = 0
#         self.text = ft.Text(str(self.counter))
#         return ft.Row([self.text,ft.ElevatedButton("Add",on_click=self.add_click)])
#
# def main(page:ft.Page):
#     page.add(Counter(),Counter())

# 闭包写法
# class Counter(ft.UserControl):
#     def build(self):
#         self.counter = 0
#         text = ft.Text(str(self.counter))
#
#         def add_click(e):
#             self.counter += 1
#             text.value = str(self.counter)
#             self.update()
#
#         return ft.Row([text,ft.ElevatedButton("Add",on_click=add_click)])
#
# def main(page:ft.Page):
#     page.add(Counter(),Counter())

# 构造函数写法
# class Counter(ft.UserControl):
#     def __init__(self,initial_count):
#         super().__init__()
#         self.counter = initial_count
#
#     def build(self):
#         text = ft.Text(str(self.counter))
#
#         def add_click(e):
#             self.counter += 1
#             text.value = str(self.counter)
#             self.update()
#
#         return ft.Row([text,ft.ElevatedButton("Add",on_click=add_click)])
#
# def main(page:ft.Page):
#     page.add(Counter(100),Counter(200))

# 构造函数写法
# import time,threading
# class Counter(ft.UserControl):
#     def __init__(self,seconds):
#         super().__init__()
#         self.seconds = seconds
#
#     def update_timer(self):
#         while self.seconds and self.running:
#             mins,secs = divmod(self.seconds,60)
#             self.countdown.value = "{:02d}:{:02d}".format(mins,secs)
#             self.update()
#             time.sleep(1)
#             self.seconds -= 1
#
#     def did_mount(self):
#         self.running = True
#         self.th = threading.Thread(target=self.update_timer,args=(),daemon=True)
#         self.th.start()
#
#     def will_unmount(self):
#         self.running = False
#
#     def build(self):
#         self.countdown = ft.Text()
#         return self.countdown
#
# def main(page:ft.Page):
#     page.add(Counter(120),Counter(60))

# 控件的引用
# def main(page:ft.Page):
#     first_name = ft.TextField(label="First name",autofocus=True)
#     last_name = ft.TextField(label="Last name")
#     greetings = ft.Column()
#
#     def btn_click(e):
#         greetings.controls.append(ft.Text(f"Hello,{first_name.value} {last_name.value}!"))
#         first_name.value = ""
#         last_name.value = ""
#         page.update()
#         first_name.focus()
#
#     page.add(
#         first_name,
#         last_name,
#         ft.ElevatedButton("Say hello!",on_click=btn_click),
#         greetings
#     )

# 控件的引用
# def main(page:ft.Page):
#     first_name = ft.Ref[ft.TextField]()
#     last_name = ft.Ref[ft.TextField]()
#     greetings = ft.Ref[ft.Column]()
#
#     def btn_click(e):
#         greetings.current.controls.append(
#             ft.Text(f"Hello,{first_name.current.value} {last_name.current.value}!")
#         )
#         first_name.current.value = ""
#         last_name.current.value = ""
#         page.update()
#         first_name.current.focus()
#
#     page.add(
#         ft.TextField(ref=first_name,label="First name",autofocus=True),
#         ft.TextField(ref=last_name,label="Last name"),
#         ft.ElevatedButton("Say hello!",on_click=btn_click),
#         ft.Column(ref=greetings)
#     )

# 可及性
def main(page:ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_keyboard(e:ft.KeyboardEvent):
        print(e)
        if e.key == "S" and e.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()

    page.on_keyboard_event = on_keyboard

    txt_number = ft.Text("0",size=40)

    def button_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        txt_number,
        ft.Text("Press CTRL + S to toggle semantics debugger"),
        ft.FloatingActionButton(icon=ft.icons.ADD,tooltip="Increment number",on_click=button_click)
    )



ft.app(port=8550,target=main,view=ft.WEB_BROWSER)
# ft.app(target=main)
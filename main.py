import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.utils import platform

# 仅在安卓环境下导入权限模块
if platform == 'android':
    from android.permissions import request_permissions, Permission

class SimpleMusicPlayer(App):
    def build(self):
        self.sound = None
        
        # 界面布局
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.label = Label(
            text="极简播放器\n扫描路径: /sdcard/Download/", 
            halign="center", 
            font_size='18sp'
        )
        
        btn_play = Button(
            text="扫描并播放第一首歌", 
            size_hint=(1, 0.4), 
            background_color=(0.1, 0.6, 0.1, 1)
        )
        btn_play.bind(on_press=self.scan_and_play)
        
        btn_stop = Button(
            text="停止播放", 
            size_hint=(1, 0.4), 
            background_color=(0.8, 0.1, 0.1, 1)
        )
        btn_stop.bind(on_press=self.stop_music)
        
        layout.add_widget(self.label)
        layout.add_widget(btn_play)
        layout.add_widget(btn_stop)
        
        # 启动时请求权限（兼容安卓13+的媒体权限）
        if platform == 'android':
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_MEDIA_AUDIO  # 针对 Android 13+
            ])
            
        return layout

    def scan_and_play(self, instance):
        # 通用下载路径
        path = "/sdcard/Download/"
        
        try:
            if not os.path.exists(path):
                self.label.text = "找不到下载目录"
                return

            # 获取 mp3 文件列表
            files = [f for f in os.listdir(path) if f.lower().endswith('.mp3')]
            
            if not files:
                self.label.text = "Download 文件夹里\n没有找到 MP3 文件"
                return

            self.stop_music()

            # 加载并播放
            target = os.path.join(path, files[0])
            self.sound = SoundLoader.load(target)
            
            if self.sound:
                self.sound.play()
                self.label.text = f"正在播放:\n{files[0]}"
            else:
                self.label.text = "音频加载失败\n请检查文件格式"
        except Exception as e:
            self.label.text = f"错误: {str(e)}"

    def stop_music(self, *args):
        if self.sound:
            self.sound.stop()
            self.label.text = "播放已停止"

if __name__ == '__main__':
    SimpleMusicPlayer().run()

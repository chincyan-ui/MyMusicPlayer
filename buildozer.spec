[app]

# (str) 应用标题
title = My Music Player

# (str) 包名
package.name = mymusicplayer

# (str) 域名
package.domain = org.mymusic

# (str) 源代码所在路径
source.dir = .

# (list) 包含的文件后缀
source.include_exts = py,png,jpg,kv,atlas,mp3

# (str) 版本号
version = 0.1

# (list) 项目依赖 (核心：必须包含 android 和 sdl2 相关的库才能正常播放)
requirements = python3,kivy==2.3.0,android,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

# (str) 支持的屏幕方向 (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) 是否全屏
fullscreen = 1

# (list) 权限 (包含安卓13+所需的媒体音频权限)
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_AUDIO

# (int) 目标 Android API 等级 (建议 33 适配主流机型)
android.api = 33

# (int) 最小 Android API 等级
android.minapi = 21

# (str) Android SDK 等级 (通常与 API 等级一致)
android.sdk = 33

# (str) Android NDK 版本 (推荐版本)
android.ndk = 25b

# (bool) 是否接受 SDK 许可证
android.accept_sdk_license = True

# (list) 架构 (arm64-v8a 是目前绝大多数安卓手机的架构)
android.archs = arm64-v8a

# (str) 构建模式 (debug 或 release)
build_mode = debug

[buildozer]

# (int) 日志等级 (2 表示详细)
log_level = 2

# (int) 是否显示警告
warn_on_root = 1

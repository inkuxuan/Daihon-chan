# Project Introduction

This is a python app for VRChat users to send texts via Chatbox.

It acts like a normal text editor with multiple lines and allow the user to send any single line into the Chatbox in VRChat in a convenient way.

This is mainly meant to be used by event staff who can utilize chatbox to send script messages for those hard of hearing or deaf.

このRepoは、VRCのChatboxにメッセージを送るためのアプリです。

普通のテキストエディターの見た目で、複数行のテキストから、一行ごとにChatboxへ便利で発送することができます。

このアプリは、VRC上のイベントスタッフが、難聴またはろう者の方に、台本を可視化させるために開発されました。

# Instructions

End users could download the distribution EXE file and execute.

The app is simply a text editor with the additional ability to

* Highlight the current editing line
* Ctrl and mouse wheel to resize the font
* Shift-Enter to send the current line to VRChat and start a new line
* Ctrl-S to send the current line without starting a new line

**Note that this App is not capable of saving and reading files. Copy and paste your own script here**

**Do NOT close the command prompt when using the app**. This was bacause building the app with noconsole argument 
resulted in Windows Defender regarding it as a virus. 

Configuration files are saved in ~/.config/daihon_chan/

ユーザは、ReleaseからEXEファイルをダウンロードし、実行できます。

普通のテキストエディタの挙動のほか、

* 編集されている行のハイライト
* Ctrlを押しながらマウスホイールで文字の大きさを調整できる
* Shift-Enterキーで発送と改行
* Ctrl-Sで改行せずに発送

**注意：本アプリにはセーブ機能ついておりませんので、台本はコピペでやってください。**

**使用中にコマンドウィンドウは閉じないでください**（Buildする時NoConsole指定するとアンチヴィルスアプリに誤認識されるため、コマンドプロンプトを残しました）
Title: SEPSpeechTools
Date: 2017-01-27

Wordなどには文章の文字数を表示する機能があります。

しかし、日本語は漢字とかなの入り混じった文章のため、文字数自体が文章の長さとは言い切れない場合があります。

読み上げる際の時間の長さに直結しそうな要素を考えてみると、読み仮名の長さの方がより正確な文章の長さと言えるのではないでしょうか。

日本語アカデミックディベート界では立論の長さは文字数を単位とすることが基本と思われますが、それは文字数でしか文章の長さを見ることができなかったことにあります。

ところで、自然言語処理技術の中に、形態素解析というものがあります。この分野では辞書という形で膨大な単語の読み仮名情報が記録されています。

この辞書を利用することで、文章の読み仮名を取得することはできないでしょうか？

ということで生まれたのが[SEPSpeechTools]です。

## 謝辞

このツールの根幹には[mecab-ipadic-NEologd]があります。
最新の単語等を網羅したこの辞書がなければ、現実的に用いることができるツールにはなりませんでした。
この場を借りて感謝いたします。

その他、以下のツールを使用しております。

* [AquesTalk]
* [libmecab]
* mecab-ipadic
* [Qt5]


## 数え上げルール

* 拗音（`ゃ` `ゅ` `ょ`等）を0母音とします。
* 促音（`っ`）を0.5母音として数えます。
* 記号のうち、句点（`。`）や長音（`ー`）といったタイミングに関わるものを1母音として数えます。
* その他の記号は0母音として扱います。
* 読みの取得できない未知の単語については文字数をそのまま適用します。

## 使い方

テキストボックスにテキストを貼り付けると、ウィンドウ下部のステータスバーに文字数と母音数が表示されます。

![mainwindow.png]({attach}/img/sep-speech-tools/mainwindow.png)

どのようにルビが振られたかを見ることもできます。

![speechdialog.png]({attach}/img/sep-speech-tools/speechdialog.png)

機械音声生成ライブラリを用いて取得した読み仮名を読み上げることもできます。

詳しくは付属のhelp.htmlをお読みください。

## 注意事項

このツールはテキストエディタとして用いることを推奨しません。
テキストの変更ごとにテキストの解析処理が行われるため、重要な文章を計測にかける際は文章のバックアップをとった上で使用してください。

このツールを使用したことで生じた損害等は作者及びディベート情報研究所は一切関知しません。
全て自己責任でご使用ください。

## ダウンロード

ダウンロードはこちらから。

<a href="https://github.com/info-labs/sep-speech-tools/releases/tag/v0.0.1" class="btn btn-default btn-lg">
  <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> Download v0.0.1
</a>


[SEPSpeechTools]: https://github.com/info-labs/sep-speech-tools
[SEPSpeechTools v0.0.1]: https://github.com/info-labs/sep-speech-tools/releases/tag/v0.0.1

[AquesTalk]: http://www.a-quest.com/products/aquestalk.html
[libmecab]: http://taku910.github.io/mecab/
[mecab-ipadic-NEologd]: https://github.com/neologd/mecab-ipadic-neologd
[Qt5]: https://www.qt.io/

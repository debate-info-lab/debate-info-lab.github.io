Title: 次世代Webアーカイブを作成しました
Date: 2017-03-02

[次世代Webアーカイブ]はWebページのクロール結果にデジタル署名を施すことで、サービス外にデータを移したとしても有効な証拠であり続ける新しいWebアーカイブサービスです。

従来のWebアーカイブサービスは収集結果をWebサービス上で提供することで証拠としての機能を提供してきました。

しかし、Webサービスが終了してしまえば、それらの証拠は失われることになります。

仮にユーザーがアーカイブを手元で保管しようとしても、ユーザーの手元に渡った時点で改ざんの疑いが生じるため証拠の効力が失われてしまいます。

このサービスではリクエストされたURLの記録と同時にデジタル署名を付加することで、サーバーで作成された時点から改ざんが行われていないことを保証し、ユーザーの手元でも証拠の効力を維持できるようにしました。

アーカイブ手法はInternet Archive (archive.org)で実際に使用されているWARCファイルフォーマット（ISO 28500:2009）に準拠しています。

デジタル署名はOpenPGP（RFC 4880）の実装の一つ、GnuPGを用いて作成しています。

署名鍵は [Info Labs Archive (2017 4096 bits)] (keyid=728AA3B54479F3F4) になります。

デジタル署名用の[検証ツール]も用意しました。

アーカイブは<https://github.com/ikreymer/pywb>などを用いて閲覧することが出来ます。

GUIのアーカイブビューアについては現在鋭意製作中です。

## 参照

* [次世代Webアーカイブ]
* [QGPG]

[次世代Webアーカイブ]: https://info-labs.jp/crawler/
[検証ツール]: https://github.com/info-labs/QGPG/releases/tag/v0.1.0
[QGPG]: https://github.com/info-labs/QGPG
[Info Labs Archive (2017 4096 bits)]: https://info-labs.jp/pks/lookup?op=vindex&search=0x728aa3b54479f3f4

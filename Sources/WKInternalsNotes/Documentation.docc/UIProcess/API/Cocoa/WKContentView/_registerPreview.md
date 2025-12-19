# ``WKInternalsNotes/WKContentView/_registerPreview()``

リンクプレビュー用の登録処理を行う。

## Objective-C Declaration
```objective-c
- (void)_registerPreview;
```

## Discussion
`allowsLinkPreview` が無ければ何もしない。UIContextMenu を使う構成では外部 delegate を設定し、必要ならクリックドライバーを上書きする。レガシー経路では `UIPreviewItemController` を生成して delegate と関連ジェスチャを保持する。

## References
- [`WKContentViewInteraction.h#L1084`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1084)
- [`WKContentViewInteraction.mm#L14747`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14747)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

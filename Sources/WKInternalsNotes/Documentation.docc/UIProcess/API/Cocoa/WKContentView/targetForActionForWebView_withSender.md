# ``WKInternalsNotes/WKContentView/targetForActionForWebView(_:withSender:)``

WebView 向けアクションのターゲットを決定する。

## Objective-C Declaration
```objective-c
- (id)targetForActionForWebView:(SEL)action withSender:(id)sender;
```

## Discussion
非同期テキスト入力経路を使う場合、フォールバック用のアクションは `nil` を返してシステム側へ委ねる。その他は `super` の決定結果を返す。

## References
- [`WKContentViewInteraction.h#L761`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L761)
- [`WKContentViewInteraction.mm#L4946`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4946)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

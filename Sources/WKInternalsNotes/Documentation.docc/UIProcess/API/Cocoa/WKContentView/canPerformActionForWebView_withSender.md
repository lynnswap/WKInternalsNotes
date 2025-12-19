# ``WKInternalsNotes/WKContentView/canPerformActionForWebView(_:withSender:)``

WebView 向けアクションの有効可否を判定する。

## Objective-C Declaration
```objective-c
- (BOOL)canPerformActionForWebView:(SEL)action withSender:(id)sender;
```

## Discussion
編集状態や選択範囲、パスワードフィールド判定、ペーストボード内容などに基づいてアクション可否を返す。DOM ペースト要求中は `paste:` のみ許可する。

## References
- [`WKContentViewInteraction.h#L760`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L760)
- [`WKContentViewInteraction.mm#L4743`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4743)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

# ``WKInternalsNotes/WKContentView/_requestTextInputContextsInRect(_:completionHandler:)``

指定矩形内のテキスト入力コンテキストを取得する。

## Objective-C Declaration
```objective-c
- (void)_requestTextInputContextsInRect:(CGRect)rect completionHandler:(void (^)(NSArray<_WKTextInputContext *> *))completionHandler;
```

## Discussion
編集対象が無いと判定される場合は空配列を返す。`WebPageProxy` に問い合わせ、得られた `ElementContext` を `_WKTextInputContext` 配列に変換して返す。

## References
- [`WKContentViewInteraction.h#L916`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L916)
- [`WKContentViewInteraction.mm#L7482`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7482)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

# ``WKInternalsNotes/WKContentView/_focusTextInputContext(_:placeCaretAt:completionHandler:)``

指定コンテキストへフォーカスしてキャレットを配置する。

## Objective-C Declaration
```objective-c
- (void)_focusTextInputContext:(_WKTextInputContext *)context placeCaretAt:(CGPoint)point completionHandler:(void (^)(UIResponder<UITextInput> *))completionHandler;
```

## Discussion
`becomeFirstResponder` に失敗した場合は `nil` を返す。既に同一コンテキストなら読み取り専用かどうかで返却値を決め、そうでなければ `focusTextInputContextAndPlaceCaret` を呼び出して結果を返す。

## References
- [`WKContentViewInteraction.h#L917`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L917)
- [`WKContentViewInteraction.mm#L7453`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7453)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

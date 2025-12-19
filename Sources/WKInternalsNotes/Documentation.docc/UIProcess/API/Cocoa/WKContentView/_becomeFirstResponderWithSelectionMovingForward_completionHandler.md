# ``WKInternalsNotes/WKContentView/_becomeFirstResponderWithSelectionMovingForward(_:completionHandler:)``

初期フォーカス方向を指定して first responder を取得する。

## Objective-C Declaration
```objective-c
- (void)_becomeFirstResponderWithSelectionMovingForward:(BOOL)selectingForward completionHandler:(void (^)(BOOL didBecomeFirstResponder))completionHandler;
```

## Discussion
`_page->setInitialFocus` に `selectingForward` を渡して初期フォーカスを設定し、完了後に `becomeFirstResponder` を呼んで結果を completion handler に返す。

## References
- [WKContentViewInteraction.h#L844](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L844)
- [WKContentViewInteraction.mm#L6180](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6180)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

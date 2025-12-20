# ``WKInternalsNotes/WKFormInputSession/endEditing()``

カスタム入力ビューの編集終了を通知する。

## Objective-C Declaration
```objective-c
- (void)endEditing;
```

## Discussion
`_customInputView` が `WKFormControl` に準拠している場合のみ、`controlEndEditing` を呼び出して終了処理を委譲する。

## References
- [`WKContentViewInteraction.h#L329`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L329)
- [`WKContentViewInteraction.mm#L873`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L873)
- [`WKContentViewInteraction.mm#L875`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L875)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |

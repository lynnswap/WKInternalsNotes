# ``WKInternalsNotes/WKFormAccessoryViewDelegate/accessoryViewAutoFill(_:)``

AutoFill ボタンタップ時に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)accessoryViewAutoFill:(WKFormAccessoryView *)view;
```

## Discussion
`WKFormAccessoryView` の `_autoFill` から delegate に通知される。`WKContentViewInteraction` では `_WKInputDelegate` の `accessoryViewCustomButtonTappedInFormInputSession:` を呼び出す。

## References
- [`WKFormAccessoryView.mm#L302`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L302)
- [`WKContentViewInteraction.mm#L6290`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6290)
- [`WKFormAccessoryView.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

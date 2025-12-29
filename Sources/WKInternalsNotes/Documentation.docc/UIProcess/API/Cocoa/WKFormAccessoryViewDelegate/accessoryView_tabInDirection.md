# ``WKInternalsNotes/WKFormAccessoryViewDelegate/accessoryView(_:tabInDirection:)``

前後の入力要素へ移動する要求を通知する。

## Objective-C Declaration
```objective-c
- (void)accessoryView:(WKFormAccessoryView *)view tabInDirection:(WebKit::TabDirection)direction;
```

## Discussion
`WKFormAccessoryView` の前後ボタンから呼ばれる。`WKContentViewInteraction` では入力を終了して `focusNextFocusedElement` を実行し、完了後に `reloadInputViews` してフォーカス移動状態を解除する。

## References
- [`WKFormAccessoryView.mm#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L292)
- [`WKFormAccessoryView.mm#L297`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L297)
- [`WKContentViewInteraction.mm#L6271`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6271)
- [`WKFormAccessoryView.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

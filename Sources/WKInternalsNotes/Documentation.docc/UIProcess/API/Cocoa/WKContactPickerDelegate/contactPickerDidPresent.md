# ``WKInternalsNotes/WKContactPickerDelegate/contactPickerDidPresent(_:)``

連絡先ピッカーが表示されたことを通知する。

## Objective-C Declaration
```objective-c
- (void)contactPickerDidPresent:(WKContactPicker *)contactPicker;
```

## Discussion
`WKContactPicker` が `presentViewController` の completion で delegate を呼び出す。`WKContentViewInteraction` では `_didPresentContactPicker` を `WKWebView` に通知する。

## References
- [`WKContactPicker.mm#L168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.mm#L168)
- [`WKContentViewInteraction.mm#L9794`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9794)
- [`WKContactPicker.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.h#L59)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

# ``WKInternalsNotes/WKContactPickerDelegate/contactPickerDidDismiss(_:)``

連絡先ピッカーが閉じられたことを通知する。

## Objective-C Declaration
```objective-c
- (void)contactPickerDidDismiss:(WKContactPicker *)contactPicker;
```

## Discussion
`WKContactPicker` の `_contactPickerDidDismissWithContactInfo:` から delegate に通知される。`WKContentViewInteraction` では `_contactPicker` の delegate を解除して破棄し、`WKWebView` に `_didDismissContactPicker` を伝える。

## References
- [`WKContactPicker.mm#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.mm#L230)
- [`WKContentViewInteraction.mm#L9801`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9801)
- [`WKContactPicker.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.h#L60)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

# ``WKInternalsNotes/WKContactPicker/initWithView(_:)``

`WKWebView` を保持する初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKWebView *)view;
```

## Discussion
`[super init]` に成功した場合、`_webView` に `view` を保持する。

## References
- [`WKContactPicker.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.h#L47)
- [`WKContactPicker.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |

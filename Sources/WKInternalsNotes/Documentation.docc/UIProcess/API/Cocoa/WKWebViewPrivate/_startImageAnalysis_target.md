# ``WKInternalsNotes/WKWebView/_startImageAnalysis(_:target:)``

`_startImageAnalysis` を開始する。

## Objective-C Declaration
```objective-c
- (void)_startImageAnalysis:(NSString *)identifier target:(NSString *)targetIdentifier WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L518`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L518)
- [`WKWebView.mm#L4142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4142)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

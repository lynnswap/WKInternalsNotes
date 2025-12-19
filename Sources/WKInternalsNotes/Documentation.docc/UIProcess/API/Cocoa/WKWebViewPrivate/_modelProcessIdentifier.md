# ``WKInternalsNotes/WKWebView/_modelProcessIdentifier``

`_modelProcessIdentifier` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) pid_t _modelProcessIdentifier WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L227)
- [`API/Cocoa/WKWebView.mm#L4896`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4896)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

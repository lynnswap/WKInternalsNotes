# ``WKInternalsNotes/WKWebView/_wasPrivateRelayed``

`_wasPrivateRelayed` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _wasPrivateRelayed WK_API_AVAILABLE(macos(13.1), ios(16.2));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L238)
- [`WKWebView.mm#L3831`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3831)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

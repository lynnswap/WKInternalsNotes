# ``WKInternalsNotes/WKWebView/_setPageScale(_:withOrigin:)``

`_setPageScale` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPageScale:(CGFloat)scale withOrigin:(CGPoint)origin;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L62)
- [`WKWebViewTesting.mm#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L224)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

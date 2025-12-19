# ``WKInternalsNotes/WKWebView/_didLoadAppInitiatedRequest(_:)``

`_didLoadAppInitiatedRequest` を実行する。

## Objective-C Declaration
```objective-c
- (void)_didLoadAppInitiatedRequest:(void (^)(BOOL result))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L509`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L509)
- [`WKWebView.mm#L4771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4771)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

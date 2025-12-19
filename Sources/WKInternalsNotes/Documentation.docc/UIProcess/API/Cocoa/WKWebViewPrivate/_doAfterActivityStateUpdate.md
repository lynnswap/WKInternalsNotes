# ``WKInternalsNotes/WKWebView/_doAfterActivityStateUpdate(_:)``

`_doAfterActivityStateUpdate` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterActivityStateUpdate:(void (^)(void))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L125)
- [`API/Cocoa/WKWebViewTesting.mm#L541`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L541)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

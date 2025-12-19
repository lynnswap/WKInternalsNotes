# ``WKInternalsNotes/WKWebView/_resizeWhileHidingContentWithUpdates(_:)``

`_resizeWhileHidingContentWithUpdates` を実行する。

## Objective-C Declaration
```objective-c
- (void)_resizeWhileHidingContentWithUpdates:(void (^)(void))updateBlock;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L753`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L753)
- [`API/ios/WKWebViewIOS.mm#L4778`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4778)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

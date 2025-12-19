# ``WKInternalsNotes/WKWebView/_scrollToRect(_:origin:minimumScrollDistance:)``

`_scrollToRect` を実行する。

## Objective-C Declaration
```objective-c
- (BOOL)_scrollToRect:(WebCore::FloatRect)targetRect origin:(WebCore::FloatPoint)origin minimumScrollDistance:(float)minimumScrollDistance;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/ios/WKWebViewIOS.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L81)
- [`API/ios/WKWebViewIOS.mm#L1800`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L1800)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

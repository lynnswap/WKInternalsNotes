# ``WKInternalsNotes/WKWebView/_findInteraction``

`_findInteraction` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _UIFindInteraction *_findInteraction WK_API_AVAILABLE(ios(16.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L676`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L676)
- [`WKWebViewIOS.mm#L460`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L460)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

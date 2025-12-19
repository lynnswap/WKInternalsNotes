# ``WKInternalsNotes/WKWebView/_scrollPerformanceDataCollectionEnabled``

`_scrollPerformanceDataCollectionEnabled` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setScrollPerformanceDataCollectionEnabled:) BOOL _scrollPerformanceDataCollectionEnabled WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setScrollPerformanceDataCollectionEnabled:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L399`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L399)
- [`API/Cocoa/WKWebView.mm#L6032`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6032)
- [`API/Cocoa/WKWebView.mm#L6026`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6026)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

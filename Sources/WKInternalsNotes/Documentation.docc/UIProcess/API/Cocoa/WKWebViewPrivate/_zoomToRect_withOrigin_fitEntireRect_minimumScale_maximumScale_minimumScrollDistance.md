# ``WKInternalsNotes/WKWebView/_zoomToRect(_:withOrigin:fitEntireRect:minimumScale:maximumScale:minimumScrollDistance:)``

`_zoomToRect` を実行する。

## Objective-C Declaration
```objective-c
- (BOOL)_zoomToRect:(WebCore::FloatRect)targetRect withOrigin:(WebCore::FloatPoint)origin fitEntireRect:(BOOL)fitEntireRect minimumScale:(double)minimumScale maximumScale:(double)maximumScale minimumScrollDistance:(float)minimumScrollDistance;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L88)
- [`WKWebViewIOS.mm#L2104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L2104)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

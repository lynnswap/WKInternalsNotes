# ``WKInternalsNotes/WKWebView/_targetContentZoomScaleForRect(_:currentScale:fitEntireRect:minimumScale:maximumScale:)``

`_targetContentZoomScaleForRect` を実行する。

## Objective-C Declaration
```objective-c
- (double)_targetContentZoomScaleForRect:(const WebCore::FloatRect&)targetRect currentScale:(double)currentScale fitEntireRect:(BOOL)fitEntireRect minimumScale:(double)minimumScale maximumScale:(double)maximumScale;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L86)
- [`WKWebViewIOS.mm#L2092`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L2092)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

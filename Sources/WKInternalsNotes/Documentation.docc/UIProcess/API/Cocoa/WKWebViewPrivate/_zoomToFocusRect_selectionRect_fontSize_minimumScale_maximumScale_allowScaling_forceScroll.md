# ``WKInternalsNotes/WKWebView/_zoomToFocusRect(_:selectionRect:fontSize:minimumScale:maximumScale:allowScaling:forceScroll:)``

`_zoomToFocusRect` を実行する。

## Objective-C Declaration
```objective-c
- (void)_zoomToFocusRect:(const WebCore::FloatRect&)focusedElementRect selectionRect:(const WebCore::FloatRect&)selectionRectInDocumentCoordinates fontSize:(float)fontSize minimumScale:(double)minimumScale maximumScale:(double)maximumScale allowScaling:(BOOL)allowScaling forceScroll:(BOOL)forceScroll;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/ios/WKWebViewIOS.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L87)
- [`API/ios/WKWebViewIOS.mm#L1913`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L1913)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

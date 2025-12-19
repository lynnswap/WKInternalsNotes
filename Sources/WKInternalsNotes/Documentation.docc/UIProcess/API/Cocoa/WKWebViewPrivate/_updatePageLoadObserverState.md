# ``WKInternalsNotes/WKWebView/_updatePageLoadObserverState()``

`_updatePageLoadObserverState` を更新する。

## Objective-C Declaration
```objective-c
- (void)_updatePageLoadObserverState NS_DIRECT;
```

## Discussion
iOS では `PageClientImplIOS` から呼ばれて状態を更新する。

## References
- [`WKWebViewIOS.h#L232`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L232)
- [`PageClientImplIOS.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/PageClientImplIOS.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

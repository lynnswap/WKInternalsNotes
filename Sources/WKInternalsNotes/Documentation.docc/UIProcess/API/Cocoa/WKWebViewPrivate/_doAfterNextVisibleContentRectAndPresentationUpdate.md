# ``WKInternalsNotes/WKWebView/_doAfterNextVisibleContentRectAndPresentationUpdate(_:)``

`_doAfterNextVisibleContentRectAndPresentationUpdate` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterNextVisibleContentRectAndPresentationUpdate:(void (^)(void))updateBlock;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L553`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L553)
- [`WKWebView.mm#L1997`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1997)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

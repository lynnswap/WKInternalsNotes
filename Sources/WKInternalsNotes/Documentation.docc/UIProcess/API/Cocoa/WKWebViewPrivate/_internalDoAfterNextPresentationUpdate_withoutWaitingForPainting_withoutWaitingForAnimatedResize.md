# ``WKInternalsNotes/WKWebView/_internalDoAfterNextPresentationUpdate(_:withoutWaitingForPainting:withoutWaitingForAnimatedResize:)``

`_internalDoAfterNextPresentationUpdate` を実行する。

## Objective-C Declaration
```objective-c
- (void)_internalDoAfterNextPresentationUpdate:(void (^)(void))updateBlock withoutWaitingForPainting:(BOOL)withoutWaitingForPainting withoutWaitingForAnimatedResize:(BOOL)withoutWaitingForAnimatedResize;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewInternal.h#L551`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L551)
- [`API/Cocoa/WKWebView.mm#L1960`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1960)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

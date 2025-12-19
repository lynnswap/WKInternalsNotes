# ``WKInternalsNotes/WKWebView/_setContentOffsetX(_:y:animated:)``

`_setContentOffsetX` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setContentOffsetX:(NSNumber *)x y:(NSNumber *)y animated:(BOOL)animated NS_SWIFT_NAME(_setContentOffset(x:y:animated:));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L671`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L671)
- [`WKWebViewMac.mm#L1413`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1413)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

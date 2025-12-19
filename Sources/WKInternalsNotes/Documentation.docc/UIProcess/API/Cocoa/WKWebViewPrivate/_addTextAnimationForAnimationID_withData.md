# ``WKInternalsNotes/WKWebView/_addTextAnimationForAnimationID(_:withData:)``

`_addTextAnimationForAnimationID` を追加する。

## Objective-C Declaration
```objective-c
- (void)_addTextAnimationForAnimationID:(NSUUID *)uuid withData:(const WebCore::TextAnimationData&)styleData;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L546`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L546)
- [`WKWebView.mm#L2913`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2913)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

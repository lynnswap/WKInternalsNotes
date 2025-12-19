# ``WKInternalsNotes/WKWebView/_setNowPlayingMetadataObserver(_:)``

`_setNowPlayingMetadataObserver` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setNowPlayingMetadataObserver:(void(^)(_WKNowPlayingMetadata *))observer;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L70)
- [`API/Cocoa/WKWebViewTesting.mm#L283`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L283)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

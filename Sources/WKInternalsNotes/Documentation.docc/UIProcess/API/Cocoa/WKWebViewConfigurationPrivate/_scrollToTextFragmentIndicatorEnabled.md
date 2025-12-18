# ``WKInternalsNotes/WKWebViewConfiguration/_scrollToTextFragmentIndicatorEnabled``

scroll-to-text-fragment の indicator

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setScrollToTextFragmentIndicatorEnabled:) BOOL _scrollToTextFragmentIndicatorEnabled WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_scrollToTextFragmentIndicatorEnabled = YES`: scroll-to-text-fragment の indicator。
- `_scrollToTextFragmentIndicatorEnabled = NO`: scroll-to-text-fragment の indicator（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L176)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L264`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L264)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

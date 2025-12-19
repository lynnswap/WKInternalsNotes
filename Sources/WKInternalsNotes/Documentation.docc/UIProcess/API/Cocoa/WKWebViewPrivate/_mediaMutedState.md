# ``WKInternalsNotes/WKWebView/_mediaMutedState``

`_mediaMutedState` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKMediaMutedState _mediaMutedState WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L410`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L410)
- [`WKWebView.mm#L4457`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4457)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

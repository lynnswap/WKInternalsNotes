# ``WKInternalsNotes/WKWebView/_hasActiveNowPlayingSession``

`_hasActiveNowPlayingSession` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _hasActiveNowPlayingSession WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
PageClientImplCocoa から `_setHasActiveNowPlayingSession:` が呼ばれて更新される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L619`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L619)
- [`Cocoa/PageClientImplCocoa.mm#L422`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/PageClientImplCocoa.mm#L422)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

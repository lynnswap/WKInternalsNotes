# ``WKInternalsNotes/WKWebView/_nowPlayingMediaTitleAndArtist(_:)``

`_nowPlayingMediaTitleAndArtist` を実行する。

## Objective-C Declaration
```objective-c
- (void)_nowPlayingMediaTitleAndArtist:(void (^)(NSString *, NSString *))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L441`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L441)
- [`WKWebView.mm#L4283`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4283)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

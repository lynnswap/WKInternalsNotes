# ``WKInternalsNotes/WKWebViewConfiguration/_allowsInlineMediaPlaybackAfterFullscreen``

fullscreen 後に inline 再生を許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsInlineMediaPlaybackAfterFullscreen:) BOOL _allowsInlineMediaPlaybackAfterFullscreen  WK_API_AVAILABLE(ios(10.0));
```

## Default Value
iOS: `!allowsInlineMediaPlayback`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowsInlineMediaPlaybackAfterFullscreen = YES`: fullscreen 後に inline 再生を許可。
- `_allowsInlineMediaPlaybackAfterFullscreen = NO`: fullscreen 後に inline 再生を許可（無効）。

## Details
- iPhone: `YES`, iPad: `NO`（概ね）

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L117)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L247)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

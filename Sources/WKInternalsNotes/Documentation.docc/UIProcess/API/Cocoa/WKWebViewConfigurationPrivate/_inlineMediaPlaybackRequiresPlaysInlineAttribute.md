# ``WKInternalsNotes/WKWebViewConfiguration/_inlineMediaPlaybackRequiresPlaysInlineAttribute``

inline 再生に `playsinline` 必須か

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInlineMediaPlaybackRequiresPlaysInlineAttribute:) BOOL _inlineMediaPlaybackRequiresPlaysInlineAttribute WK_API_AVAILABLE(ios(10.0));
```

## Default Value
iOS: `!allowsInlineMediaPlayback`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_inlineMediaPlaybackRequiresPlaysInlineAttribute = YES`: inline 再生に `playsinline` 必須か。
- `_inlineMediaPlaybackRequiresPlaysInlineAttribute = NO`: inline 再生に `playsinline` 必須か（無効）。

## Details
- iPhone: `YES`, iPad: `NO`（概ね）

## References
- [`WKWebViewConfigurationPrivate.h#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L116)
- [`WKWebViewConfiguration.mm#L871`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L871)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

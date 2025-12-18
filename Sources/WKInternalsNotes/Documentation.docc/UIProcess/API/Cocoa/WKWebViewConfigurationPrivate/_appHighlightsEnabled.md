# ``WKInternalsNotes/WKWebViewConfiguration/_appHighlightsEnabled``

App Highlights を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAppHighlightsEnabled:) BOOL _appHighlightsEnabled WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_appHighlightsEnabled = YES`: App Highlights を有効化。
- `_appHighlightsEnabled = NO`: App Highlights を有効化（無効）。

## Details
- `ENABLE(APP_HIGHLIGHTS)` が無効なら常に `NO`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L152)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1450`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1450)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

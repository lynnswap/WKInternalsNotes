# ``WKInternalsNotes/WKWebViewConfiguration/_incompleteImageBorderEnabled``

incomplete image の border 表示

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setIncompleteImageBorderEnabled:) BOOL _incompleteImageBorderEnabled WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_incompleteImageBorderEnabled = YES`: incomplete image の border 表示。
- `_incompleteImageBorderEnabled = NO`: incomplete image の border 表示（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L95)
- [`WKWebViewConfiguration.mm#L1060`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1060)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

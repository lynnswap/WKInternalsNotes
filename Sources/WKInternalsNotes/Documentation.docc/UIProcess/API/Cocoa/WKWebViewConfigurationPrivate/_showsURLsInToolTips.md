# ``WKInternalsNotes/WKWebViewConfiguration/_showsURLsInToolTips``

URL をツールチップに表示

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShowsURLsInToolTips:) BOOL _showsURLsInToolTips WK_API_AVAILABLE(macos(10.12));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_showsURLsInToolTips = YES`: URL をツールチップに表示。
- `_showsURLsInToolTips = NO`: URL をツールチップに表示（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L126)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1250`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1250)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

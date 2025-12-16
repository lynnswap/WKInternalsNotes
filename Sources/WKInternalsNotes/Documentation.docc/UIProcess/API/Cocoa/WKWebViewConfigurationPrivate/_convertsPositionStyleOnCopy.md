# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_convertsPositionStyleOnCopy``

コピー時に `position` を変換する

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setConvertsPositionStyleOnCopy:) BOOL _convertsPositionStyleOnCopy WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_convertsPositionStyleOnCopy = YES`: コピー時に `position` を変換する。
- `_convertsPositionStyleOnCopy = NO`: コピー時に `position` を変換する（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L78)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L815`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L815)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

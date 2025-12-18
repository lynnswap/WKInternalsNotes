# ``WKInternalsNotes/WKWebViewConfiguration/_initialCapitalizationEnabled``

編集時の自動大文字化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInitialCapitalizationEnabled:) BOOL _initialCapitalizationEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_initialCapitalizationEnabled = YES`: 編集時の自動大文字化。
- `_initialCapitalizationEnabled = NO`: 編集時の自動大文字化（無効）。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L89)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1209)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

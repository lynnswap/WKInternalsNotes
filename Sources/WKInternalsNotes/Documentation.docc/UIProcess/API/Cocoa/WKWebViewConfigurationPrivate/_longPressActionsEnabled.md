# ``WKInternalsNotes/WKWebViewConfiguration/_longPressActionsEnabled``

long press actions を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLongPressActionsEnabled:) BOOL _longPressActionsEnabled WK_API_AVAILABLE(ios(12.0));
```

## Default Value
iOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_longPressActionsEnabled = YES`: long press actions を有効化。
- `_longPressActionsEnabled = NO`: long press actions を有効化（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L119)
- [`WKWebViewConfiguration.mm#L258`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L258)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

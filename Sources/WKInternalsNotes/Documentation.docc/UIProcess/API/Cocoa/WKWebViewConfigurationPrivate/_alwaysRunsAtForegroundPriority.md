# ``WKInternalsNotes/WKWebViewConfiguration/_alwaysRunsAtForegroundPriority``

旧API（`_clientNavigationsRunAtForegroundPriority` 相当）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAlwaysRunsAtForegroundPriority:) BOOL _alwaysRunsAtForegroundPriority WK_API_DEPRECATED_WITH_REPLACEMENT("_clientNavigationsRunAtForegroundPriority", ios(9.0, 14.0));
```

## Default Value
iOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_alwaysRunsAtForegroundPriority = YES`: 旧API（`_clientNavigationsRunAtForegroundPriority` 相当）。
- `_alwaysRunsAtForegroundPriority = NO`: 旧API（`_clientNavigationsRunAtForegroundPriority` 相当）（無効）。

## Details
- Deprecated

## References
- [`WKWebViewConfigurationPrivate.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L115)
- [`WKWebViewConfiguration.mm#L861`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L861)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

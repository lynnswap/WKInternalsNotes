# ``WKInternalsNotes/WKWebViewConfiguration/_clientNavigationsRunAtForegroundPriority``

client navigation を foreground 優先度で実行

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setClientNavigationsRunAtForegroundPriority:) BOOL _clientNavigationsRunAtForegroundPriority WK_API_AVAILABLE(macos(13.5), ios(13.4));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_clientNavigationsRunAtForegroundPriority = YES`: client navigation を foreground 優先度で実行。
- `_clientNavigationsRunAtForegroundPriority = NO`: client navigation を foreground 優先度で実行（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L111)
- [`WKWebViewConfiguration.mm#L835`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L835)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

# ``WKInternalsNotes/WKWebViewConfiguration/_canShowWhileLocked``

ロック中に表示可能

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCanShowWhileLocked:) BOOL _canShowWhileLocked WK_API_AVAILABLE(ios(13.0));
```

## Default Value
iOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_canShowWhileLocked = YES`: ロック中に表示可能。
- `_canShowWhileLocked = NO`: ロック中に表示可能（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L122)
- [`WKWebViewConfiguration.mm#L936`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L936)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

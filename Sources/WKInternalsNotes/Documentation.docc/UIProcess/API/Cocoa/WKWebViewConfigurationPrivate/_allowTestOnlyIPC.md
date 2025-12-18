# ``WKInternalsNotes/WKWebViewConfiguration/_allowTestOnlyIPC``

Test-only IPC を許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowTestOnlyIPC:) BOOL _allowTestOnlyIPC WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_allowTestOnlyIPC = YES`: Test-only IPC を許可。
- `_allowTestOnlyIPC = NO`: Test-only IPC を許可（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L154)
- [`WKWebViewConfiguration.mm#L1459`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1459)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

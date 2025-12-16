# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_shouldSendConsoleLogsToUIProcessForTesting``

console log を UIProcess に転送（テスト用）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldSendConsoleLogsToUIProcessForTesting:) BOOL _shouldSendConsoleLogsToUIProcessForTesting WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldSendConsoleLogsToUIProcessForTesting = YES`: console log を UIProcess に転送（テスト用）。
- `_shouldSendConsoleLogsToUIProcessForTesting = NO`: console log を UIProcess に転送（テスト用）（無効）。

## Details
- テスト用

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L101)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L800`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L800)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

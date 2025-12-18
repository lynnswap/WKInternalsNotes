# ``WKInternalsNotes/WKPreferences/_logsPageMessagesToSystemConsoleEnabled``

Log page messages to system console を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLogsPageMessagesToSystemConsoleEnabled:) BOOL _logsPageMessagesToSystemConsoleEnabled WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_logsPageMessagesToSystemConsoleEnabled = YES`: Log page messages to system console を有効化する。
- `_logsPageMessagesToSystemConsoleEnabled = NO`: Log page messages to system console を無効化する。
- Implementation: [`Source/WebCore/page/FrameConsoleClient.cpp#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/FrameConsoleClient.cpp#L140) の `FrameConsoleClient::addMessage` が `logsPageMessagesToSystemConsoleEnabled()` を参照する。

## Details
- WebPreferences key: `LogsPageMessagesToSystemConsoleEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L90)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L446`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L446)
- [`Source/WebCore/page/FrameConsoleClient.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/FrameConsoleClient.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4670`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4670) (key: `LogsPageMessagesToSystemConsoleEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

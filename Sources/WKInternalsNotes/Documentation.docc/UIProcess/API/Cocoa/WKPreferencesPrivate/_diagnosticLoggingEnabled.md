# ``WKInternalsNotes/WKPreferences/_diagnosticLoggingEnabled``

Diagnostic logging を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDiagnosticLoggingEnabled:) BOOL _diagnosticLoggingEnabled WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_diagnosticLoggingEnabled = YES`: Diagnostic logging を有効化する。
- `_diagnosticLoggingEnabled = NO`: Diagnostic logging を無効化する。
- Implementation: [`Source/WebCore/page/Page.cpp#L1631`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp#L1631) の `Page::diagnosticLoggingClient` が `diagnosticLoggingEnabled()` を参照する。

## Details
- WebPreferences key: `DiagnosticLoggingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L101)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L516`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L516)
- [`Source/WebCore/page/Page.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2453`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2453) (key: `DiagnosticLoggingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

# ``WKInternalsNotes/WKWebViewConfiguration/_shouldRelaxThirdPartyCookieBlocking``

3rd-party cookie blocking を緩める

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldRelaxThirdPartyCookieBlocking:) BOOL _shouldRelaxThirdPartyCookieBlocking WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldRelaxThirdPartyCookieBlocking = YES`: 3rd-party cookie blocking を緩める。
- `_shouldRelaxThirdPartyCookieBlocking = NO`: 3rd-party cookie blocking を緩める（無効）。

## Details
- Safari/TestWebKitAPI など限定。条件外で setter は例外

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L149)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1479`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1479)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

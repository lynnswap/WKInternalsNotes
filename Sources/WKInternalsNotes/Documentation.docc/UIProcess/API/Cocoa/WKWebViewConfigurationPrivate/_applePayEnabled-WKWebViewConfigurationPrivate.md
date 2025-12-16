# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_applePayEnabled``

Apple Pay / Payment Request を許可

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setApplePayEnabled:) BOOL _applePayEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `ENABLE(APPLE_PAY_REMOTE_UI) ? YES : NO` / macOS: `ENABLE(APPLE_PAY_REMOTE_UI) ? YES : NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_applePayEnabled = YES`: Apple Pay / Payment Request を許可。
- `_applePayEnabled = NO`: Apple Pay / Payment Request を許可（無効）。

## Details
- `ApplePayEnabled`（`WKPreferences`）＋ override

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L90)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1321)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

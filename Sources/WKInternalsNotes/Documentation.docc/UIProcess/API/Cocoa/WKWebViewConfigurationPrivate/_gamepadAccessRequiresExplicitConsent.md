# ``WKInternalsNotes/WKWebViewConfiguration/_gamepadAccessRequiresExplicitConsent``

gamepad access に明示同意を要求

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setGamepadAccessRequiresExplicitConsent:) BOOL _gamepadAccessRequiresExplicitConsent WK_API_AVAILABLE(visionos(2.0));
```

## Default Value
`NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_gamepadAccessRequiresExplicitConsent = YES`: gamepad access に明示同意を要求。
- `_gamepadAccessRequiresExplicitConsent = NO`: gamepad access に明示同意を要求（無効）。

## Details
- `ENABLE(GAMEPAD)` が無効なら常に `NO`

## References
- [`WKWebViewConfigurationPrivate.h#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L181)
- [`WKWebViewConfiguration.mm#L268`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L268)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

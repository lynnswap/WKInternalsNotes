# ``WKInternalsNotes/WKWebViewConfiguration/_legacyEncryptedMediaAPIEnabled``

legacy EME API を有効化

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLegacyEncryptedMediaAPIEnabled:) BOOL _legacyEncryptedMediaAPIEnabled WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_legacyEncryptedMediaAPIEnabled = YES`: legacy EME API を有効化。
- `_legacyEncryptedMediaAPIEnabled = NO`: legacy EME API を有効化（無効）。

## References
- [`WKWebViewConfigurationPrivate.h#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L140)
- [`WKWebViewConfiguration.mm#L1408`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1408)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

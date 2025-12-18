# ``WKInternalsNotes/WKWebViewConfiguration/_maskedURLSchemes``

URL scheme マスク対象

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setMaskedURLSchemes:) NSSet<NSString *> *_maskedURLSchemes WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `[]` / macOS: `[]`

## Discussion
- この API を使わない場合: マスク対象 scheme が空のため、JS バインディングへ URL がそのまま露出する。
- `_maskedURLSchemes` を設定すると: 対象 scheme の URL が、JS バインディングでは `webkit-masked-url://hidden/` に置き換えられる。
- 空 set に戻すと: マスクしない。

## Details
- Web Extension controller 設定時は既定で extension schemes になる場合あり

## References
- [`WKWebViewConfigurationPrivate.h#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L104)
- [`WKWebViewConfiguration.mm#L1095`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1095)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

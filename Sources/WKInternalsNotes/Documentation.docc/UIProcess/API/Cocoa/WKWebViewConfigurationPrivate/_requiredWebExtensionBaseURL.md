# ``WKInternalsNotes/WKWebViewConfiguration/_requiredWebExtensionBaseURL``

Web Extension 用の「必須 base URL」制約

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, setter=_setRequiredWebExtensionBaseURL:) NSURL *_requiredWebExtensionBaseURL;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: base URL 制約はなく、（Web Extension URL 以外への）ナビゲーションは通常どおり許可される。
- `_requiredWebExtensionBaseURL` を設定すると: base URL と一致しない URL へのナビゲーションは navigation error になる。
- `nil` に戻すと: base URL 制約を解除する。

## Details
- `ENABLE(WK_WEB_EXTENSIONS)` のみ

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L66)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L388)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

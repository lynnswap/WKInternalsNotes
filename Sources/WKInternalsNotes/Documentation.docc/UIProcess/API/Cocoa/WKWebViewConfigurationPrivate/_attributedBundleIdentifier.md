# ``WKInternalsNotes/WKWebViewConfiguration/_attributedBundleIdentifier``

ネットワーク活動の attribution 対象 bundle id

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAttributedBundleIdentifier:) NSString *_attributedBundleIdentifier;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: network activity は通常の attribution のまま扱われる（`nil`）。
- `_attributedBundleIdentifier` を設定すると: この `WKWebView` の network activity を、指定 bundle id のアプリとして attribution する。
- `nil` に戻すと: attribution の指定を解除する。

## References
- [`WKWebViewConfigurationPrivate.h#L168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L168)
- [`WKWebViewConfiguration.mm#L1537`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1537)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

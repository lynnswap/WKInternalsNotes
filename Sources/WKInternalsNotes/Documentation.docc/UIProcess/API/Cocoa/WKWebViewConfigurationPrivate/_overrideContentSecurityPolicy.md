# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_overrideContentSecurityPolicy``

CSP を上書き

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOverrideContentSecurityPolicy:) NSString *_overrideContentSecurityPolicy WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: CSP は通常どおりレスポンスヘッダ等に従う（`nil`）。
- `_overrideContentSecurityPolicy` を設定すると: 指定文字列が CSP として適用される（既存 CSP を上書き/追加する用途）。
- `nil` に戻すと: 上書きを解除する。

## Details
- null 文字列は `nil` として返る

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L138)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1367`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1367)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

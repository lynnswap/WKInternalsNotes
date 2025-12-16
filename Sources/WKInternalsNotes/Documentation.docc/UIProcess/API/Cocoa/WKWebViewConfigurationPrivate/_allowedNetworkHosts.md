# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_allowedNetworkHosts``

許可するネットワーク host 制限

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setAllowedNetworkHosts:) NSSet<NSString *> *_allowedNetworkHosts WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: `nil`（無制限）のため、HTTP/WS の network load は通常どおり許可される。
- `_allowedNetworkHosts` を設定すると: host がこの set に含まれる場合のみ、HTTP/WS の network load が許可される。
- `nil` に戻すと: 無制限に戻る。空 set にすると: HTTP/WS の network load をすべてブロックする。

## Details
- `nil` は “無制限”

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L107)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1132)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |

# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_shouldAcceptInsecureCertificatesForWebSockets``

WebSocket で不正な証明書を許可するかのフラグ（deprecated）。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldAcceptInsecureCertificatesForWebSockets:) BOOL _shouldAcceptInsecureCertificatesForWebSockets WK_API_DEPRECATED_WITH_REPLACEMENT("WKNavigationDelegate.didReceiveAuthenticationChallenge", macos(13.0, 14.4), ios(16.0, 17.4), visionos(1.0, 1.1));
```

## Default Value
`false` を返す。

## Discussion
getter は常に `false` を返し、setter は `UNUSED_PARAM` で実質的に何もしない。

## References
- [_WKWebsiteDataStoreConfiguration.h#L71](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L71)
- [_WKWebsiteDataStoreConfiguration.mm#L751](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L751)
- [_WKWebsiteDataStoreConfiguration.mm#L756](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L756)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

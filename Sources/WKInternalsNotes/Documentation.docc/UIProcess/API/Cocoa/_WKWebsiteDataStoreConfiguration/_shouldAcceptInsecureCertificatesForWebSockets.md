# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_shouldAcceptInsecureCertificatesForWebSockets``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldAcceptInsecureCertificatesForWebSockets:) BOOL _shouldAcceptInsecureCertificatesForWebSockets WK_API_DEPRECATED_WITH_REPLACEMENT("WKNavigationDelegate.didReceiveAuthenticationChallenge", macos(13.0, 14.4), ios(16.0, 17.4), visionos(1.0, 1.1));
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKWebsiteDataStoreConfiguration.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

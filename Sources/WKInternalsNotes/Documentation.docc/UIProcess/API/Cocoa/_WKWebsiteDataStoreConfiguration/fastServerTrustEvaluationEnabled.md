# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/fastServerTrustEvaluationEnabled``

高速なサーバートラスト評価を有効にするかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL fastServerTrustEvaluationEnabled WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `fastServerTrustEvaluationEnabled` の値を返す。

## Discussion
getter は `_configuration->fastServerTrustEvaluationEnabled()` を返し、setter は `_configuration->setFastServerTrustEvaluationEnabled` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L54](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L54)
- [_WKWebsiteDataStoreConfiguration.mm#L485](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L485)
- [_WKWebsiteDataStoreConfiguration.mm#L490](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L490)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

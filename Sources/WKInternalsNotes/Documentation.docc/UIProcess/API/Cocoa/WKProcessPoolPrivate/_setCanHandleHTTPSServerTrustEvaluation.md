# ``WKInternalsNotes/WKProcessPool/_setCanHandleHTTPSServerTrustEvaluation(_:)``

HTTPS サーバー信頼評価を扱えるかのフラグを設定する。

## Objective-C Declaration
```objective-c
- (void)_setCanHandleHTTPSServerTrustEvaluation:(BOOL)value WK_API_DEPRECATED_WITH_REPLACEMENT("_WKWebsiteDataStoreConfiguration.fastServerTrustEvaluationEnabled", macos(10.11, 10.15.4), ios(9.0, 13.4));
```

## Discussion
現在の実装は空で、処理は行わない。

## References
- [`WKProcessPoolPrivate.h#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L86)
- [`WKProcessPool.mm#L253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L253)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

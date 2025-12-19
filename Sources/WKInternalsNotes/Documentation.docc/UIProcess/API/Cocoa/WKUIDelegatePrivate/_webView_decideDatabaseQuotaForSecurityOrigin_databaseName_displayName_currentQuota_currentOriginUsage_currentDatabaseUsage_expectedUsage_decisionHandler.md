# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:decideDatabaseQuotaForSecurityOrigin:databaseName:displayName:currentQuota:currentOriginUsage:currentDatabaseUsage:expectedUsage:decisionHandler:)``

データベース名付きで容量上限を delegate が決定する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView decideDatabaseQuotaForSecurityOrigin:(WKSecurityOrigin *)securityOrigin databaseName:(NSString *)databaseName displayName:(NSString *)displayName currentQuota:(unsigned long long)currentQuota currentOriginUsage:(unsigned long long)currentOriginUsage currentDatabaseUsage:(unsigned long long)currentUsage expectedUsage:(unsigned long long)expectedUsage decisionHandler:(void (^)(unsigned long long newQuota))decisionHandler;
```

## Discussion
UIClient がこちらを優先し、completionHandler に newQuota を渡す。

## References
- [`WKUIDelegatePrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L141)
- [`UIDelegate.mm#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L159)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

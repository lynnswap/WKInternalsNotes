# ``WKInternalsNotes/WKWebsiteDataStore/_setStorageAccessPromptQuirkForTesting(_:withSubFrameDomains:withTriggerPages:completionHandler:)``

テスト用に Storage Access Prompt Quirk を設定する。

## Objective-C Declaration
```objective-c
- (void)_setStorageAccessPromptQuirkForTesting:(NSString *)topFrameDomain withSubFrameDomains:(NSArray<NSString *> *)subFrameDomains withTriggerPages:(NSArray<NSString *> *)triggerPages completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
永続ストアでのみ `setStorageAccessPromptQuirkForTesting` を呼び、非永続では即 `completionHandler` を実行する。

## References
- [`WKWebsiteDataStorePrivate.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L78)
- [`WKWebsiteDataStore.mm#L940`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L940)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

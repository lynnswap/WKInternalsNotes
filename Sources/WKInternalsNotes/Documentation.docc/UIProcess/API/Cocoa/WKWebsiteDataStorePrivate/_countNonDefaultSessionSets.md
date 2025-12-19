# ``WKInternalsNotes/WKWebsiteDataStore/_countNonDefaultSessionSets(_:)``

非デフォルトセッションセット数を取得する。

## Objective-C Declaration
```objective-c
- (void)_countNonDefaultSessionSets:(void(^)(uint64_t))completionHandler;
```

## Discussion
`countNonDefaultSessionSets` を呼び、取得した件数を `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L126)
- [`WKWebsiteDataStore.mm#L1257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1257)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

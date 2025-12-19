# ``WKInternalsNotes/WKWebsiteDataStore/_renameOrigin(_:to:forDataOfTypes:completionHandler:)``

指定データ種別の origin をリネームする。

## Objective-C Declaration
```objective-c
- (void)_renameOrigin:(NSURL *)oldName to:(NSURL *)newName forDataOfTypes:(NSSet<NSString *> *)dataTypes completionHandler:(void (^)(void))completionHandler;
```

## Discussion
データ種別が空なら即完了し、LocalStorage/IndexedDB 以外を含むと例外を投げる。`SecurityOriginData` に変換して `renameOriginInWebsiteData` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L104)
- [`WKWebsiteDataStore.mm#L1101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

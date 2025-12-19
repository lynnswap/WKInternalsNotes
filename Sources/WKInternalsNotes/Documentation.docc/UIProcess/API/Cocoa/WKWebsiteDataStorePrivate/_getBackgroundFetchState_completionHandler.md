# ``WKInternalsNotes/WKWebsiteDataStore/_getBackgroundFetchState(_:completionHandler:)``

バックグラウンドフェッチの状態を取得する。

## Objective-C Declaration
```objective-c
-(void)_getBackgroundFetchState:(NSString *) identifier completionHandler:(void(^)(NSDictionary *state))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`getBackgroundFetchState` の戻り値を辞書に変換して `completionHandler` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L140)
- [`WKWebsiteDataStore.mm#L1379`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1379)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

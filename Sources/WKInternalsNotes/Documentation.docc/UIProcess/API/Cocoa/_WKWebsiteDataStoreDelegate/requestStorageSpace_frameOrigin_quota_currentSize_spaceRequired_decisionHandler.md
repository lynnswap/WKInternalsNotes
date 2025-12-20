# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/requestStorageSpace(_:frameOrigin:quota:currentSize:spaceRequired:decisionHandler:)``

ストレージ容量の追加要求に対する判断を求める。

## Objective-C Declaration
```objective-c
- (void)requestStorageSpace:(NSURL *)mainFrameURL frameOrigin:(NSURL *)frameURL quota:(NSUInteger)quota currentSize:(NSUInteger)currentSize spaceRequired:(NSUInteger)spaceRequired decisionHandler:(void (^)(unsigned long long quota))decisionHandler;
```

## Discussion
delegate が未設定または未実装の場合は `completionHandler` に空の `optional` を返す。実装済みの場合は `CompletionHandlerCallChecker` で多重呼び出しを防ぎ、`topOrigin`/`frameOrigin` を URL に変換して delegate に渡す。`decisionHandler` で返した quota をそのまま完了値として伝搬する。

## References
- [`_WKWebsiteDataStoreDelegate.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L61)
- [`WKWebsiteDataStore.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L139)
- [`WKWebsiteDataStore.mm#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L157)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |

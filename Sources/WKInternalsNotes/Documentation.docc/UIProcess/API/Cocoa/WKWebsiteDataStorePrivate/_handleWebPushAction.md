# ``WKInternalsNotes/WKWebsiteDataStore/_handleWebPushAction(_:)``

Web Push アクションを処理する。

## Objective-C Declaration
```objective-c
- (void)_handleWebPushAction:(_WKWebPushAction *)webPushAction;
```

## Discussion
- `webPushAction.type` を見て push event / notification click / notification close を振り分ける。
- push event は `_handleNextPushMessageWithCompletionHandler:` でキューを処理する。
- notification click/close は WebCore persistent notification handlers を呼び、完了時に background task を終了する。
- 未知の type はログを出して終了する。

## References
- [`WKWebsiteDataStore.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L96)
- [`WKWebsiteDataStore.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L96)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

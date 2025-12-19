# ``WKInternalsNotes/WKUserContentController/_addScriptMessageHandler(_:name:contentWorld:)``

ContentWorld を指定して script message handler を追加する。

## Objective-C Declaration
```objective-c
- (void)_addScriptMessageHandler:(id <WKScriptMessageHandler>)scriptMessageHandler name:(NSString *)name contentWorld:(WKContentWorld *)contentWorld;
```

## Discussion
`contentWorld._userContentWorld` を使って `userContentWorld` 版の API に委譲する。

## References
- [`WKUserContentControllerPrivate.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L54)
- [`WKUserContentController.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L193)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

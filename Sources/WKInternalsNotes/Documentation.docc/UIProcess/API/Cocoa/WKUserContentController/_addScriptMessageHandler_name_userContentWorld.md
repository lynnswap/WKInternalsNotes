# ``WKInternalsNotes/WKUserContentController/_addScriptMessageHandler(_:name:userContentWorld:)``

user content world を指定して script message handler を追加する。

## Objective-C Declaration
```objective-c
- (void)_addScriptMessageHandler:(id <WKScriptMessageHandler>)scriptMessageHandler name:(NSString *)name userContentWorld:(_WKUserContentWorld *)userContentWorld WK_API_DEPRECATED_WITH_REPLACEMENT("_addScriptMessageHandler:name:contentWorld:", macos(10.11, 11.0), ios(9.0, 14.0));
```

## Discussion
WebScriptMessageHandler を生成して登録し、同名 handler が存在する場合は例外を投げる。

## References
- [`WKUserContentControllerPrivate.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L54)
- [`WKUserContentController.mm#L320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L320)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

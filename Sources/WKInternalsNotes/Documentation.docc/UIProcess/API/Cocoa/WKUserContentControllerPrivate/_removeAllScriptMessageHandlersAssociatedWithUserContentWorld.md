# ``WKInternalsNotes/WKUserContentController/_removeAllScriptMessageHandlersAssociatedWithUserContentWorld(_:)``

指定 user content world の script message handler を全て削除する。

## Objective-C Declaration
```objective-c
- (void)_removeAllScriptMessageHandlersAssociatedWithUserContentWorld:(_WKUserContentWorld *)userContentWorld;
```

## Discussion
`removeAllUserMessageHandlers` を呼び出し、指定 world の handler を削除する。

## References
- [`WKUserContentControllerPrivate.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L60)
- [`WKUserContentController.mm#L337`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L337)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

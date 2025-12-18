# ``WKInternalsNotes/WKUserContentController/_removeScriptMessageHandlerForName(_:userContentWorld:)``

指定 name の script message handler を削除する。

## Objective-C Declaration
```objective-c
- (void)_removeScriptMessageHandlerForName:(NSString *)name userContentWorld:(_WKUserContentWorld *)userContentWorld;
```

## Discussion
指定された name と user content world を使って handler を削除する。

## References
- [`WKUserContentControllerPrivate.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L59)
- [`WKUserContentController.mm#L332`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L332)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

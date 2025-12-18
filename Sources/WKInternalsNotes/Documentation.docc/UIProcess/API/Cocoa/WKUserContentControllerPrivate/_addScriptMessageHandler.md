# ``WKInternalsNotes/WKUserContentController/_addScriptMessageHandler(_:)``

WebScriptMessageHandler を内部登録する。

## Objective-C Declaration
```objective-c
- (void)_addScriptMessageHandler:(WebKit::WebScriptMessageHandler&)scriptMessageHandler;
```

## Discussion
同名の handler が既に存在する場合は例外を投げ、それ以外は `addUserScriptMessageHandler` で登録する。

## References
- [`WKUserContentControllerInternal.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerInternal.h#L45)
- [`WKUserContentController.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L193)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

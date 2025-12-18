# ``WKInternalsNotes/WKUserContentController/_addUserScriptImmediately(_:)``

User script を即時注入で追加する。

## Objective-C Declaration
```objective-c
- (void)_addUserScriptImmediately:(WKUserScript *)userScript WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`InjectUserScriptImmediately::Yes` を指定して追加する。

## References
- [`WKUserContentControllerPrivate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentControllerPrivate.h#L39)
- [`WKUserContentController.mm#L258`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserContentController.mm#L258)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

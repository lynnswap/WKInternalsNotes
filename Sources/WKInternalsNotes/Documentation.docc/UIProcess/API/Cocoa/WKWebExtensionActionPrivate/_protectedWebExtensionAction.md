# ``WKInternalsNotes/WKWebExtensionAction/_protectedWebExtensionAction()``

内部 WebExtensionAction を `Ref` で返す。

## Objective-C Declaration
```objective-c
- (Ref<WebKit::WebExtensionAction>)_protectedWebExtensionAction;
```

## Discussion
`*_webExtensionAction` を `Ref<WebKit::WebExtensionAction>` として返し、内部オブジェクトの寿命を保持した参照を提供する。

## References
- [`WKWebExtensionActionInternal.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionActionInternal.h#L47)
- [`WKWebExtensionAction.mm#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionAction.mm#L165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

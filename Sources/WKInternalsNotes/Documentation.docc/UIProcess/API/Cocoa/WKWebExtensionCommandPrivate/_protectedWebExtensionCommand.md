# ``WKInternalsNotes/WKWebExtensionCommand/_protectedWebExtensionCommand()``

内部 WebExtensionCommand を `Ref` で返す。

## Objective-C Declaration
```objective-c
- (Ref<WebKit::WebExtensionCommand>)_protectedWebExtensionCommand;
```

## Discussion
`*_webExtensionCommand` を `Ref<WebKit::WebExtensionCommand>` として返し、内部オブジェクトの寿命を保持した参照を提供する。

## References
- [`WKWebExtensionCommandInternal.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommandInternal.h#L46)
- [`WKWebExtensionCommand.mm#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L169)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |

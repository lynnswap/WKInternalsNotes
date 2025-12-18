# ``WKInternalsNotes/WKWebExtension/_protectedWebExtension()``

内部 WebExtension を `Ref` で返す。

## Objective-C Declaration
```objective-c
-(Ref<WebKit::WebExtension>)_protectedWebExtension;
```

## Discussion
`*_webExtension` を `Ref<WebKit::WebExtension>` として返し、内部オブジェクトの寿命を保持した参照を提供する。

## References
- [`WKWebExtensionInternal.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionInternal.h#L47)
- [`WKWebExtension.mm#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L354)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
